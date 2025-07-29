
# michaelobrien 20250728 using as a guide "build a large language model from scratch - Sebastian Raschka"

import urllib.request
import re

# use a public dataset for initial testing
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "data/the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

# load downloaded file
with open("data/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("chars", len(raw_text))
# tokenize on whitespace \s and periods/commans ,.
result = re.split(r'(\s)|([.,])', raw_text)
# truncate spaces (not recommended for code)
#result = [token for token in result if token and not token.isspace()]
print(result[:99]) # first 100 tokens

