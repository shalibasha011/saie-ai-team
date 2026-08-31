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


@app.post("/recommendations/optimize")
def optimize_recommendations(request: RecommendationRequest):
    return recommendation_optimizer.optimize(
        goal=request.goal,
        recommendations=request.recommendations,
        feedback_scores=request.feedback_scores
    )


@app.post("/outcomes")
def record_outcome(request: OutcomeRequest):
    return outcome_tracker.record_outcome(
        goal=request.goal,
        task=request.task,
        agent_id=request.agent_id,
        success=request.success,
        score=request.score
    )


@app.get("/outcomes")
def get_outcomes():
    return {
        "total_outcomes": len(outcome_tracker.get_outcomes()),
        "outcomes": outcome_tracker.get_outcomes()
    }


@app.get("/outcomes/summary")
def get_outcome_summary():
    return outcome_tracker.get_summary()


@app.get("/evaluation/{agent_id}")
def evaluate_agent(agent_id: str):
    return ai_evaluation.evaluate(
        agent_id=agent_id,
        outcomes=outcome_tracker.get_outcomes()
    )


@app.post("/progress")
def add_progress(request: ProgressRequest):
    return progress_tracker.add_item(
        goal=request.goal,
        task=request.task,
        agent_id=request.agent_id,
        status=request.status
    )


@app.put("/progress/{item_id}")
def update_progress(
    item_id: int,
    request: ProgressUpdateRequest
):
    return progress_tracker.update_status(
        item_id=item_id,
        status=request.status
    )


@app.get("/progress")
def get_progress():
    return {
        "items": progress_tracker.get_items(),
        "summary": progress_tracker.get_summary()
    }


@app.post("/scenarios")
def create_scenario(request: ScenarioRequest):
    return scenario_manager.create_scenario(
        name=request.name,
        goal=request.goal,
        assumptions=request.assumptions
    )


@app.get("/scenarios")
def get_scenarios():
    return {
        "total_scenarios": len(scenario_manager.get_scenarios()),
        "scenarios": scenario_manager.get_scenarios()
    }


@app.get("/scenarios/{scenario_id}")
def get_scenario(scenario_id: int):
    scenario = scenario_manager.get_scenario(scenario_id)

    if scenario is None:
        raise HTTPException(
            status_code=404,
            detail="Scenario not found"
        )

    return scenario


@app.get("/system/status")
def system_status():
    return {
        "system": "SAIE AI Team",
        "status": "operational",
        "total_agents": len(AGENTS),
        "total_messages": len(orchestrator.get_messages()),
        "total_scenarios": len(scenario_manager.get_scenarios()),
        "progress": progress_tracker.get_summary(),
        "outcomes": outcome_tracker.get_summary()
    }