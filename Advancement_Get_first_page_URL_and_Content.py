# -*- coding: utf-8 -*-

#urllib模块提供的上层接口，使我们可以像读取本地文件一样读取www和ftp上的数据
#参考网址：http://www.blogjava.net/ashutc/archive/2011/03/21/346695.html
import urllib
import time

#扒取文章目录的网址url
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

#设定循环文章变量，并循环50次。因为每页文章最多是50篇文章
 j = 0

while j < 50:
    #通过获得的url抓取其整个网页内容并赋值给变量content
    content = urllib.urlopen(url[j]).read()
    #'+w'表示，当前面文件('hanhan/'+url[j][-26:]是文件名)不存在的时候创建
    open(r'hanhan/' + url[j][-26:],'w+').write(content)
    print 'Downloading ',url[j]

    j = j + 1

    #使用python内置函数time，前面要事先导入
    time.sleep(1)
else:
    print 'Download article finished!'


