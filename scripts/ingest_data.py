import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.services.embedding_service import get_embedding
from pinecone import Pinecone
from app.config import PINECONE_API_KEY, PINECONE_INDEX

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(PINECONE_INDEX)

documents = []

with open("../data/documents.txt") as f:
    for line in f:
        documents.append(line.strip())


vectors = []

for i, doc in enumerate(documents):

    embedding = get_embedding(doc)

    vectors.append({
        "id": str(i),
        "values": embedding,
        "metadata": {"text": doc}
    })

index.upsert(vectors)

print("Documents uploaded successfully")