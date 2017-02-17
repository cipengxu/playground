source ./profile.conf

# Level 1
_integration_test_resources_path="${_nucleus_path}/integration.test.resources"
_caseproperties_path="${_nucleus_path}/caseproperties"

# Level 2
_eadp_test_client_path="${_nucleus_path}/eadp.test.client"
_eadp_legacy_test_client_path="${_nucleus_path}/eadp.legacy.test.client"
_integration_test_pom_parent_path="${_nucleus_path}/integration.test.pom.parent"
_qahandlers_path="${_nucleus_path}/qahandlers"

# Level 3
_test_shared_path="${_nucleus_path}/test.shared"
_nucleus_test_utils_path="${_nucleus_path}/nucleus.test.utils"
_catalog_service_path="${_nucleus_path}/catalog/catalog.service"
_catalog_model_path="${_nucleus_path}/catalog/catalog.model"
_catalog_notification_path="${_nucleus_path}/catalog/catalog.notification"

# Level 4
_catalog_integration_path="${_nucleus_path}/catalog-integration"

# Level 5
_catalog_ui_integration_path="${_nucleus_path}/catalog.ui-integration"

function check_status() {
    if [[ $1 != "0" ]]; then
        echo -e $2
        exit 1
    fi
}

function build_maven_project() {
    cd $1
    check_status $? "directory $1 does not exist"
    echo "------------------------------BUILD $1 ......------------------------------"
    mvn clean install -DskipTests
    check_status $? "------------------------------BUILD FAILURE------------------------------\nDirectory: $1\n-------------------------------------------------------------------------\n"
    echo -e "------------------------------BUILD SUCCESS------------------------------\nDirectory: $1\n-------------------------------------------------------------------------\n"
}

function build_dependency() {
    build_maven_project $_integration_test_resources_path
    
    build_maven_project $_caseproperties_path
    
    build_maven_project $_eadp_test_client_path
    
    build_maven_project $_eadp_legacy_test_client_path
    
    build_maven_project $_integration_test_pom_parent_path
    
    build_maven_project $_qahandlers_path
    
    build_maven_project $_test_shared_path
    
    build_maven_project $_nucleus_test_utils_path
    
    build_maven_project $_catalog_service_path
    
    build_maven_project $_catalog_model_path
    
    build_maven_project $_catalog_notification_path
    
    build_maven_project $_catalog_integration_path
    
    build_maven_project $_catalog_ui_integration_path
}

function main() {
    #ignore '\r' in sh files
    set -o igncr

    cd $_nucleus_path
    check_status $? "nucleus directory ${_nucleus_path} not found\n"

    build_dependency
    
    check_status $? "------------------------------BUILD ALL DEPENDENCIES FAILURE------------------------------\n"
    echo -e "------------------------------BUILD ALL DEPENDENCIES SUCCESS------------------------------\n"
}

main $@