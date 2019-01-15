#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# 参考URL：https://dev.twitter.com/rest/public/search

from requests_oauthlib import OAuth1Session
import json

CONSUMER_KEY = "****"
CONSUMER_SECRET = "****"
ACCESS_TOKEN = '****'
ACCESS_TOKEN_SECRET = '****'

qk = "****"

# ファイルに書き出し
f = open(qk + '.txt', 'a')

url =  "https://api.twitter.com/1.1/search/tweets.json"

# 指定パラメータ
params = {"q": qk,
          "count":"100",
          "result_type":"recent"}

# OAuth で GET
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
req = twitter.get(url, params = params)

if req.status_code == 200:
    # レスポンスはJSON形式なので parse する
    timeline = json.loads(req.text)

    i = 1
    # 各ツイートの本文を表示
    for tweet in timeline["statuses"]:
        try:
            print(tweet['text'])
            print("------------------------")
           
            f.write(tweet['text'] + "\n")
            f.write("------------------------\n")
            i = i + 1
        except:            
            print("Error")
            print("------------------------")

else:
    # エラーの場合
    print ("Error: %d" % req.status_code)

f.close()