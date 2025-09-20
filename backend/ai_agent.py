import requests
import re

def generate_patch(repo_state: dict):
    prompt = f"""
    You are an assistant that outputs only the content of a Dockerfile.

    Task: Create a Dockerfile for this Python Flask repo: {repo_state}.
    Do not explain, do not add comments, do not wrap in markdown code fences.
    Output only the Dockerfile content as plain text.
    """

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3:8b",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        },
    )

    if response.status_code != 200:
        raise RuntimeError(f"Ollama error {response.status_code}: {response.text}")

    data = response.json()
    if "message" not in data or "content" not in data["message"]:
        raise RuntimeError(f"Unexpected Ollama response: {data}")

    raw = data["message"]["content"]

    # Remove ``` fences if the model ignores your instruction
    cleaned = re.sub(r"^```[a-zA-Z]*\n|```$", "", raw.strip(), flags=re.MULTILINE)

    return {"Dockerfile": cleaned.strip()}
