from typing import Dict, List


class OutcomeTracker:

    def __init__(self):
        self.outcomes: List[Dict] = []

    def record_outcome(
        self,
        goal: str,
        task: str,
        agent_id: str,
        success: bool,
        score: float
    ) -> Dict:

        outcome = {
            "id": len(self.outcomes) + 1,
            "goal": goal,
            "task": task,
            "agent_id": agent_id,
            "success": success,
            "score": score
        }

        self.outcomes.append(outcome)

        return outcome

    def get_outcomes(self) -> List[Dict]:
        return self.outcomes

    def get_summary(self) -> Dict:
        total = len(self.outcomes)

        if total == 0:
            return {
                "total_outcomes": 0,
                "successful_outcomes": 0,
                "success_rate": 0,
                "average_score": 0
            }

        successful = sum(
            1 for outcome in self.outcomes
            if outcome["success"]
        )

        average_score = sum(
            outcome["score"] for outcome in self.outcomes
        ) / total

        return {
            "total_outcomes": total,
            "successful_outcomes": successful,
            "success_rate": round(successful / total * 100, 2),
            "average_score": round(average_score, 2)
        }


outcome_tracker = OutcomeTracker()