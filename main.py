from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.trip import router

app = FastAPI(
    title="AI Travel Planner API",
    description="Multi-Agent AI Travel Planner Backend powered by LangGraph and Gemini.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "AI Travel Planner API",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy",
    }