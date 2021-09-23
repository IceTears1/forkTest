#!/usr/bin/python3

import os

rootFile = '/Users/ice/ICE/test/'
class ForkModel:
    fileName = ''
    originUrl = ''
    upstreamUrl = ''
    originBranch = ''
    upstreamBranch = ''

    def __init__(self,fileName,originUrl,upstreamUrl,originBranch,upstreamBranch):
        self.fileName = fileName
        self.originUrl = originUrl
        self.upstreamUrl = upstreamUrl
        self.originBranch = originBranch
        self.upstreamBranch = upstreamBranch

    def log(self):
        str = " fileName:%s \n originUrl:%s \n upstreamUrl:%s \n originBranch:%s\n upstreamBranch:%s \n"%(self.fileName,self.originUrl,self.upstreamUrl,self.originBranch,self.upstreamBranch)
        print(str)
        
    def show(self):
        str = " fileName:%s \n originUrl:%s \n upstreamUrl:%s \n originBranch:%s\n upstreamBranch:%s \n"%(self.fileName,self.originUrl,self.upstreamUrl,self.originBranch,self.upstreamBranch)
        return str

a = ForkModel('forkTest','https://github.com/IceTears1/forkTest.git','https://github.com/Fly985/forkTest.git','main','main')

print('-------------设置数据源----------')
# a.log()
list = [a]
def logAllFile():
    a = os.popen('ls -a');
    for item in a.readlines():
        print("所有文件： " + item)

def fileExit(str):
    a = os.popen('ls');
    exit = False
    for item in a.readlines():
        temp_item = item.replace('\n','')
        b = "true"
        if exit:
            b = 'true'
        else:
            b = 'false'
       
        if temp_item==str:
            exit = True
            break
    return exit    
    

#执行shell 命令
for item in list:
    print('-------------开始 ---------- \n' + item.show())
    #进入根目录
    os.chdir(rootFile) 
    #判断库是否存在
    isexit = fileExit(item.fileName)
    if isexit:
        print('仓库已存在')
    else:
        print('仓库不存在')
        a = 'git clone ' + item.originUrl
        f = os.popen(a, "r")
        # shuchu = f.read()
        f.close()
    print('-----------------')
    #进入库目录
    os.chdir(rootFile + item.fileName)
    f = os.popen('git remote -v', "r")
    isExit_upstream = True
    
    for i in f.readlines():
        # print('--'+i+'---')
        if i.startswith("upstream"):
            isExit_upstream = True
            break
        else:
            isExit_upstream = False
        
    if isExit_upstream:
        print('存在 upstream')
    else:
        print('没有远程upstream')
        a1 = 'git remote add upstream ' + item.upstreamUrl
        f1 = os.popen(a1, "r")
        f1.close()
    print('\n\n-----upstream 配置完成 -------\n\n')
    #抓取 原仓库的更新    
    a2 = 'git fetch upstream'
    f2 = os.popen(a2, "r")
    f2.close()
    print('原仓库的 拉取...\n')

     #切换到 master 分支  
    a3 = 'git checkout ' + item.originBranch
    f3 = os.popen(a3, "r")
    f3.close()
    print('切换主分支...\n')
    #抓取 合并到本地仓库    
    a4 = 'git merge upstream/' + item.upstreamBranch
    f4 = os.popen(a4, "r")
    f4.close()
    print('合并到本地仓库...\n')
    #push   
    a5 = 'git push origin ' + item.originBranch
    f5 = os.popen(a5, "r")
    f5.close()
    print('push 完成...\n')
    print('\n\n-----end-------\n\n')