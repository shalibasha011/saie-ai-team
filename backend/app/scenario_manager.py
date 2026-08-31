from typing import Dict, List


class ScenarioManager:

    def __init__(self):
        self.scenarios: List[Dict] = []

    def create_scenario(
        self,
        name: str,
        goal: str,
        assumptions: List[str]
    ) -> Dict:

        scenario = {
            "id": len(self.scenarios) + 1,
            "name": name,
            "goal": goal,
            "assumptions": assumptions,
            "status": "created"
        }

        self.scenarios.append(scenario)

        return scenario

    def get_scenarios(self) -> List[Dict]:
        return self.scenarios

    def get_scenario(self, scenario_id: int):
        for scenario in self.scenarios:
            if scenario["id"] == scenario_id:
                return scenario

        return None


scenario_manager = ScenarioManager()