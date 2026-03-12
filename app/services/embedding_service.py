from groq import Groq
from google import genai
from google.genai import types
from app.config import GOOGLE_API_KEY

client = genai.Client()



def get_embedding(text: str):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=768, task_type="SEMANTIC_SIMILARITY"),
    )
    return response.embeddings[0].values
