from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Research Intel Agent",
    description="AI-powered research and competitive intelligence agent",
    version="0.1.0",
)


class ResearchRequest(BaseModel):
    query: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/research")
def run_research(request: ResearchRequest):
    return {
        "query": request.query,
        "status": "received",
    }
