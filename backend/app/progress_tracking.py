from typing import Dict, List


class ProgressTracker:

    def __init__(self):
        self.items: List[Dict] = []

    def add_item(
        self,
        goal: str,
        task: str,
        agent_id: str,
        status: str = "pending"
    ) -> Dict:

        item = {
            "id": len(self.items) + 1,
            "goal": goal,
            "task": task,
            "agent_id": agent_id,
            "status": status
        }

        self.items.append(item)

        return item

    def update_status(
        self,
        item_id: int,
        status: str
    ) -> Dict:

        for item in self.items:
            if item["id"] == item_id:
                item["status"] = status
                return item

        return {
            "error": "Progress item not found"
        }

    def get_items(self) -> List[Dict]:
        return self.items

    def get_summary(self) -> Dict:
        total = len(self.items)

        completed = sum(
            1 for item in self.items
            if item["status"] == "completed"
        )

        in_progress = sum(
            1 for item in self.items
            if item["status"] == "in_progress"
        )

        pending = sum(
            1 for item in self.items
            if item["status"] == "pending"
        )

        progress_percentage = (
            round((completed / total) * 100, 2)
            if total > 0
            else 0
        )

        return {
            "total": total,
            "completed": completed,
            "in_progress": in_progress,
            "pending": pending,
            "progress_percentage": progress_percentage
        }


progress_tracker = ProgressTracker()