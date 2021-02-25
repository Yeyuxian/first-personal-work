# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:37:10 2021

@author: ASUS
"""

import json
import jieba

#排序
commentList = open('filter_comments.txt', 'r',errors = 'ignore').read()

words = jieba.lcut(commentList)
wordCounts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        wordCounts[word] = wordCounts.get(word, 0) + 1
items = list(wordCounts.items())
items.sort(key=lambda x: x[1], reverse=True)
#写入字典
countList = []
for i in range(len(items)):
    countDict = {}
    word, count = items[i]
    if count >= 10:
        countDict['name'] = word
        countDict['value'] = count
        countList.append(countDict)
# print(countList)
data = {}
data['data'] = countList
print(data)
with open('comments.json', 'w',errors = 'ignore') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)