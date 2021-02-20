#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = r'C:\Users\whl5378\Desktop\1.21\test2\und - 副本\\'

f=os.listdir(path)
n=0
for i in f:
    oldname=path+f[n]
    newname=path+str(n)+'_'+'und'+'.jpg'
    os.rename(oldname,newname)
    print(oldname,'=====>',newname)

    n+=1