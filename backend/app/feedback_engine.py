from typing import Dict, List


class FeedbackEngine:

    def __init__(self):
        self.feedback_history: List[Dict] = []

    def record_feedback(
        self,
        agent_id: str,
        task: str,
        score: float,
        feedback: str
    ) -> Dict:

        record = {
            "agent_id": agent_id,
            "task": task,
            "score": score,
            "feedback": feedback,
            "status": "recorded"
        }

        self.feedback_history.append(record)

        return record

    def get_feedback(self) -> List[Dict]:
        return self.feedback_history

    def get_agent_average_score(
        self,
        agent_id: str
    ) -> Dict:

        records = [
            item for item in self.feedback_history
            if item["agent_id"] == agent_id
        ]

        if not records:
            return {
                "agent_id": agent_id,
                "average_score": None,
                "total_feedback": 0
            }

        average_score = sum(
            item["score"] for item in records
        ) / len(records)

        return {
            "agent_id": agent_id,
            "average_score": round(average_score, 2),
            "total_feedback": len(records)
        }


feedback_engine = FeedbackEngine()