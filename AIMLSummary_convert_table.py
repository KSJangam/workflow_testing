#!/usr/bin/env python
# coding: utf-8


import pandas
import argparse
import json


parser=argparse.ArgumentParser(description="io files")
parser.add_argument("inputfile", type=argparse.FileType('r'), help="input file")
parser.add_argument("outputfile", type=str, help="output file")
args=parser.parse_args()

df1=pandas.read_csv(args.inputfile, encoding='UTF-8', keep_default_na=False)

col_names=df1.columns

data = {'name':'Classification', 'parent':"null", 'children':[]}

def parse_row(row, index, parent, l):
    if len(col_names)>index and row[col_names[index]]=="":
        return parse_row(row, index+1, parent, l)
    
    if len(col_names)>index+1:
        item = [x for x in l if x['name']==row[col_names[index]]]
        if len(item)==0:
            children=[parse_row(row, index+1, row[col_names[index]], [])]
            if children == [""]:
                return {'name':row[col_names[index]], 'parent':parent}
            else:
                return {'name':row[col_names[index]], 'parent':parent, 'children':children}
        else:
            children=item[0]['children']
            new_item=parse_row(row, index+1, row[col_names[index]], children)
            if new_item != "":
                added=False
                for num in range(len(children)):
                    if children[num]['name']==new_item['name']:
                        children[num]=new_item
                        added=True
                if not added:
                    children.append(new_item)
            return {'name':row[col_names[index]], 'parent':parent, 'children':children}
    elif len(col_names)==index+1:
        if row[col_names[index]]=="":
            return ""
        else:
            return {'name':row[col_names[index]], 'parent':parent}
    
    return ""
            

df1 = df1.reset_index()  
for index, row in df1.iterrows():
    i=0
    while(row[col_names[i]]==""):
        i=i+1  
    new_item = parse_row(row, i, data['name'], data['children'])
    added=False
    for num in range(len(data['children'])):
        if data['children'][num]['name']==new_item['name']:
            data['children'][num]=new_item
            added=True
    if not added:
        data['children'].append(new_item)


with open(args.outputfile, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)