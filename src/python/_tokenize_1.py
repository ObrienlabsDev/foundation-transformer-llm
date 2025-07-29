
# michaelobrien 20250728 using as a guide "build a large language model from scratch - Sebastian Raschka"

import urllib.request

# use a public dataset for initial testing
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "data/the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

