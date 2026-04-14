from .db import get_store
from datetime import datetime

def create_event(title: str, start_time: str, end_time: str = "", description: str = "", location: str = "") -> dict:
    """Schedule a new calendar event.
    Args:
        title: Event title (required).
        start_time: Start time in 'YYYY-MM-DD HH:MM' format (required).
        end_time: Optional end time in 'YYYY-MM-DD HH:MM' format.
        description: Optional event description.
        location: Optional event location.
    Returns:
        Dict with success status and event ID.
    """
    store = get_store()
    event = {
        "id": store["_event_id"],
        "title": title,
        "description": description,
        "start_time": start_time,
        "end_time": end_time,
        "location": location,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    store["events"].append(event)
    store["_event_id"] += 1
    return {"success": True, "event_id": event["id"], "title": title, "start_time": start_time}

def list_events(date_filter: str = "") -> dict:
    """List calendar events, optionally filtered by date string.
    Args:
        date_filter: Optional date string e.g. '2026-04' for April 2026.
    Returns:
        Dict containing list of events.
    """
    store = get_store()
    if date_filter:
        events = [e for e in store["events"] if date_filter in e["start_time"]]
    else:
        events = store["events"]
    return {"events": sorted(events, key=lambda x: x["start_time"]), "count": len(events)}

def delete_event(event_id: int) -> dict:
    """Delete a calendar event by its ID.
    Args:
        event_id: The integer ID of the event to delete.
    Returns:
        Dict confirming deletion.
    """
    store = get_store()
    store["events"] = [e for e in store["events"] if e["id"] != event_id]
    return {"success": True, "deleted_event_id": event_id}
