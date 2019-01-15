# -*- coding: utf-8 -*-
"""
@author: hideyuki.takase
"""
import matplotlib.pyplot as plt
import numpy as np
import math

# f(x)を自分で書く
f = lambda x: (math.exp(-x**2/2)) / math.sqrt(2*math.pi)

# ベクトルxを [-5.0, ..., 5.0] の区間で作成
n = np.linspace(-3.0, 3.0, 100000)

# f(x)の結果を得る
p = []
for i in range(len(n)):
    p.append(f(n[i]))

# グラフに表示
plt.scatter(n, p,lw=0.0001)
plt.show()