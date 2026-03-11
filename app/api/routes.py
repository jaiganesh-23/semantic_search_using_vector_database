from fastapi import APIRouter
from app.services.embedding_service import get_embedding
from app.services.vector_service import query_vectors

router = APIRouter()


@router.get("/search")
def search(query: str):

    embedding = get_embedding(query)

    results = query_vectors(embedding)

    return {
        "query": query,
        "results": results
    }