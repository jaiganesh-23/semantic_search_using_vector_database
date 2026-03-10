from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService

embedding_service = EmbeddingService()

documents = []

with open("data/documents.txt") as f:
    for line in f:
        documents.append(line.strip())

embeddings = embedding_service.embed(documents)

dimension = embeddings.shape[1]

vector_db = VectorService(dimension)

vector_db.add_vectors(embeddings, documents)

print("Data indexed successfully")