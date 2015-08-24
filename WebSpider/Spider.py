__author__ = 'clark'
#coding=utf-8

import urllib
from WebSpider import ParserHtml

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml('http://www.douguo.com/cookbook/1231705.html')

# open('douguo1.html', 'w').write(html)
fcbm = ParserHtml.GetFCBM()
fcbm.feed(html)

print(fcbm.getHead())
material = fcbm.getMaterial()
for one in material:
    print(one)

steps = fcbm.getStep()
for ones in steps:
    for one in ones:
        print(one)
# material = fcbm.getMaterial()
# for i in material:
#     print(i)