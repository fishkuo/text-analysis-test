import pandas as pd
import re

# read file 
txt = pd.read_csv("test-text.csv")
# drop nan
txt = txt.dropna()
# 只保留中文字[\u4E00-\u9FFF]
txt = txt["0"].values.tolist()
clean_txt = []
for item in txt:
  cleaned = "".join(re.findall(r"[\u4E00-\u9FFF]",item))
  clean_txt.append(cleaned)
# 丟掉剩下空白的
clean_txt = [x for x in clean_txt if x]

print(len(clean_txt))
print(clean_txt[:5])
clean_txt = pd.DataFrame(clean_txt)
clean_txt.to_csv("clean-txt.csv")