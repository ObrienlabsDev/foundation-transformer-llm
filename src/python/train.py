import os
import re


# we will use the "Attention is all you need" paper as our training data for now
file_path = "attention_is_all_you_need.txt"
data_directory_path = "data"


with open(file_path, "r", encoding="utf-8") as f: # auto close file
    raw_text=f.read()
print("Chars: ", len(raw_text))
preprocessed_text = re.split(r"\s+", raw_text) # split the text into words
#preprocessed_text = re.split(raw_text, r"\s+") # this compiles but is wrong
print(preprocessed_text[:99]) # print out the first 100 characters

# split the file into 1k parts using a generator
def get_text_generator(file_path, chunk_size=1024):
    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            text = f.read(chunk_size)
            if not text:
                break
            yield text
# Create a generator to read the text in chunks of 1024 characters
text_generator = get_text_generator(file_path, chunk_size=1024)

# we need to split the training data in training, test and validation parts - usually 10% for test and 10% for validation - the rest for training
# create/use a data directory
os.makedirs(data_directory_path, exist_ok=True)

# Create a file to store the training data
with open(os.path.join(data_directory_path, "train.txt"), "w", encoding="utf-8") as f:
    for i in range(10):
        text = next(text_generator)
        f.write(text)
# Create a file to store the validation data
with open(os.path.join(data_directory_path, "val.txt"), "w", encoding="utf-8") as f:
    for i in range(10):
        text = next(text_generator)
        f.write(text)
# Create a file to store the test data
with open(os.path.join(data_directory_path, "test.txt"), "w", encoding="utf-8") as f:
    for i in range(10):
        text = next(text_generator)
        f.write(text)
