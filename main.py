def analyze_text(path):
    import re
    import string
    from collections import Counter

    sentence_count = 0
    word_count = 0
    word_frequency = Counter()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.lower()
            sentence_count += len(re.findall(r'[.!?]', line))
            clean_line = line.translate(str.maketrans("", "", string.punctuation))
            words = clean_line.split()
            word_count += len(words)
            word_frequency.update(words)

    return word_count, sentence_count, word_frequency


word_c, sentence_c, word_frequency = analyze_text("sample_text.txt")

print("Words count: {}\nSentences count: {}\nTop 10 words: ".format(word_c, sentence_c))
for word, count in word_frequency.most_common(10):
    print("{}: {}".format(word, count))