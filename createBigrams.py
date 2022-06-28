from nbformat import write
from nltk import bigrams, trigrams
import pandas as pd

df = pd.read_csv('clean_dataset\poder-lavajato-dataset.csv', encoding='latin-1')
dfSize = len(df)

corpus = []
for index, row in df.iterrows():
    doc = row['text'].split(',')
    corpus.append(doc)

i = 1
bagOfBigrams = dict()
for document in corpus:
    print(f"Processing file {i} of {dfSize}")
    bigramsList = list(bigrams(document))
    #bigramsFile.write(str(bigramsList) + "\n")
    for bigram in bigramsList:
        key = ','.join(bigram)
        verifyBigram = [ word for word in bigram]
        verifyBigram = ','.join(verifyBigram)
        #print(f'Bigram: {bigram} - {type(bigram)}')
        if verifyBigram in bagOfBigrams:
            bagOfBigrams[key] +=1
        else:
            bagOfBigrams[key] = 1


#sort 
sortedBoB = sorted(bagOfBigrams.items(), key=lambda x: x[1], reverse=True)

#create a file with Bow
bobFile = open('bob.csv','w+')

i = 0;
bobFile.write("bigram,count\n")
for bigram in sortedBoB:
    i+=1
    bobFile.write(f"{bigram[0]},{bigram[1]}\n")
    print(f"Writing {i}")


bobFile.close()

