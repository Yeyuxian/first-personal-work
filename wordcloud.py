# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:41:16 2021

@author: ASUS
"""

import requests
import re
import time
#准备工作
url = 'https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1614174646181'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
html = requests.get(url,headers = headers).content.decode()
print(html)
comments_list = list()
totalcom = int(re.findall('"oritotal":(.*?),',html,re.S)[0])
print(totalcom)
rangetime = round((totalcom - 10)/10)+1
print(rangetime)
t = int(time.time())
print(t)
now = t + 3
n = 1
m = 1
print(now,n,m)
cursor = 0

#获取评论
for i in range(rangetime):
    print("获取第{}集，第{}页的评论".format(str(n),str(m)))
    url_content = 'https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + str(cursor) + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=' + str(t)
    html = requests.get(url_content,headers=headers).content.decode()
    contents = re.findall('"content":"(.*?)"',html,re.S)[0]
    cursor = re.findall(',"last":"(.*?)",',html,re.S)[0]
    m += 1
    t = now
    now += 1
    #print(contents)
    comments_list.append(contents)
    #print(comments_list)
    
#写入TXT文档

with open("comments.txt", "w", encoding="GBK", errors="ignore") as f:
        for i in comments_list:
            f.write(str(i))
            f.write("\n")
            
#过滤  
          
filter = list()
with open('comments.txt','r',errors='ignore') as f:
    lines = f.readlines()
    for s in lines:
        word = re.findall('[\u4e00-\u9fa5]', s)
        if len(word) == 0:
            continue
        else:
            new = ''.join(word)
        filter.append(new)
#写入新的TXT文档
with open('filter_comments.txt','w') as f:
    for s in filter:
        f.write(s)       