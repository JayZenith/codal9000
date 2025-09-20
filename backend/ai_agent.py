import requests
import re
import os

#you need to parse all this 
# Get a list of Python dependencies from requirements.txt
with open("./toy_repo/requirements.txt") as f:
    dependencies = [line.strip() for line in f if line.strip()]

# Detect exposed ports (maybe hardcode or parse from Flask config)
exposed_ports = [5000]

def generate_patch(repo_state: dict):
    repo_state = {
        "dependencies": dependencies,
        "python_version": "3.10",
        "exposed_ports": exposed_ports,
        "extra_packages": ["build-essential", "python-psycopg2"],
        "entrypoint": "app.py",  # real main file of your Flask app
        "copy_paths": [". /app/"]
    }

    prompt = f"""
    You are an AI assistant that outputs ONLY a complete, ready-to-use Dockerfile as plain text. 
    Do NOT include comments, markdown, or explanations.

    Repo information: {repo_state}

    Rules:
    1. Use the specified Python version.
    2. Set WORKDIR to /app before copying any files.
    3. Copy requirements.txt first and install dependencies using `pip install -r requirements.txt`.
    4. Install extra system packages with `apt-get install -y ...`, then remove apt cache using `rm -rf /var/lib/apt/lists/*`.
    5. Copy the rest of the repository files into /app.
    6. Expose the listed ports.
    7. Set CMD to ["python", "<entrypoint>"] if the entrypoint ends with .py.
    8. Ensure Dockerfile uses best practices for layer caching and minimal image size.
    """



    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gemma:7b",
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
