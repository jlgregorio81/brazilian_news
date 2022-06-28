from nbformat import write
from nltk import trigrams
import pandas as pd

df = pd.read_csv('clean_dataset\poder-lavajato-dataset.csv', encoding='latin-1')
dfSize = len(df)

corpus = []
for index, row in df.iterrows():
    doc = row['text'].split(',')
    corpus.append(doc)

i = 1
bagOfTrigrams = dict()
for document in corpus:
    print(f"Processing file {i} of {dfSize}")
    trigramList = list(trigrams(document))
    #bigramsFile.write(str(bigramsList) + "\n")
    for trigram in trigramList:
        key = ','.join(trigram)
        verifyTrigram = [ word for word in trigram]
        verifyTrigram = ','.join(verifyTrigram)
        #print(f'Bigram: {bigram} - {type(bigram)}')
        if verifyTrigram in bagOfTrigrams:
            bagOfTrigrams[key] +=1
        else:
            bagOfTrigrams[key] = 1


#sort 
sortedBot = sorted(bagOfTrigrams.items(), key=lambda x: x[1], reverse=True)

#create a file with Bow
botFile = open('bot.csv','w+')

i = 0;
botFile.write("trigram,count\n")
for trigram in sortedBot:
    i+=1
    botFile.write(f"{trigram[0]},{trigram[1]}\n")
    print(f"Writing {i}")


botFile.close()

