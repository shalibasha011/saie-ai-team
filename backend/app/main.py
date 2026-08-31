from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .agents import AGENTS
from .orchestrator import orchestrator
from .planning import planning_engine
from .task_decomposition import task_decomposition_engine
from .autonomous_planner import autonomous_planner
from .decision_intelligence import decision_intelligence
from .feedback_engine import feedback_engine
from .recommendation_optimizer import recommendation_optimizer
from .outcome_tracking import outcome_tracker
from .evaluation import ai_evaluation
from .progress_tracking import progress_tracker
from .scenario_manager import scenario_manager
from .risk_simulation import risk_simulation_engine
from .execution_engine import agent_execution_engine
from .storage import storage


app = FastAPI(
    title="SAIE AI Team",
    version="0.1.0"
)


# =========================
# Request Models
# =========================

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


class RecommendationRequest(BaseModel):
    goal: str
    recommendations: list[str]
    feedback_scores: list[float]


class OutcomeRequest(BaseModel):
    goal: str
    task: str
    agent_id: str
    success: bool
    score: float


class ProgressRequest(BaseModel):
    goal: str
    task: str
    agent_id: str
    status: str = "pending"


class ProgressUpdateRequest(BaseModel):
    status: str


class ScenarioRequest(BaseModel):
    name: str
    goal: str
    assumptions: list[str]


class RiskSimulationRequest(BaseModel):
    scenario_name: str
    risks: list[str]


class ExecutionRequest(BaseModel):
    goal: str


# =========================
# Basic Endpoints
# =========================

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


# =========================
# Agent Endpoints
# =========================

@app.get("/agents")
def get_agents():
    return {
        "total_agents": len(AGENTS),
        "