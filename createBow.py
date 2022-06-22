from ast import operator
import pandas as pd, nltk

#load the file
fileName =  './poder-lavajato-dataset.csv'

#load the file as csv
df = pd.read_csv(fileName, encoding='latin-1')

i=0
bagOfWords = dict()
for index, row in df.iterrows():
    words = row['text'].split(',')
    for word in words:
        if word in bagOfWords:
            bagOfWords[word] += 1
        else:
            bagOfWords[word] = 1
    i+=1
    if i == 20:
        break

#sort 
sortedBoW = sorted(bagOfWords.items(), key=lambda x: x[1], reverse=True)

i = 0;
for word in sortedBoW:
    i+=1
    print(f"{i} - {word[0]} - {word[1]}")
    if i >= 100:
        break



