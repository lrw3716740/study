#coding:utf-8
import os
path="F:\Project"
def gci (path):

    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path,parent)
        if os.path.isdir(child):
            gci(child)
        else:
            print(child)

gci(path)