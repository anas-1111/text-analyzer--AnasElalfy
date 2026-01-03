import re
import string
from collections import Counter

sentence_count = 0
word_count = 0
word_frequency = Counter()

with open("sample_text.txt", "r", encoding="utf-8") as file:
    for line in file:

        line = line.lower()

        sentence_count += len(re.findall(r'[.!?]', line))

        clean_line = line.translate(str.maketrans("", "", string.punctuation))
        
        word = clean_line.split()
        word_count += len(word)
        word_frequency.update(word)

