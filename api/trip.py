from fastapi import APIRouter, HTTPException, status

from schemas.trip import TripRequest, TripResponse
from services.trip_service import TripGenerationError, TripService

router = APIRouter(
    prefix="/api/v1/trips",
    tags=["Trips"],
)

trip_service = TripService()


@router.post(
    "/generate",
    response_model=TripResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate AI Travel Itinerary",
    description="Generate an AI-powered travel itinerary using the LangGraph multi-agent workflow.",
)
async def generate_trip(request: TripRequest) -> TripResponse:
    try:
        itinerary = trip_service.generate_trip(
            destination=request.destination,
            days=request.days,
            budget=request.budget,
            travel_style=request.travel_style,
            travelers=request.travelers,
        )

        return TripResponse(
            destination=request.destination,
            itinerary=itinerary,
        )

    except TripGenerationError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected server error: {str(exc)}",
        ) from exc