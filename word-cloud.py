from wordcloud import WordCloud
import pandas as pd
import ast
from matplotlib import pyplot as plt
txt = pd.read_csv("clean-txt-tokenized.csv")

# 製作成空格分開的大字串
txt_str = ""
for i in range(len(txt)):
  txt["token_text"][i] = ast.literal_eval(txt["token_text"][i])
  txt_str += ' '.join(txt["token_text"][i])

# print(txt_str)
cloud = WordCloud(font_path="TaipeiSansTCBeta-Regular.ttf").generate(txt_str)
cloud.to_file('wordcloud.png')


# print(cloud)
