from typing import Any

from graph.workflow import graph


class TripGenerationError(Exception):
    """Raised when the AI travel planner fails to generate an itinerary."""


class TripService:
    """Service layer for interacting with the LangGraph travel planner."""

    def generate_trip(
        self,
        destination: str,
        days: int,
        budget: float,
        travel_style: str,
        travelers: int,
    ) -> str:
        """
        Execute the LangGraph workflow and return the generated itinerary.

        Args:
            destination: Travel destination.
            days: Number of travel days.
            budget: User's travel budget.
            travel_style: Preferred travel style.
            travelers: Number of travelers.

        Returns:
            Generated itinerary as a string.

        Raises:
            TripGenerationError:
                If the workflow fails or does not return an itinerary.
        """

        state: dict[str, Any] = {
            "destination": destination,
            "days": days,
            "budget": budget,
            "travel_style": travel_style,
            "travelers": travelers,
        }

        try:
            result = graph.invoke(state)

            itinerary = result.get("final")

            if not itinerary:
                raise TripGenerationError(
                    "LangGraph did not return a final itinerary."
                )

            return itinerary

        except Exception as exc:
            if isinstance(exc, TripGenerationError):
                raise

            raise TripGenerationError(
                f"Workflow execution failed: {exc}"
            ) from exc