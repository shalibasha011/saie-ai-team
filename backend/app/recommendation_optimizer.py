from typing import Dict, List


class RecommendationOptimizer:

    def optimize(
        self,
        goal: str,
        recommendations: List[str],
        feedback_scores: List[float]
    ) -> Dict:

        optimized_recommendations = []

        for index, recommendation in enumerate(recommendations):
            score = (
                feedback_scores[index]
                if index < len(feedback_scores)
                else 0
            )

            optimized_recommendations.append(
                {
                    "id": index + 1,
                    "recommendation": recommendation,
                    "score": score
                }
            )

        optimized_recommendations.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return {
            "goal": goal,
            "total_recommendations": len(optimized_recommendations),
            "recommendations": optimized_recommendations,
            "best_recommendation": (
                optimized_recommendations[0]
                if optimized_recommendations
                else None
            ),
            "status": "optimized"
        }


recommendation_optimizer = RecommendationOptimizer()