# -*- coding: utf-8 -*-

#urllib模块提供的上层接口，使我们可以像读取本地文件一样读取www和ftp上的数据
#参考网址：http://www.blogjava.net/ashutc/archive/2011/03/21/346695.html
import urllib
import time

page = 1

#文章总页数
page_size = 7

#扒取每页文章目录列表的文章数
list_size = 50

#存储文章的链接列表
url = ['']*list_size
#抓取文章url编号
url_number = 1

while page <= page_size:
    #扒取文章目录的网址url
    list_url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(page)+'.html'
    #通过获得的list_url抓取其整个htlm,并将抓取的内容赋值给变量con
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
        print url_number,url[i]
        #下一个文章链接，肯定是在上一个文章链接html后面
        title = con.find(r'<a title=',html)
        #找到href=位置,并以字符“h”作为位置编号，并指定从title开始搜
        href = con.find(r'href=',title)

        #找到.html位置,并以字符“.”作为位置编号，并指定从href开始搜
        html = con.find(r'.html',href)
        i = i + 1
        url_number = url_number + 1
    else:
        print '第',page,'页','All article\'s URL find end!\n'

    j = 0

    while j < list_size:
        #通过获得的url抓取其整个网页内容并赋值给变量content
        content = urllib.urlopen(url[j]).read()
        #'+w'表示，当前面文件('hanhan/'+url[j][-26:]是文件名)不存在的时候创建
        open(r'hanhan/' + url[j][-26:],'w+').write(content)
        print '第',page,'页','第',j+1,'篇','Downloading',url[j]

        j = j + 1


        #使用python内置函数time，前面要事先导入
        #time.sleep(1)
    else:
        print '第',page,'页','Download article finished!'

    page = page + 1
else:
    print 'All article find and download end!'


