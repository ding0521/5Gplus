# -*- coding:utf-8 -*-

# 1. 批量重命名文件，批量在文件名前加上“IMT|”
# 将 '180204-filename.md' 改为 'IMT|180204-filename.md'
# 也就是说，只提取文件名,在其前面添加“IMT|”即可；

# 算法：

# 读取所有文件名，存储在数组fNams中；
# 读取每个文件名fname，将“ITM|”拼接在fname前，存储在new_fName;
#从new_fName中读取文件名，并重命名之前文件；

from sys import argv

import os

filePath = './'

fNameList = os.listdir(filePath)
n_fNameList = [len(fNameList)]

for fname in fNameList:
    n_fname = 'IMT|'+fname
    
    #n_fNameList.append(n_fname)
    os.rename(fname, n_fname)




# 2. 批量在文件前写入以下格式：

'''
---
layout:     post
title:      
subtitle:   
date:       
author:     慕广陵
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 
    - 
--- 

'''                         
