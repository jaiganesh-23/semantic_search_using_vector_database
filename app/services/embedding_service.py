from .load_model import get_model
class EmbeddingService:

    def __init__(self):
        self.model = get_model()

    def embed(self, texts):
        return self.model.encode(texts)