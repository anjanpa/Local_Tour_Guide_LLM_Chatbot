import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json

def search_context(query,k=2):
  '''
  query=user's query
  k=number of matches to  retrieve
  '''
  import os
  current_dir=os.path.realpath(os.path.dirname(__file__))
  json_path =os.path.join(current_dir,'project_uncleaned_data.json')
  with open(json_path, 'r') as f:
    cleaned_documents=json.load(f)
  texts = [doc['title'] + ": " + doc['description'] for doc in cleaned_documents]
  ## read vector db embedddings
  index = faiss.read_index(os.path.join(current_dir,'project_index.idx'))

  ## perform query
  model = SentenceTransformer('bert-base-nli-mean-tokens')
  query = query
  query_embedding = model.encode(query)
  distances, indices = index.search(np.array([query_embedding]), k)

  print(distances)
  threshold=1
  # if distances[0][0] > threshold:
  #       return ["Sorry, I don't have enough context to answer that question."]

  # Retrieve the matching documents from the corpus
  matching_documents = [texts[i] for i in indices[0]]
  print(matching_documents)

  return matching_documents


def search_in_vectordb_cosine(query, k=1):
    import os
    current_dir=os.path.realpath(os.path.dirname(__file__))
    json_path =os.path.join(current_dir,'project_uncleaned_data.json')

    with open(json_path, 'r') as f:
      cleaned_documents=json.load(f)
    texts = [doc['title'] + ": " + doc['description'] for doc in cleaned_documents]

    ## read vector db embedddings
    index = faiss.read_index(os.path.join(current_dir,'project_index_cosine.idx'))

    ## perform query
    model = SentenceTransformer('bert-base-nli-mean-tokens')

    # Normalize the query embedding
    query_embedding = model.encode([query])[0]
    query_embedding = query_embedding / np.linalg.norm(query_embedding)

    # Search the index for the k nearest neighbors
    distances, indices = index.search(np.array([query_embedding]), k)

    print(distances,indices)
    matching_documents = [texts[i] for i in indices[0]]
    print(matching_documents)
    return matching_documents