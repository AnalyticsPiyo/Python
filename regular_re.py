#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# 正規表現
# http://news.mynavi.jp/series/python/013/

# 上を読んでからだと効果的
# http://qiita.com/Shadow/items/ce272419dde2f95cdabc

import re

# match  先頭からのみ対応
print re.match('\d+', '123abc') != None   # True
print re.match('\d+', 'abc123') != None   # False

# search
print re.search('^\d+', '123abc') != None  # True
print re.search('^\d+', 'abc123') != None  # False
print re.search('\d+', 'abc123') != None   # True

# 返り値はmatch型のobject　←　これを操作する

# マッチする文字列を全部取得
l = re.findall('\d+', '123abc456def')
print l  # ['123', '456']

l = re.findall('\d+', 'abc def')
print l  # []

# 正規表現のコンパイル化(高速化)
regex = re.compile('[^\d]*(\d+).*$')
m = regex.match('hello324 hoge321')
print m.groups() # ('324',)
m = regex.match('324 hoge321')
print m.groups()  # ('324',)