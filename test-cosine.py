import math, re, pandas as pd
from collections import Counter
from strsimpy.cosine import Cosine

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


text1 = 'josé roela da silva'
text2 = 'josé roela da silva sauro'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

print(cosine)

# vector1 = ['josé', 'roela', 'da', 'silva']
# vector2 = ['josé', 'roela', 'da', 'silva', 'sauro']
# cosine = 1 - spatial.distance.cosine(vector1, vector2)

# print("Cosine:", cosine)
print("------>")

cosine = Cosine(2)
s0 = 'josé roela da silva'
s1 = 'josé roela da silva sauro'
p0 = cosine.get_profile(s0)
p1 = cosine.get_profile(s1)
print(cosine.similarity_profiles(p0, p1))


