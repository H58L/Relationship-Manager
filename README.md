# Relationship-Manager

Build order

Step 1 — Project skeleton

Python environment
FastAPI
configuration
folder structure
/health

Step 2 — Synthetic banking data

ABC Industries
accounts/products
transactions
service cases
meeting notes
product catalogue

Step 3 — Basic RAG

ingest meeting notes/emails
chunk
embed
retrieve relevant context

Step 4 — MCP

expose customer/product/service information as tools
make the agent capable of deciding when to call them

Step 5 — Agent

understand RM request
determine required information
call tools
retrieve documents
synthesize evidence
generate briefing

Step 6 — Grounding
Every important recommendation gets its evidence.

Step 7 — Evaluation
We'll create questions where we know the expected answer and test whether the agent actually reaches it.

<br><hr>
<h1>Dependencies</h1>
<li>FastApi: FastAPI = framework for building the API</li>
<li>Uvicorn: Uvicorn = server that runs the API</li>

<hr>
<h1>Running the app</h1>
<li>Create and activate virtual environment:  python -m venv venv , venv\Scripts\activate</li>
<li>Install dependencies: pip install -r requirements.txt  </li>
<li>Run: uvicorn app.main:app_rm --reload </li>
