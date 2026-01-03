import re
import string

sentence_count = 0


with open("sample_text.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.lower()
        sentence_count += len(re.findall(r'[.!?]', line))
        clean_line = line.translate(str.maketrans("", "", string.punctuation))
        print(clean_line)

print(sentence_count)
