from google.adk.agents import LlmAgent

from .task_tools import create_task, list_tasks, update_task_status, delete_task
from .calendar_tools import create_event, list_events, delete_event
from .notes_tools import create_note, search_notes, list_notes, delete_note

MODEL = "gemini-2.5-flash"

# ── Sub-agent 1: Task Manager ──
task_agent = LlmAgent(
    name="task_agent",
    model=MODEL,
    description="Specialist for creating, listing, updating, and deleting tasks.",
    instruction="""You are a task management specialist.
Help users manage their to-do list using the tools available to you.
When creating tasks: confirm the title, priority, and due date.
When listing tasks: display as a numbered list with ID, status, and priority.
When updating: confirm the task ID and new status.
Always confirm what action was taken.""",
    tools=[create_task, list_tasks, update_task_status, delete_task],
)

# ── Sub-agent 2: Calendar Manager ──
calendar_agent = LlmAgent(
    name="calendar_agent",
    model=MODEL,
    description="Specialist for scheduling events and managing the calendar.",
    instruction="""You are a calendar and scheduling specialist.
Help users schedule and manage events using the tools available to you.
When creating events: confirm title, date, time, and location.
When listing events: display in chronological order with full details.
Always use YYYY-MM-DD HH:MM format for times.
Always confirm what action was taken.""",
    tools=[create_event, list_events, delete_event],
)

# ── Sub-agent 3: Notes Manager ──
notes_agent = LlmAgent(
    name="notes_agent",
    model=MODEL,
    description="Specialist for saving, searching, and retrieving notes.",
    instruction="""You are a notes and information management specialist.
Help users store and retrieve information using the tools available to you.
When creating notes: confirm the title and tags used.
When searching: show matching note titles and a brief excerpt.
Always confirm what action was taken.""",
    tools=[create_note, search_notes, list_notes, delete_note],
)

# ── Root Agent: Orchestrator ──
root_agent = LlmAgent(
    name="orchestrator",
    model=MODEL,
    description="Primary AI assistant coordinating task, calendar, and notes management.",
    instruction="""You are a personal AI assistant that helps users manage tasks, schedules, and information.

You coordinate three specialist sub-agents:
- task_agent: for anything about tasks (create, list, update, complete, delete)
- calendar_agent: for events, meetings, and scheduling
- notes_agent: for saving notes, searching information, retrieving stored data

Always transfer to the right specialist to handle the request.
For requests spanning multiple domains, handle them one at a time by transferring to each relevant agent.
If the user is just chatting or asking something general, respond directly without transferring.""",
    sub_agents=[task_agent, calendar_agent, notes_agent],
)
