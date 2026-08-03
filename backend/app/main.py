from fastapi import FastAPI

app = FastAPI(
    title="Medora Chatbot API",
    description="Backend API for medicine guidance, RAG and clinical rules.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    """Return basic information about the API."""
    return {
        "name": "Medora Chatbot API",
        "status": "running",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """Confirm that the backend is running."""
    return {
        "status": "healthy",
    }