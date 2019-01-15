#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# �Q�lURL�Fhttps://dev.twitter.com/rest/public/search

from requests_oauthlib import OAuth1Session
import json

CONSUMER_KEY = "****"
CONSUMER_SECRET = "****"
ACCESS_TOKEN = '****'
ACCESS_TOKEN_SECRET = '****'

qk = "****"

# �t�@�C���ɏ����o��
f = open(qk + '.txt', 'a')

url =  "https://api.twitter.com/1.1/search/tweets.json"

# �w��p�����[�^
params = {"q": qk,
          "count":"100",
          "result_type":"recent"}

# OAuth �� GET
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
req = twitter.get(url, params = params)

if req.status_code == 200:
    # ���X�|���X��JSON�`���Ȃ̂� parse ����
    timeline = json.loads(req.text)

    i = 1
    # �e�c�C�[�g�̖{����\��
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
    # �G���[�̏ꍇ
    print ("Error: %d" % req.status_code)

f.close()