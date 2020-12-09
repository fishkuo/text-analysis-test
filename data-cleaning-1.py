import pandas as pd
# plt.rcParams['font.family'] = 'Arial Unicode MS'
# plt.rcParams['font.size'] = 12

# for 未來需要set column name使用
post_content = pd.read_csv("post_content.csv", names = ["post_id","post_content","post_title", "created_at", "updated_at", "comment_count", "like_count", "gender"])
post_comment = pd.read_csv("post_comment.csv",names = ["comment_id", "post_id", "created_at", "updated_at","floor", "comment_content","like_count", "gender"])

# for測試的，只有文字欄位的小dataframe(正式不會這樣做)
test_text = pd.concat([post_comment["comment_content"],post_content["post_content"]], axis=0)

test_text.to_csv("test-text.csv")





  

