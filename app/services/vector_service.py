from pinecone import Pinecone
from app.config import PINECONE_API_KEY, PINECONE_INDEX

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(PINECONE_INDEX)


def query_vectors(vector):

    results = index.query(
        vector=vector,
        top_k=3,
        include_metadata=True
    )

    output = []

    for match in results["matches"]:
        output.append(match["metadata"]["text"])

    return output