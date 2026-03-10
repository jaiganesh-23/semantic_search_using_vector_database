from fastapi import FastAPI
from app.api.routes import router
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Vector Search API",
    description="Semantic Search using Vector Database",
)

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Vector Search API</title>
        </head>
        <body>
            <h1>🚀 Vector Search Engine</h1>
            <p>Your FastAPI service is running successfully.</p>
            <p>Use the API docs:</p>
            <a href="/docs">Open Swagger Docs</a>
        </body>
    </html>
    """