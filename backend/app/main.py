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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .agents import AGENTS
from .orchestrator import orchestrator

app = FastAPI(
    title="SAIE AI Team",
    version="0.1.0"
)


class TaskRequest(BaseModel):
    task: str
    agent_id: str


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


@app.post("/tasks")
def assign_task(request: TaskRequest):
    result = orchestrator.assign_task(
        task=request.task,
        agent_id=request.agent_id
    )

    if not result["success"]:
        raise HTTPException(
            status_code=404,
            detail=result["error"]
        )

    return result


@app.get("/messages")
def get_messages():
    return {
        "total_messages": len(orchestrator.get_messages()),
        "messages": orchestrator.get_messages()
    }