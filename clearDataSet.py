import pandas as pd, nltk, string, spacy


#base path of the data set
basePath = 'dataset'
fileName =  'articles.csv'
dataSetFile = f"{basePath}/{fileName}"

#load the data set file
#dataSet = open(dataSetFile, "r", encoding='utf-8')
#csvFile = csv.reader(dataSet)
df = pd.read_csv(dataSetFile, encoding='utf-8')

#define the stopwords
stopWords = nltk.corpus.stopwords.words('portuguese')
#define the special chars
specialChars =  string.punctuation
#define the lemmatizer
nlp = spacy.load('pt_core_news_sm')

#doc = nlp("Ontem eu fiz amizade com uma pessoa que é manipuladora e gosta de computadores. Ele curte conteúdo noticiários")

# for word in doc:
#     print(word.lemma_)

# print(stopWords)
# print('------')
#print(type(specialChars))
# print('------')

newDataSet = []

#perform the cleaning...
i = -1
for index, row in df.iterrows():
    i+=1
    print(f"Processing register num:{i} \n")
    if 'poder' in row['category'].lower() and 'lava-jato' in row['link']:
        try:
            tokenizedText = nltk.tokenize.word_tokenize(row['title'])
            cleanTitle = [ word for word in tokenizedText if not word.lower() in stopWords and word.isalnum() and word not in specialChars and len(word) > 1 ]
            #lemmatizer
            cleanTitle = nlp(' '.join(cleanTitle))
            cleanTitle = [ word.lemma_ for word in cleanTitle ]
            tokenizedText = nltk.tokenize.word_tokenize(row['text'])
            cleanText = [ word for word in tokenizedText if not word.lower() in stopWords and word.isalnum() and word not in specialChars and len(word) > 1 ]
            #lemmatizer
            cleanText = nlp(' '.join(cleanText))
            cleanText = [ word.lemma_ for word in cleanText ]
            #tokenize title and text - the rest is string
            newDataSet.append([cleanTitle, cleanText, row['date'], row['category'], row['link']])
        except Exception as e:
            print(f"Title: {row['title']}")
            print(f"Value of: {i}")
            continue

newFile = open("clean_data_set.csv", "w+")

line = 2
newFile.write("id,title,date,category,url,text\n")
for row in newDataSet:
    title = '"' + ','.join(row[0]) + '"'
    date = '"' + row[2] + '"'
    category = '"' + row[3] + '"'
    url = '"' + row[4] + '"'
    text = '"' + ','.join(row[1]) + '"'
    try:
        newFile.write(f"{line},{title},{date},{category},{url},{text} \n")
        line+=1
    except Exception as e:
        print(f"Error: {e}")
        print(f"{title}")
    print(f"Writing register num: {line} \n")

    
newFile.close()