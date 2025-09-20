import React, { useState } from "react";
import { fetchRepo, aiPlan, runExecutor } from "./api";

export default function App() {
  const [repo, setRepo] = useState({});
  const [logs, setLogs] = useState("");

  return (
    <div>
      <button onClick={async () => setRepo(await fetchRepo())}>
        Load Repo
      </button>
      <button onClick={async () => await aiPlan()}>
        AI Plan
      </button>
      <button onClick={async () => {
        const res = await runExecutor();
        setLogs(res.logs);
      }}>
        Run Pipeline
      </button>

      <pre>{JSON.stringify(repo, null, 2)}</pre>
      <pre>{logs}</pre>
    </div>
  );
}
