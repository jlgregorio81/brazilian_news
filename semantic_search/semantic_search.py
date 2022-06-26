from sentence_transformers import SentenceTransformer, util
import torch, pandas as pd

embedder = SentenceTransformer('all-MiniLM-L6-v2')


#read the file 
df = pd.read_csv('../clean_dataset/painel-do-leitor-dataset.csv', encoding='latin-1')

corpus = []
for index, row in df.iterrows():
    doc = row['text'].split(',')
    corpus.append(doc)


corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

# Query sentences:
queries = ['petrobras', 'corrupção', 'lula', 'delação', 'moro', 'odebrecht', 
         'propina', 'stf', 'pt', 'dilma']


# Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
top_k = min(10, len(corpus))
for query in queries:
    query_embedding = embedder.encode(query, convert_to_tensor=True)

    # We use cosine-similarity and torch.topk to find the highest 5 scores
    cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
    top_results = torch.topk(cos_scores, k=top_k)

    print("\n\n======================\n\n")
    print("Query:", query)
    print("\nTop 5 most similar sentences in corpus:")

    for score, idx in zip(top_results[0], top_results[1]):
        print(corpus[idx], "(Score: {:.4f})".format(score))