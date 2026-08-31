from typing import Dict, List


class RiskSimulationEngine:

    def simulate(
        self,
        scenario_name: str,
        risks: List[str]
    ) -> Dict:

        results = []

        for index, risk in enumerate(risks, start=1):
            probability = min(20 + (index * 15), 100)
            impact = min(30 + (index * 10), 100)

            risk_score = round(
                (probability * impact) / 100,
                2
            )

            if risk_score >= 60:
                level = "high"
            elif risk_score >= 30:
                level = "medium"
            else:
                level = "low"

            results.append(
                {
                    "id": index,
                    "risk": risk,
                    "probability": probability,
                    "impact": impact,
                    "risk_score": risk_score,
                    "level": level
                }
            )

        high_risks = [
            item for item in results
            if item["level"] == "high"
        ]

        return {
            "scenario": scenario_name,
            "total_risks": len(results),
            "high_risks": len(high_risks),
            "results": results,
            "status": "completed"
        }


risk_simulation_engine = RiskSimulationEngine()