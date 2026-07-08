from typing import Literal

from pydantic import BaseModel, Field, field_validator


class TripRequest(BaseModel):
    """Request payload for generating a travel itinerary."""

    destination: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Name of the city or country the trip should be planned for.",
        examples=["Paris"],
    )

    days: int = Field(
        ...,
        ge=1,
        le=30,
        description="Number of travel days.",
        examples=[5],
    )

    budget: float = Field(
        ...,
        gt=0,
        description="Total travel budget.",
        examples=[2000],
    )

    travel_style: Literal[
        "Adventure",
        "Luxury",
        "Budget",
        "Family",
        "Romantic",
        "Business",
    ] = Field(
        ...,
        description="Preferred travel style.",
        examples=["Luxury"],
    )

    travelers: int = Field(
        ...,
        ge=1,
        le=20,
        description="Number of travelers.",
        examples=[2],
    )

    @field_validator("destination")
    @classmethod
    def strip_and_validate_destination(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError(
                "Destination must not be empty."
            )

        return value


class TripResponse(BaseModel):
    """Response payload returned by the AI Travel Planner."""

    destination: str = Field(
        ...,
        description="Destination selected by the user.",
    )

    itinerary: str = Field(
        ...,
        description="Generated AI travel itinerary.",
    )