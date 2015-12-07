# scrapy-python
scrapy write by python


#爬虫

##新浪博客文章列表特征

<a title=.... href=...  .html>

##技术要点

* 字符串函数find
* 列表list[-x:-y]
* 文件读写操作
* 循环体while

###字符串函数find
```
$ python
 >>> help(str.find)
````
##Advancement_Get_List_Content.py功能

###获取第一页所有文章的URL


#扒取文章目录的网址url

```
list_url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
#扒取文章目录列表的数
list_size = 50
#存储四十个文章的链接列表
url = ['']*list_size

con = urllib.urlopen(list_url).read()

#找到<a title=位置,并以字符“<”作为位置编号
title = con.find(r'<a title=')

#找到href=位置,并以字符“h”作为位置编号，并指定从title开始搜
href = con.find(r'href=',title)

#找到.html位置,并以字符“.”作为位置编号，并指定从href开始搜
html = con.find(r'.html',href)

i = 0

while title != -1 and href != -1 and html != -1 and i < list_size:
    #去除多余部分，截取完整html地址
    #href + 6:从href位置开始的第6位置
    #html +5:从html位置开始的第5位置
    url[i] = con[href + 6:html + 5:]
    print i+1
    print url[i]
    #下一个文章链接，肯定是在上一个文章链接html后面
    title = con.find(r'<a title=',html)
    #找到href=位置,并以字符“h”作为位置编号，并指定从title开始搜
    href = con.find(r'href=',title)

    #找到.html位置,并以字符“.”作为位置编号，并指定从href开始搜
    html = con.find(r'.html',href)
    i = i + 1
else:
    print 'Find end!'
```

###将第一页所有文章下载到本地

###访问新浪“博文目录”并获取文章列表中各个文章URL
###获取"博文目录"第一页列表中各文章中的内容下载到本地
















