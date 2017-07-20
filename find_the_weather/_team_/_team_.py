# -*- coding: utf-8 -*-
import csv #python中的import语句是用来导入模块的,在这里导入了CSV模块
with open('_team_.tsv', encoding='utf8') as f: #对于大文件，用with open(xx) as fp:  for line in fp:方式来读取 
    reader = csv.DictReader(f) #用reader的方式对csv文件进行读取使用
    print ('\t'.join(reader.fieldnames))
    for r in reader: #运用了for循环
        print ('\t'.join([r[k] for k in reader.fieldnames]) ) 
