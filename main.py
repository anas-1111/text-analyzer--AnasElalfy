import re

sentence_count = 0


with open("sample_text.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.lower()
        sentence_count += len(re.findall(r'[.!?]', line))

print(sentence_count)
