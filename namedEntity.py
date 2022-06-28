import spacy, pandas as pd

#load the nlp model
nlp = spacy.load('pt_core_news_sm')

#load the dataset
dataset = pd.read_csv('clean_dataset/poder-lavajato-upper.csv', encoding='latin-1')


i=0
entitiesList = dict()

for index, doc in dataset.iterrows():
    #print("------->")
    tokenized = doc['text'].split(",")
    theText = ' '.join(tokenized)
    theDoc = nlp(theText)
    entities = [ (entity, entity.label_) for entity in theDoc.ents ]
    for entity in entities:
        entityName = str(entity[0])      
        if entityName in entitiesList:
            entitiesList[entityName] += 1
        else:
            entitiesList[entityName] = 1
    # print(tags)
    # print("------")
    # i+=1
    # if i == 5:
    #     break

sortedEntities = sorted(entitiesList.items(), key=lambda x: x[1], reverse=True)

i = 0
csvFile = open('named_entities.csv', 'w+')
csvFile.write("entity,count\n")
for key, value in sortedEntities:
    csvFile.write(f"{key},{value}\n")
    i+=1
    print(f"Writing Entity: {i}")

csvFile.close()




#gramatical classes
# for index, doc in dataset.iterrows():
#     print("-------")
#     theDoc = nlp(doc['text'])
#     tags = [ (token.orth_, token.pos_) for token in theDoc ]
#     for tag in tags:
#         if(tag[1] == 'PROPN'):
#             print(f"tag: {tag}\n")