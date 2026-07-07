from langgraph.graph import StateGraph, END
from typing import TypedDict

from agents.planner_agent import planner
from agents.info_agent import travel_info
from agents.hotel_agent import hotel_info
from agents.flight_agent import flight_info
from agents.activity_agent import activity_info
from agents.synthesizer_agent import create_itinerary


class TravelState(TypedDict):
    destination: str
    planner: str
    info: str
    hotel: str
    flight: str
    activity: str
    final: str


# ---------------- Planner Node ----------------
def planner_node(state: TravelState):

    state["planner"] = planner(
        f"Plan a trip to {state['destination']}"
    )

    return state


# ---------------- Planner Router ----------------
def planner_router(state: TravelState):

    planner_output = state["planner"]

    if "Need Hotel: No" in planner_output:
        return "flight"

    return "info"


# ---------------- Info Node ----------------
def info_node(state: TravelState):

    state["info"] = travel_info(state["destination"])

    return state


# ---------------- Hotel Node ----------------
def hotel_node(state: TravelState):

    state["hotel"] = hotel_info(state["destination"])

    return state


# ---------------- Flight Node ----------------
def flight_node(state: TravelState):

    state["flight"] = flight_info(state["destination"])

    return state


# ---------------- Activity Node ----------------
def activity_node(state: TravelState):

    state["activity"] = activity_info(state["destination"])

    return state


# ---------------- Synthesizer Node ----------------
def synthesizer_node(state: TravelState):

    state["final"] = create_itinerary(
        state["info"],
        state["hotel"],
        state["flight"],
        state["activity"]
    )

    return state


# ---------------- Build Graph ----------------
builder = StateGraph(TravelState)

builder.add_node("planner", planner_node)
builder.add_node("info", info_node)
builder.add_node("hotel", hotel_node)
builder.add_node("flight", flight_node)
builder.add_node("activity", activity_node)
builder.add_node("synthesizer", synthesizer_node)

# Starting Node
builder.set_entry_point("planner")

# Conditional Routing
builder.add_conditional_edges(
    "planner",
    planner_router,
    {
        "info": "info",
        "flight": "flight",
    }
)

# Graph Flow
builder.add_edge("info", "hotel")
builder.add_edge("hotel", "flight")
builder.add_edge("flight", "activity")
builder.add_edge("activity", "synthesizer")
builder.add_edge("synthesizer", END)

graph = builder.compile()