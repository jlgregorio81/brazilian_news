import pandas as pd, nltk

#load the file
fileName =  'clean_dataset/poder-lavajato-dataset.csv'

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
    print(f"Processing word number: {i}\n")

#sort 
sortedBoW = sorted(bagOfWords.items(), key=lambda x: x[1], reverse=True)

#create a file with Bow
bowFile = open('bow.csv','w+')

i = 0;
bowFile.write("word,count\n")
for word in sortedBoW:
    i+=1
    bowFile.write(f"{word[0]},{word[1]}\n")
    print(f"Writing {i}")


bowFile.close()