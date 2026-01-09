from enum import Enum
from pydantic import BaseModel
from typing import List, Optional, Any


class TaskStatus(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class TaskResult(BaseModel):
    status: TaskStatus
    data: Optional[Any] = None


class Task(BaseModel):
    name: str
    description: str


class Condition(BaseModel):
    name: str
    description: str
    source_task: str
    target_task_success: str
    target_task_failure: str


class Flow(BaseModel):
    id: str
    name: str
    start_task: str
    tasks: List[Task]
    conditions: List[Condition]
