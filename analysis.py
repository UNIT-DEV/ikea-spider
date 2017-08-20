#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

def output(content, target):
    with open(target, 'w') as f:
        for i in content:
            f.write(i + '\n')

with open('result.csv', 'rb') as f:
    results = csv.reader(f, delimiter=',')
    categories = set([])
    products = set([])
    features = set([])
    broads = set([])
    row = 0    
    for result in results:
        if row == 0:
            row += 1
            continue
        categories.add(result[0])
        product = result[1]
        if ',' in product or '，' in product or re.match(r'\d+', product):
            pass
        elif '+' in product:
            ps = product.split('+')
            for p in ps:
                if not re.match(r'\d+', p):
                    products.add(p)
        elif '/' in product:
            ps = product.split('/')
            if not re.match(r'\d+', ps[0]):
                products.add(ps[0])
        elif '和' in product:
            ps = product.split('和')
            for p in ps:
                if not re.match(r'\d+', p):
                    products.add(p)     
        else:
            if not re.match(r'\d+', product):
                products.add(product)
        if result[4] != None and result[4] != '':
            features.add(result[4])
        if result[2] != None and result[2] != '':
            broad = result[2].strip()
            bb = []
            if '/' in broad:
                bs = broad.split('/')
            elif ' ' in broad:
                bs = broad.split(' ')
            else:
                bs = [broad]
            for b in bs:
                if ' ' in b:
                    bbb = b.split(' ')
                    for bbb in bb:
                        if not re.match(r'[\u4e00-\u9fa5]+', bbb.strip()):
                            broads.add(bbb.strip())
                else:
                    if not re.match(r'[\u4e00-\u9fa5]+', b.strip()):
                        broads.add(b.strip())
    output(categories, 'dict/categories.txt')
    output(products, 'dict/products.txt')
    output(features, 'dict/features.txt')
    output(broads, 'dict/broads.txt')
