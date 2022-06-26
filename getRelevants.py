

import pandas as pd


scores = pd.read_csv('scores-esporte.csv')

df = pd.read_csv('clean_dataset/esporte-dataset.csv', encoding='latin-1')

#print(f"{mercadoDataSet.iloc[18710]['id']} - {mercadoDataSet.iloc[18710]['title']} ")

relevants = 0
irrelevants = 0
precision = 0
p10 = 0
p20 = 0
p50 = 0
p100 = 0
p200  = 0
map = 0 

for index, score in scores.iterrows():
    #print(f"{int(score['row'])} - {score['score']}")
    id = int(score['row'])
    #a document is relevant if the term 'lava,jato' is in the text
    if('lava,jato' in df.iloc[id-2]['text'] ):
        precision = precision + score['score']
        relevants+=1  
        print(f"-----> Document: {df.iloc[id-2]['id']}\n")
    else:
        irrelevants+=1
    #print(f"Index: {index}")

    if index == 9:
        p10 = round(relevants/10,2)
        # print(f'Relevants at P@10: {relevants}')
        # print(f"Index: {index}")
    
    if index == 19:
        p20 = round(relevants/20, 2)
        #print(f'Relevants at P@20: {relevants}')

    if index  == 49:
        p50 = round(relevants/50, 2)
        #print(f'Relevants at P@50: {relevants}')

    if index == 99:
        p100 = round(relevants/100, 2)
        #print(f'Relevants at P@100: {relevants}')
    
    if index == 199:
        p200 = round(relevants/200, 2)
        #print(f'Relevants at P@100: {relevants}')
    
    # if index == 10:
    #     break
    
#map = division the sum of precision by total of documents in dataset
map = round(precision/len(df), 2)

print(f"Relevants: {relevants}")
print(f"Irrelevants: {irrelevants}")
print(f"Total of documents: {relevants + irrelevants}")
print(f"Dataset Size: {len(df)}")
print("------------------")
print("Precision at (P@N)")
print(f"P@10: {p10}")
print(f"P@20: {p20}")
print(f"P@50: {p50}")
print(f"P@100: {p100}")
print(f"P@200: {p200}")
print(f"MAP: {map}")

#print(f"Precision: {precision}")


