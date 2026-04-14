from .db import get_store
from datetime import datetime

def create_task(title: str, description: str = "", priority: str = "medium", due_date: str = "") -> dict:
    """Create a new task.
    Args:
        title: The task title (required).
        description: Optional task description.
        priority: low, medium, or high.
        due_date: Optional due date in YYYY-MM-DD format.
    Returns:
        Dict with success status and task ID.
    """
    store = get_store()
    task = {
        "id": store["_task_id"],
        "title": title,
        "description": description,
        "status": "pending",
        "priority": priority,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    store["tasks"].append(task)
    store["_task_id"] += 1
    return {"success": True, "task_id": task["id"], "title": title, "priority": priority}

def list_tasks(status: str = "all") -> dict:
    """List tasks, optionally filtered by status.
    Args:
        status: Filter by 'pending', 'in_progress', 'completed', or 'all'.
    Returns:
        Dict containing list of tasks.
    """
    store = get_store()
    tasks = store["tasks"] if status == "all" else [t for t in store["tasks"] if t["status"] == status]
    return {"tasks": tasks, "count": len(tasks)}

def update_task_status(task_id: int, status: str) -> dict:
    """Update the status of an existing task.
    Args:
        task_id: The integer ID of the task to update.
        status: New status - 'pending', 'in_progress', or 'completed'.
    Returns:
        Dict confirming the update.
    """
    store = get_store()
    for task in store["tasks"]:
        if task["id"] == task_id:
            task["status"] = status
            return {"success": True, "task_id": task_id, "new_status": status}
    return {"success": False, "error": f"Task {task_id} not found"}

def delete_task(task_id: int) -> dict:
    """Delete a task by its ID.
    Args:
        task_id: The integer ID of the task to delete.
    Returns:
        Dict confirming deletion.
    """
    store = get_store()
    store["tasks"] = [t for t in store["tasks"] if t["id"] != task_id]
    return {"success": True, "deleted_task_id": task_id}
