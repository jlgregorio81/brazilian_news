import math, re, pandas as pd
from collections import Counter

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


# text1 = "Dilma é corrupta"
# text2 = "Lula é corrupto"


# vector1 = text_to_vector(text1)
# vector2 = text_to_vector(text2)

# cosine = get_cosine(vector1, vector2)

# print("Cosine:", cosine)

# ----------------------------------------------------------------------------------------------------

dataSetFile = pd.read_csv('clean_dataset/painel-do-leitor-dataset.csv', encoding='latin-1')
query = 'petrobras corrupção lula delação moro odebrecht propina stf pt dilma'

#vector 1
vector1 = text_to_vector(query)

cosineScores = []
i = 1
for index, row in dataSetFile.iterrows():
    print(f'Processing register {i}')
    text = row['text'].split(',')
    text = ' '.join(text)
    #print(f"Text: {text}")
    vector2 = text_to_vector(text)
    cosine = get_cosine(vector1, vector2)
    #print(f"Cosine: {cosine}")
    cosineScores.append({ 'id' : row['id'], 'score' : cosine})
    i+=1


#a function to define the key to sort
def scoreSort(e):
    return e['score']
#sort the scores 
cosineScores.sort(key=scoreSort, reverse=True)

#put in a file
i=0
scoreFile = open('cosine-scores.csv', 'w+')
scoreFile.write("id,score\n")
for score in cosineScores:
    if score['score'] == 0:
        break
    else:
        print(f'Writing register {i}')
        scoreFile.write(f"{score['id']},{score['score']}\n")
        i+=1

scoreFile.close()



