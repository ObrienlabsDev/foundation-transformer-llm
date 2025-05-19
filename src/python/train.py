
file_path = "attention_is_all_you_need.txt"
with open(file_path, "r", encoding="utf-8") as f:
    raw_text=f.read()
print("Chars: ", len(raw_text))
print(raw_text[:99])

