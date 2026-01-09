# Async Flow Manager Microservice

A generic, async, condition-driven flow manager that executes tasks sequentially and determines the next step based on task results.

## Features
- Fully async execution
- Enum-based task status
- JSON-defined workflows
- REST API using FastAPI
- Easy to extend and test

## Architecture
- Tasks are independent async functions
- Conditions control task transitions
- Flow engine is generic and reusable

## Setup

```bash
git clone https://github.com/santosh6146/project-test.git
cd project-test
pip install -r requirements.txt
uvicorn app.main:app --reload

## API Documentation

The API documentation is available at `http://localhost:8000/docs`.

## Example Usage

```bash
# Run a flow
POST http://localhost:8000/run-flow
Content-Type: application/json

{
    "flow": {
        "id": "flow123",
        "name": "Test Flow",
        "start_task": "task1",
        "tasks": [
            {
                "name": "task1",
                "description": "Fetch data"
            },
            {
                "name": "task2",
                "description": "Process data"
            },
            {
                "name": "task3",
                "description": "Store data"
            }
        ],
        "conditions": [
            {
                "name": "condition1",
                "description": "Success condition",
                "source_task": "task1",
                "target_task_success": "task2",
                "target_task_failure": "task3"
            }
        ]
    }
}
```
