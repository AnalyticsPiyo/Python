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

unique_words = set()
segments_count = {}
segments_count = defaultdict(lambda: 0)
result_words = []
tagger = MeCab.Tagger("-Ochasen")
result_word_category = {}
result_word_category = defaultdict(lambda: 0)

doc1 = "スポーツはサッカーと野球が好きなり"
doc2 = "スポーツは嫌いだけどバスケなら許す"
doc3 = "スポーツはサッカーがいいね！特にロベカルが最高だね"

doc_all = [["doc1", doc1], ["doc2", doc2], ["doc3", doc3]]

def morphological_Analysis(result_sql):
    for row in result_sql:
        unique_words = set()
        node = tagger.parseToNode(row[1])
        words_count = {}
        words_count = defaultdict(lambda: 0)

        while node:

            if node.feature.split(",")[0] == "名詞":
                words_count[node.surface] = words_count[node.surface] + 1
                # ある単語 tt が出現する文書の数 計算用
                unique_words.add(node.surface)
            node = node.next
        result_words.append([row[0],words_count])
        for i in unique_words:
            result_word_category[i] = result_word_category[i] + 1
    return result_words ,result_word_category


# 各文書の単語の出現数
result = morphological_Analysis(doc_all)
# 各文書の単語の出現数
tf = result[0]
# ある単語 tt が出現する文書の数
df = result[1]
# 全文章数 N
N = int(len(doc_all))

# ある単語 tt のIDF値
idf = {}
for k, v in  df.items():
    idf[k] = math.log((N/v)) + 1

tf_idf = []
tf_idf_dict = {}
# TF-IDFを計算
for x in tf:
    tf_idf_dict = {}
    for kk, vv in x[1].items():
        tf_idf_dict[kk] = vv * idf[kk] 
    tf_idf.append([x[0], tf_idf_dict])

for res in tf_idf:
    print(res[0])
    for kkk,vvv in res[1].items():
        print(kkk, vvv)
