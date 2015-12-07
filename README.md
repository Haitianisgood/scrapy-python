# scrapy-python
scrapy write by python


#爬虫

##新浪博客文章列表特征

```
<a title=.... href=...  .html>
```

##技术要点

* 字符串函数find
* 列表list[-x:-y]
* 文件读写操作
* 循环体while
* 库函数urllib

###字符串函数find
```
$ python
 >>> help(str.find)
````

###库函数urlib
爬虫通过url抓取web内容的库,需要在源文件导入此库
```
import urllib
```

##Advancement_Get_List_Content.py功能

###获取第一页所有文章的URL

```
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
```

###将第一页所有文章下载到本地

```
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
```

##Advancement_Get_ALL_Content.py功能

###循环每页
```
page = 1

#文章总页数
page_size = 7

while page <= page_size:

  while：
   获取文章url
  else：
   print '第',page,'页','All article\'s URL find end!\n'
   
  while：
   通过上面获取的ur，下载所有文章
  else：
   print '第',page,'页','Download article finished!'


    page = page + 1
else:
    print 'All article find and download end!'

```

###访问新浪“博文目录”并获取文章列表中各个文章URL
```
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

```

###通过上面获取的URL，获取"博文目录"每页列表中各文章中的内容下载到本地

```
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
        
```

