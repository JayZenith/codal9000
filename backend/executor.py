import subprocess

def run_pipeline(repo_path: str):
    try:
        build = subprocess.run(
            ["docker", "build", "-t", "demo-app", "."],
            cwd=repo_path, capture_output=True, text=True
        )
        if build.returncode != 0:
            return build.stderr

        test = subprocess.run(
            ["docker", "run", "demo-app", "pytest"],
            cwd=repo_path, capture_output=True, text=True
        )
        return test.stdout + test.stderr
    except Exception as e:
        return str(e)
