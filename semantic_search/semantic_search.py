from posixpath import split
from sentence_transformers import SentenceTransformer, util
import pandas as pd
from torch import embedding

model = SentenceTransformer('all-MiniLM-L6-v2')

# Two lists of sentences
#sentences1 = ['petrobras operacao lava jato stf delacao']
#sentences2 = ['segio moro aciona stf operação lava jato delação lula dilma ']


dataSetFile = pd.read_csv('../clean_dataset/painel-do-leitor-dataset.csv', encoding='latin-1')
query = ['petrobras corrupção lula delação moro odebrecht propina stf pt dilma']

qryEmbedding = model.encode(query, convert_to_tensor=True)

corpus = []
cosineScores = []
i = 1
for index, row in dataSetFile.iterrows():
    print(f'Processing register {i}')
    text = row['text'].split(',')
    text = [' '.join(text)]
    textEmbedding = model.encode(text, convert_to_tensor=True)
    cosineScore = util.cos_sim(qryEmbedding, textEmbedding)
    #print(f'Cosine Score: {round(cosineScore[0][0],4)} ')
    #print(f'Cosine Score: {type(cosineScore)} ')
    id = int(row['id'])
    cosineScores.append({'id': id, 'score': cosineScore[0][0]})
    i+=1

def scoreSort(e):
    return e['score']
#sort the scores 
cosineScores.sort(key=scoreSort, reverse=True)

#put in a file
i = 1
scoreFile = open('cosin_scores.csv', 'w+')
scoreFile.write("id,score\n")
for score in cosineScores:
    if score['score'] == 0:
        break
    else:
        scoreFile.write(f"{score['id']},{score['score']}\n")
    print(f'Writing register {i}')
scoreFile.close()



#Compute embedding for both lists
# embeddings1 = model.encode(sentences1, convert_to_tensor=True)
# embeddings2 = model.encode(sentences2, convert_to_tensor=True)

#Compute cosine-similarits
# cosine_scores = util.cos_sim(embeddings1, embeddings2)

#Output the pairs with their score
# for i in range(len(sentences1)):
    # print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))