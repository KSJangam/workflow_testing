#!/usr/bin/env python
# coding: utf-8


import pandas
import argparse
import os 
parser=argparse.ArgumentParser(description="io files")

#parser.add_argument("inputfile", type=argparse.FileType('r'), help="input file")

parser.add_argument("outputfile", type=argparse.FileType('w'), help="output file")
args=parser.parse_args()
x="input/"+os.listdir("input")[0]


df1=pandas.read_csv(x, encoding = "ISO-8859-1", engine='c', keep_default_na=False)

nodes = dict() #create dictionary to store the ID of classification nodes
i = 1 #keep a counter to assign node ID



cols=[list() for num in range(3)]


col_names=df1.columns


df1 = df1.reset_index()  # make sure indexes pair with number of rows
for index, row in df1.iterrows():
    if row[col_names[0]]+str(0) not in nodes.keys() and row[col_names[0]]!="":
        nodes[row[col_names[0]]+str(0)]=[i, [0]]
        cols[0].append(0)
        cols[1].append(i)
        cols[2].append(row[col_names[0]])
        i=i+1
    for num in range(1, len(col_names)):
        if row[col_names[num]]!="": 
            backstep=1
            while num-backstep>=0 and row[col_names[num-backstep]]=="":
                backstep=backstep+1
            if num-backstep<0:
                p=0
            else:
                p=nodes[row[col_names[num-backstep]]+str(num-backstep)][0]
            if row[col_names[num]]+str(num) not in nodes.keys(): 
                nodes[row[col_names[num]]+str(num)]=[i, [p]]  
                cols[0].append(p)
                cols[1].append(i)
                cols[2].append(row[col_names[num]])
                i=i+1
            elif p not in nodes[row[col_names[num]]+str(num)][1]:
                nodes[row[col_names[num]]+str(num)][1].append(p)
                cols[0].append(p)
                cols[1].append(nodes[row[col_names[num]]+str(num)][0])
                cols[2].append(row[col_names[num]])


d = {'ParentID':cols[0], 'ChildID':cols[1], 'Name':cols[2]}
df = pandas.DataFrame(data = d)
df.head(15)



df.to_csv(args.outputfile, encoding= 'unicode_escape', index=False)



df.tail(15)

