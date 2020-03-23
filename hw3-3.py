import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import pandas as pd
from scipy import stats
#
# plt.figure(figsize=(8,4), dpi = 100)
# x=[1,2,3,4,5,6,7,8,9,10]
# y=[11,12,13,14,15,16,17,18,19,20]
#
#
# dağılım = np.random.normal(x,y)
# plt.hist(dağılım)
# plt.show()
#
# res = stats.probplot(dağılım, plot=plt)
# plt.show()

##ben bu graphları nasıl yorumlayacağımı hiç anlamadım hocam.
##doğru mu ondan da emin değilim. Bu istatistiksel dağılımların dersini bile
##aldım ama ona rağmen anlamadım.
#1/2/2020
#3/23/2020


df = pd.read_csv("AAPL.csv")
T2019 = df[0:196].mean()["Open"]
T2020 = df[196:253].mean()["Open"]
hisse_senedi_getirisi = (T2020-T2019) / T2019
print(hisse_senedi_getirisi)
