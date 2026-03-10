import faiss
import numpy as np

class VectorService:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add_vectors(self, vectors, docs):
        self.index.add(np.array(vectors))
        self.documents.extend(docs)

    def search(self, query_vector, k=3):

        distances, indices = self.index.search(query_vector, k)

        results = []

        for i in indices[0]:
            results.append(self.documents[i])

        return results