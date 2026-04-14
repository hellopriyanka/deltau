**myAgent — AI Personal Assiostant**
Multi-Agent System | ADK + Gemini + Cloud Run + Firestore + Python

**Project structure**
my-agent/
├── agent.py              # Core agent logic (ADK LlmAgent)
├── calendar_tools.py     # Calendar-related tools
├── notes_tools.py        # Notes management tools
├── task_tools.py         # Task management tools
├── db.py                 # Database connection & queries
├── agent_system.db       # SQLite database file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables
├── .env.example          # Environment variable template (recommended)
├── main.py               # FastAPI HTTP server (to be added)
├── Dockerfile            # Container image for Cloud Run (to be added)
├── .adk/                 # ADK config & artifacts
│   └── artifacts/
├── __pycache__/          # Python cache files
└── venv/                 # Virtual environment
    ├── bin/
    ├── include/
    ├── lib/
    ├── lib64/
    └── pyvenv.cfg


**Live URL: **https://multi-agent-system-618786985600.us-central1.run.app
**GitHub:** 	https://github.com/hellopriyanka/deltauStack: 	Google ADK + Gemini 2.5 Flash + Cloud Run + Vertex AI

**Requirements**
google-adk>=1.0.0
google-cloud-aiplatform
