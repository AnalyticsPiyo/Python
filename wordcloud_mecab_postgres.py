# -*- coding: utf-8 -*-
"""
@author: hideyuki.takase
"""

import psycopg2
import re
from collections import defaultdict
import math
import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud

words = set()
words_count = {}
segments_count = {}
words_count = defaultdict(lambda: 0)
segments_count = defaultdict(lambda: 0)

### MeCab設定 ###
tagger = MeCab.Tagger("-Ochasen")
words = []
def morphological_Analysis(result_sql):
    for row in result_sql:
        node = tagger.parseToNode(row[3])

        while node:
            if node.feature.split(",")[0] == "名詞":
                words.append(node.surface)
            node = node.next
    return words

### データベースの設定 ###
connector = psycopg2.connect(
    host='****', 
    database='****', 
    user='****', 
    password='****',
)
cursor = connector.cursor()
# sql文作成
sql = """
select
  ****
from
  ****
"""
cursor.execute(sql)
result = cursor.fetchall()

seg = morphological_Analysis(result)

### 終了処理 ###
cursor.close()
connector.close()

### 描画###
# Stop Wordの設定もできる
stop_words = ["/"]
# フォントのパス指定
fpath = "C:/Windows/Fonts/meiryo.ttc"

wordcloud = WordCloud(background_color="white", font_path=fpath, width=900, height=500, stopwords=stop_words).generate(" ".join(seg))
plt.figure(figsize=(15,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
