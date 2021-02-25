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
