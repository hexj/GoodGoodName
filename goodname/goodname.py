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
        # print('{', end="")
        wfn = ""
        for line in lines:
            if("画宝宝" in line):
                cnt = cnt+1
                zi = line[0:3]
                if(cnt < 10):
                    wfn = "data/0{0}.txt".format(cnt)
                else:
                    wfn = "data/{0}.txt".format(cnt)
                print(wfn)
                # print('("{0}":"0{1}")'.format(zi, cnt), end="")
            else:
                with open(wfn, 'a') as wf:
                    wf.write(line)
                # print(line)
        # print('}')


def list_data_filename():
    g = os.walk(r"data")
    for path, dir_list, file_list in g:
        for file_name in file_list:
            dtfn = os.path.join(path, file_name)
            print(dtfn)
            with open(dtfn, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    rowarr = line.split('：')
                    print(rowarr)
                    break
            break


def filter_bad(cnt):
    if(int(cnt)>27 or int(cnt)<2):
        return []
    if(len(cnt) ==1):
        cnt = "0{0}".format(cnt)
    fname = "data/{0}.txt".format(cnt)
    ngwd = '欠|祸|厄|刑|伤|凶|困|病|亡|破|厄|灾|败|弱|劳累|劳神|劳苦|不幸|不祥|多疾|克父|克母|忧心|多忧|潦倒|中年劳|多劳|奔波|酸|苦'
    ngarr = ngwd.split('|')
    gd = []
    with open(fname, 'r') as f:
        lines = f.readlines()
        for line in lines:
            filter = False
            for ng in ngarr:
                if(ng in line):
                    filter = True
                    # print(ng, '-----', line)
                    break
            if(filter == False):
                print(line,end="")
                # print(line[:1])
                gd.append(line[:1])
    return gd

def compu(bh1,bh2):
    cparr = []
    zi1 = filter_bad(bh1)
    zi2 = filter_bad(bh2)
    for zi in zi1:
        for z in zi2:
            cparr.append("{0}{1}".format(zi,z))
    return cparr

def main(args):
    # list_data_filename()
    # splitfile()
    print(args)
    cparr = compu(args[1], args[2])
    with open("zuhe.txt", 'a') as wf:
        if(cparr is not None and len(cparr) >1):
            for zh in cparr:
                wf.write(zh)
                wf.write("\n")
    print(cparr)
    # if(len(args) >= 2):
    #     for cnt in args[1:]: 
    #         print("{0}画字".format(cnt))
    #         filter_bad(cnt)

import sys
if __name__ == '__main__':
    main(sys.argv)
