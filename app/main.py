from fastapi import FastAPI
from app.models import Flow
from app.flow_engine import FlowEngine

app = FastAPI(title="Async Flow Manager Service")


@app.post("/run-flow")
async def run_flow(flow_json: dict):
    """
    Executes a predefined flow asynchronously.
    """

    flow = Flow(**flow_json.get("flow"))
    engine = FlowEngine(flow)

    return await engine.run()
