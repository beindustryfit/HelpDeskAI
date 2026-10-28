"""Week 3: POST /classify goes here. Left as a tiny app so Docker has something to start."""
from fastapi import FastAPI

app = FastAPI(title="HelpDesk AI")


@app.get("/")
def root():
    return {"app": "helpdesk-ai", "hint": "Week 3 adds POST /classify"}
