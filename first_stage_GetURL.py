# -*- coding: utf-8 -*-

#urllib模块提供的上层接口，使我们可以像读取本地文件一样读取www和ftp上的数据
#参考网址：http://www.blogjava.net/ashutc/archive/2011/03/21/346695.html
import urllib

str0 = '<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102eo83.html">《论电影的七个元素》——关于我对电…</a>'

#找到<a title位置,并以字符“<”作为位置编号，这就是“0”
title = str0.find(r'<a title')
print title

#找到href=位置,并以字符“h”作为位置编号，这就是“28”
href = str0.find(r'href=')
print href
#找到.html位置,并以字符“.”作为位置编号，这就是“81”
html = str0.find(r'.html')
print html

#去除多余部分，截取完整html地址
#href + 6从href位置开始的第6位置
#html +5从html位置开始的第5位置
url = str0[href + 6:html +5]
print url

#通过获得的url抓取其整个htlm,并将抓取的内容赋值给变量content
content = urllib.urlopen(url).read()
print content

#设置文件名字，字符串切片，[-26:]表示倒数第26个到最后的字符串
filename = url[-26:]
print filename

#将内容写入到名为filename的文件中
open(filename,'w').write(content)
