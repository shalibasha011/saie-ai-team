from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .agents import AGENTS
from .orchestrator import orchestrator
from .planning import planning_engine
from .task_decomposition import task_decomposition_engine
from .autonomous_planner import autonomous_planner
from .decision_intelligence import decision_intelligence
from .feedback_engine import feedback_engine


app = FastAPI(
    title="SAIE AI Team",
    version="0.1.0"
)


class TaskRequest(BaseModel):
    task: str
    agent_id: str


class PlanRequest(BaseModel):
    goal: str


class DecomposeRequest(BaseModel):
    goal: str


class StrategyRequest(BaseModel):
    goal: str


class DecisionRequest(BaseModel):
    goal: str
    options: list[str]


class FeedbackRequest(BaseModel):
    agent_id: str
    task: str
    score: float
    feedback: str


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


@app.post("/plans")
def create_plan(request: PlanRequest):
    return planning_engine.create_plan(goal=request.goal)


@app.post("/decompose")
def decompose_goal(request: DecomposeRequest):
    return task_decomposition_engine.decompose(goal=request.goal)


@app.post("/strategy")
def create_strategy(request: StrategyRequest):
    return autonomous_planner.create_execution_strategy(goal=request.goal)


@app.post("/decisions")
def analyze_decision(request: DecisionRequest):
    return decision_intelligence.analyze(
        goal=request.goal,
        options=request.options
    )


@app.post("/feedback")
def record_feedback(request: FeedbackRequest):
    return feedback_engine.record_feedback(
        agent_id=request.agent_id,
        task=request.task,
        score=request.score,
        feedback=request.feedback
    )


@app.get("/feedback")
def get_feedback():
    return {
        "total_feedback": len(feedback_engine.get_feedback()),
        "feedback": feedback_engine.get_feedback()
    }


@app.get("/feedback/{agent_id}/average")
def get_agent_average(agent_id: str):
    return feedback_engine.get_agent_average_score(agent_id)