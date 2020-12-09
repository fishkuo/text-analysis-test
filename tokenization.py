import pandas as pd
from ckiptagger import data_utils, WS, POS

# read file 
clean_txt = pd.read_csv("clean-txt.csv")

# print(clean_txt.columns)
# print(clean_txt)

data_utils.download_data_gdown("./")  # 執行一次就好
ws = WS("./data")
clean_txt['token_text'] = ws(clean_txt["0"])

print(clean_txt[:5])

#save
clean_txt.to_csv("clean-txt-tokenized.csv")