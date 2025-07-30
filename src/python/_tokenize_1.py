
# michaelobrien 20250728 using as a guide "build a large language model from scratch - Sebastian Raschka"

import urllib.request
import re

from SimpleTokenizerV1 import SimpleTokenizerV1

# use a public dataset for initial testing
#url = ("https://raw.githubusercontent.com/rasbt/"
#       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
#       "the-verdict.txt")
#file_path = "data/the-verdict.txt"
#urllib.request.urlretrieve(url, file_path)

# load downloaded file
with open("src/python/data/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("chars", len(raw_text))
# tokenize on whitespace \s and periods/commans ,.
result = re.split(r'(\s)|([.,])', raw_text)
# truncate spaces (not recommended for code)
result = [token for token in result if token and not token.isspace()]
#print(result[:99]) # first 100 tokens

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
#print(preprocessed[:30])

# assign token ids
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

# create a vocabulary dictionary
vocab = {token:integer for integer,token in enumerate(all_words)}
#for i, item in enumerate(vocab.items()):
#    print(item)
#    if i >= 50:
#        break

tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know," 
       Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
decoded_text = tokenizer.decode(ids)
print(decoded_text)