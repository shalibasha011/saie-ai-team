from .agents import AGENTS
from .collaboration import create_message


class AgentOrchestrator:

    def __init__(self):
        self.agents = AGENTS
        self.messages = []

    def get_agents(self):
        return self.agents

    def assign_task(self, task: str, agent_id: str):
        agent = next(
            (agent for agent in self.agents if agent["id"] == agent_id),
            None
        )

        if not agent:
            return {
                "success": False,
                "error": "Agent not found"
            }

        message = create_message(
            sender="orchestrator",
            receiver=agent_id,
            message_type="task",
            content={
                "task": task
            }
        )

        self.messages.append(message)

        return {
            "success": True,
            "agent": agent,
            "message": message
        }

    def get_messages(self):
        return self.messages


orchestrator = AgentOrchestrator()