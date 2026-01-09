from app.models import Flow, TaskStatus
from app.tasks import TASK_REGISTRY


class FlowEngine:
    """
    Generic async flow execution engine.
    """

    def __init__(self, flow: Flow):
        self.flow = flow
        self.conditions = {
            condition.source_task: condition
            for condition in flow.conditions
        }

    async def run(self) -> dict:
        """
        Executes the flow asynchronously.
        """
        current_task = self.flow.start_task
        context_data = None

        while current_task != "end":
            print(f"\nExecuting task: {current_task}")

            task_func = TASK_REGISTRY.get(current_task)
            if not task_func:
                raise ValueError(f"Task '{current_task}' not found")

            # Execute task
            result = (
                await task_func(context_data)
                if context_data
                else await task_func()
            )

            condition = self.conditions.get(current_task)
            if not condition:
                print("No condition found. Ending flow.")
                break

            if result.status == TaskStatus.SUCCESS:
                current_task = condition.target_task_success
                context_data = result.data
            else:
                current_task = condition.target_task_failure

        return {
            "flow_id": self.flow.id,
            "status": "completed",
            "last_task": current_task
        }