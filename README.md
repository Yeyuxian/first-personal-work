# first-personal-work

## 主要目的（mian purpose）
    采集腾讯视频里电视剧《在一起》的全部评论信息
    
## 粗略过程（rough process）
 1. 利用爬虫爬取评论
 2. 过滤评论
 3. 利用 **jieba** 将评论拆分
 4. 利用 **echarts** 将拆分的评论进行词云图制作
 5. 展示写好的html

## 完成情况（completion)
|过程|利用时间|完成情况|
|:-----:|:------:|:------:|
|爬取评论|2h|部分完成|
|过滤评论|30min|完成|
|评论拆分|1h|完成|
|json转换|1h|完成|
|制作词云图|1h|完成|
|git上传|1h|完成|

## 文件功能（file function）
- wordcloud.py(爬取评论的代码)
- wordcloudjson.py(将评论转换为json格式的代码)
- comments.txt(爬取的评论)
- filter_comments.txt(过滤后的评论)
- comments.json(转换为json格式的评论)
- wordCloud.html(完成渲染后的网页)
