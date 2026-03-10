from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Vector Search API",
    description="Semantic Search using Vector Database",
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Vector Search API running"}