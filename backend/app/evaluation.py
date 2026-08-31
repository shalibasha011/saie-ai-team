from typing import Dict, List


class AIEvaluationFramework:

    def evaluate(
        self,
        agent_id: str,
        outcomes: List[Dict]
    ) -> Dict:

        agent_outcomes = [
            outcome for outcome in outcomes
            if outcome["agent_id"] == agent_id
        ]

        if not agent_outcomes:
            return {
                "agent_id": agent_id,
                "total_evaluations": 0,
                "success_rate": 0,
                "average_score": 0,
                "performance": "no_data"
            }

        total = len(agent_outcomes)

        successful = sum(
            1 for outcome in agent_outcomes
            if outcome["success"]
        )

        average_score = sum(
            outcome["score"]
            for outcome in agent_outcomes
        ) / total

        success_rate = round(
            successful / total * 100,
            2
        )

        if average_score >= 90:
            performance = "excellent"
        elif average_score >= 75:
            performance = "good"
        elif average_score >= 50:
            performance = "needs_improvement"
        else:
            performance = "poor"

        return {
            "agent_id": agent_id,
            "total_evaluations": total,
            "successful_outcomes": successful,
            "success_rate": success_rate,
            "average_score": round(average_score, 2),
            "performance": performance
        }


ai_evaluation = AIEvaluationFramework()