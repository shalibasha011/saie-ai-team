from typing import Dict

from .planning import planning_engine
from .task_decomposition import task_decomposition_engine
from .autonomous_planner import autonomous_planner


class AgentExecutionEngine:

    def execute(self, goal: str) -> Dict:
        """
        Runs the main SAIE workflow:
        1. Create a plan
        2. Break the goal into tasks
        3. Create an execution strategy
        """

        plan = planning_engine.create_plan(
            goal=goal
        )

        tasks = task_decomposition_engine.decompose(
            goal=goal
        )

        strategy = autonomous_planner.create_execution_strategy(
            goal=goal
        )

        return {
            "goal": goal,
            "status": "completed",
            "workflow": {
                "plan": plan,
                "task_decomposition": tasks,
                "execution_strategy": strategy
            }
        }


agent_execution_engine = AgentExecutionEngine()