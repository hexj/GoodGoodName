#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os 

def splitfile():
    # numarr = dict([("一","01")("二","02")("三","03")("四","04")("五","05")("六","06")("七","07")])
    filename = "src-data/srcfile.txt"
    with open(filename, 'r') as f:
        lines = f.readlines()
        cnt = 0
        # print('dict([', end="")
        wfn = ""
        for line in lines:
            if("画宝宝" in line):
                cnt = cnt+1
                zi = line[0:3]
                wfn = "data/0{0}.txt".format(cnt)
                # print('("{0}","0{1}")'.format(zi, cnt), end="")
            else:
                with open(wfn,'a') as wf:
                    wf.write(line)
                print(line)
        # print('])')
def main():
    g = os.walk(r"data")
    for path,dir_list,file_list in g:  
        for file_name in file_list:  
            # print(file_name)
            print(os.path.join(path, file_name) )

    pass

if __name__ == '__main__':
    main()