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
from fastapi import FastAPI
from .agents import AGENTS

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


@app.get("/agents")
def get_agents():
    return {
        "total_agents": len(AGENTS),
        "agents": AGENTS
    }