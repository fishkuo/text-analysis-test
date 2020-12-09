import jiagu
import pandas as pd
from opencc import OpenCC

# 用來繁轉簡，現在是在要算情緒分數時一筆一筆呼叫轉簡體，效能一定糟透，理論上也許要另外存一個欄位是簡體？
cc = OpenCC('t2s')
txt = pd.read_csv("clean-txt-tokenized.csv")
txt["sentiment"] = 0
for i in range(len(txt)):
  txt["sentiment"][i] = jiagu.sentiment(cc.convert(txt["0"][i]))

txt.to_csv("clean-txt-tokenized-sentiment.csv")