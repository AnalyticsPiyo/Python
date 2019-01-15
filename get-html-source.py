# -*- coding: utf-8 -*-
"""
@author: hideyuki.takase
"""

import urllib.request
f = open('test.txt', 'w')
filehandle = urllib.request.urlopen("http://iss.ndl.go.jp/api/opensearch?title=DataScience")

for i in range(5720):
   objStr= filehandle.readline().decode("utf-8")
   if "<pubDate>" in objStr:
       f.write(objStr)
f.close()
