# In-memory storage for Cloud Run compatibility
_store = {
    "tasks": [],
    "events": [],
    "notes": [],
    "_task_id": 1,
    "_event_id": 1,
    "_note_id": 1,
}

def get_store():
    return _store
