#!/usr/bin/python   
#-*-coding=utf-8-*-   
  
import os,sys,re,time;   

class Replacer:
    def __init__(self, countryCode):
        print("self.countryCode: " + countryCode);
        self.countryCode = countryCode

    def existedGroup(matchobj, index):
        try:
           matchobj.group(index)
        except IndexError:
           return '';
        else:
           return matchobj.group(index);

    def replace(self, matchobj):
        matchedStrBeforeCountryCode = Replacer.existedGroup(matchobj, 1);
        matchedCountryCode = matchobj.group(2);
        matchedStrAfterCountryCode = Replacer.existedGroup(matchobj, 3);
        if matchedCountryCode.isupper():
             return matchedStrBeforeCountryCode + self.countryCode.upper() + matchedStrAfterCountryCode;
        else:
             return matchedStrBeforeCountryCode + self.countryCode.lower() + matchedStrAfterCountryCode; 

  
odir = input('请输入目录:');   
  
ext = input('需要替换的文件后缀(含.):');   

sta = input('请输入正则表达式(多个正则表达式以,隔开):');   
  
# strb = input('替换后的字符串:');     
  
os.chdir(odir);   
  
c1 = os.walk(os.getcwd());   
  
filelist = [];   
  
# stra = re.compile(sta,re.DOTALL);

# expression = r"%s" % sta;

# stra = re.compile(expression, re.DOTALL);   
  
for c2 in c1:   
    for c3 in c2[2]:   
        c4 = os.path.join(c2[0],c3);   
        c5 = os.path.splitext(c4);   
        if c5[1] == ext:   
            filelist.append(c4);   
        else:   
            pass;   
print(filelist);   
  
for filename in filelist:  
    countryCode = filename[len(filename)-len(ext)-2:len(filename)-len(ext)];
    print("countryCode: "+ countryCode);
    myReplacer = Replacer(countryCode).replace;

    for stra in sta.split(","):
        fileread = open(filename,'r');   
        filer = fileread.read();
        expression = r"%s" % stra;
        # re.purge();
        print(stra);
        strare = re.compile(expression, re.DOTALL);  
        sub = re.sub(strare, myReplacer, filer, 0);
        fileread.close();   
        fileok = open(filename,'w');   
        fileok.write(sub);   
        fileok.close();
    print(filename);   
    print('替换成功!');