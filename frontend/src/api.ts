import axios from "axios";

const API = "http://localhost:8000";

export async function fetchRepo() {
  return axios.get(`${API}/repo/files`).then(res => res.data);
}

export async function aiPlan() {
  return axios.post(`${API}/ai/plan`).then(res => res.data);
}

export async function runExecutor() {
  return axios.post(`${API}/executor/run`).then(res => res.data);
}
