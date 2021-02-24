
# write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure) that has
# words as the keys and the number of times each word was seen as the values.

from collections import Counter
import re



def count_words(text: str) -> dict:
    regex = r"[a-zA-z']+"
    text = text.lower()
    return dict(Counter(re.findall(regex, text)))


# Test
sentence = "oh what a day, what a lovely day!"
sentence2 = "oh my, oh lord, what trickery trick, trickery trick!"
sentence3 = "don't stop believing"
sentence4 = "gusta python ¿te"
print(count_words(sentence))
print(count_words(sentence2))
print(count_words(sentence3))
print(count_words(sentence4))