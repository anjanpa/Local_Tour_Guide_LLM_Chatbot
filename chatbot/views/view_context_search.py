import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json

def search_context(query,k=1):
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
  model = SentenceTransformer('all-MiniLM-L6-v2')
  query = query
  query_embedding = model.encode(query)
  distances, indices = index.search(np.array([query_embedding]), k)

  print(distances)
  threshold=0.9
  if distances[0][0] > threshold:
        return ["Sorry, I don't have enough context to answer that question."]

  # Retrieve the matching documents from the corpus
  matching_documents = [texts[i] for i in indices[0]]

  return matching_documents