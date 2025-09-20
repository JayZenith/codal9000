import os

def read_repo(path: str):
    files = {}
    for root, _, filenames in os.walk(path):
        for f in filenames:
            with open(os.path.join(root, f), "r") as fp:
                rel_path = os.path.relpath(os.path.join(root, f), path)
                files[rel_path] = fp.read()
    return files

def write_files(path: str, patch: dict):
    for filename, content in patch.items():
        full_path = os.path.join(path, filename)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
