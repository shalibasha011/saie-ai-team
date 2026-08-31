from fastapi import FastAPI

from .agents import AGENTS
from .orchestrator import orchestrator
from .planning import planning_engine


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
        "agents": AGENTS
    }


@app.get("/plan")
def get_plan():
    return {
        "planning_engine": str(planning_engine)
    }


@app.get("/team")
def get_team():
    return {
        "message": "SAIE AI Team is ready",
        "agents": AGENTS,
        "orchestrator": str(orchestrator),
        "planning_engine": str(planning_engine)
    }