from fastapi import APIRouter
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService

router = APIRouter()

embedding_service = EmbeddingService()

documents = [
    "Python is a high level programming language",
    "Machine learning enables computers to learn from data",
    "Vector databases store embeddings for similarity search",
    "FastAPI is used to build APIs in Python",
    "Jaiganesh knows python"
]

embeddings = embedding_service.embed(documents)

dimension = embeddings.shape[1]

vector_db = VectorService(dimension)
vector_db.add_vectors(embeddings, documents)


@router.get("/search")

def search(query: str):

    query_vector = embedding_service.embed([query])

    results = vector_db.search(query_vector)

    return {"results": results}