from fastapi import FastAPI

app = FastAPI(
    title="SAIE AI Team",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to SAIE AI Team",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }