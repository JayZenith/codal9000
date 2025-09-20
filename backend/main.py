from fastapi import FastAPI
from ai_agent import generate_patch
from executor import run_pipeline
from repo_loader import read_repo, write_files

app = FastAPI()

# returns toy_repo files as a dict
@app.get("/repo/files")
def get_repo_files():
    return read_repo("toy_repo")

# calls AI to generate "patch" (Dockerfile, CI YAML, tests) into repo
@app.post("/ai/plan")
def ai_plan():
    repo_state = read_repo("toy_repo")
    patch = generate_patch(repo_state)
    # write_files() updates repo
    write_files("toy_repo", patch)
    return {"patch": patch}

# runs a pipeline (docker build) in repo
@app.post("/executor/run")
def executor_run():
    logs = run_pipeline("toy_repo")
    return {"logs": logs}
