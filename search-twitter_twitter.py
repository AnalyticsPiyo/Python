#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# @author: hideyuki.takase

import twitter
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

CONSUMER_KEY = "****"
CONSUMER_SECRET = "****"
ACCESS_TOKEN = '****'
ACCESS_TOKEN_SECRET = '****'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token_key=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

# 検索
search= u"****"
tweets = api.GetSearch(term=search, count=100,result_type='recent')
test = open("test.txt", "a")

for i in tweets:
    test.write(i.created_at.encode("utf-8"))
test.close()