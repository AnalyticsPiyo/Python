# -*- coding: utf-8 -*-
"""
@author: hideyuki.takase
"""
import matplotlib.pyplot as plt
import numpy as np
import math

# f(x)を自分で書く
f = lambda x: (math.exp(-x**2/16)) / (math.sqrt(2*math.pi)*4)

# ベクトルxを [-5.0, ..., 5.0] の区間で作成
n = np.linspace(-10.0, 10.0, 100000)

# f(x)の結果を得る
p = []
for i in range(len(n)):
    p.append(f(n[i]))

# グラフに表示
plt.scatter(n, p,lw=1)
plt.xlim([-11,11])
plt.show()