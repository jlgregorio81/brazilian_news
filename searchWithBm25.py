from rank_bm25 import *
import pandas as pd, spacy


df = pd.read_csv('clean_dataset/esporte-dataset.csv', encoding='latin-1')

corpus = []
for index, row in df.iterrows():
    doc = row['text'].split(',')
    corpus.append(doc)

bm25 = BM25Okapi(corpus)

query = ['petrobras', 'corrupção', 'lula', 'delação', 'moro', 'odebrecht', 
         'propina', 'stf', 'pt', 'dilma']


#get the scores
scores = bm25.get_scores(query)

#define an id to all scores
row=2
scoreList = []
for score in scores:
    scoreList.append({'row' : row, 'score' : round(score, 4)})
    row+=1

#a function to define the key to sort
def scoreSort(e):
    return e['score']
#sort the scores 
scoreList.sort(key=scoreSort, reverse=True)

#put in a file
scoreFile = open('scores.csv', 'w+')
scoreFile.write("row,score\n")
for score in scoreList:
    if score['score'] == 0:
        break
    else:
        scoreFile.write(f"{score['row']},{score['score']}\n")

scoreFile.close()

