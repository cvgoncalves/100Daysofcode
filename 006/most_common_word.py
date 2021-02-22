import os
import urllib.request
import re
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

def get_harry_most_common_word():
    word_list = []
    stop_word = []

    with open(stopwords_file, 'r', encoding='utf-8') as sw:
        for l in sw:
            l = l.split()
            stop_word.append(*l)

    # print(stop_word)

    with open(harry_text, 'r', encoding='utf-8') as fh:
        for line in fh:
            line = line.lower().replace("'", "")
            line = re.sub(r'\W+', ' ', line)
            word = re.findall("[a-zA-Z\-\.'/]+", line)
            for w in word:
                if w not in stop_word:
                    word_list.append(w)

    # print(word_list)

    most_common = (Counter(word_list).most_common(1))[0]

    return most_common

print(type(get_harry_most_common_word()) == tuple)
print(get_harry_most_common_word()[0] == 'dursley')
print(get_harry_most_common_word()[1] == 45)