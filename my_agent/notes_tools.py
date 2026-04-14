from .db import get_store
from datetime import datetime

def create_note(title: str, content: str, tags: str = "") -> dict:
    """Save a new note.
    Args:
        title: Note title (required).
        content: Note body text (required).
        tags: Optional comma-separated tags e.g. 'work,urgent'.
    Returns:
        Dict with success status and note ID.
    """
    store = get_store()
    note = {
        "id": store["_note_id"],
        "title": title,
        "content": content,
        "tags": tags,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    store["notes"].append(note)
    store["_note_id"] += 1
    return {"success": True, "note_id": note["id"], "title": title, "tags": tags}

def search_notes(query: str) -> dict:
    """Search notes by keyword in title, content, or tags.
    Args:
        query: The search keyword or phrase.
    Returns:
        Dict containing matching notes.
    """
    store = get_store()
    q = query.lower()
    notes = [n for n in store["notes"] if q in n["title"].lower() or q in n["content"].lower() or q in n["tags"].lower()]
    return {"notes": notes, "count": len(notes)}

def list_notes() -> dict:
    """List all saved notes.
    Returns:
        Dict containing all notes.
    """
    store = get_store()
    return {"notes": store["notes"], "count": len(store["notes"])}

def delete_note(note_id: int) -> dict:
    """Delete a note by its ID.
    Args:
        note_id: The integer ID of the note to delete.
    Returns:
        Dict confirming deletion.
    """
    store = get_store()
    store["notes"] = [n for n in store["notes"] if n["id"] != note_id]
    return {"success": True, "deleted_note_id": note_id}
