from groq import Groq
from transformers import AutoModel

embedding_model = AutoModel.from_pretrained(
    'jinaai/jina-embeddings-v2-base-en',
    trust_remote_code=True
)


def get_embedding(text: str):

    response = embedding_model.encode(text).tolist()

    return response