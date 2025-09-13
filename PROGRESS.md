# 📌 Project Progress — AIatHome

## ✅ Current Status
- Repo: [erichhugo-beep/AI-at-home](https://github.com/erichhugo-beep/AI-at-home)  
- Environment: Python 3.12, venv working  
- Config: config/client.yaml created and loaded OK  
- Logs: logs/client.log records idle/active events  
- Client: client/cli.py runs idle detection loop  
- Workloads:
  - dummy workload added  
  - Starts on idle, stops on active  
  - Confirmed in logs  
- Documentation: README.md created and pushed  
- Git: commits and pushes successful, branch = main  

---

## 📂 Repo Structure (key parts)
AI-at-home/
├── client/
│ └── cli.py
├── workloads/
│ ├── init.py
│ └── dummy/
│ ├── init.py
│ └── run.py
├── config/
│ └── client.yaml
├── logs/
│ └── client.log
├── requirements.txt
├── README.md
└── PROGRESS.md 👈 (this file)
---

## 📝 What We Did Step by Step
1. Created GitHub repo and cloned locally.  
2. Setup project folders (client, workloads, config, logs, scripts, etc.).  
3. Added client.yaml config with idle/active thresholds.  
4. Installed dependencies (	yper, ich, etc.) and locked equirements.txt.  
5. Built client/cli.py:
   - Detects idle/active state.  
   - Logs events.  
6. Created dummy workload (workloads/dummy/run.py) that simulates CPU load.  
7. Wired workload into client:  
   - On idle → dummy runs.  
   - On active → dummy stops.  
8. Verified logs show dummy start/stop.  
9. Wrote README.md with setup & usage.  
10. Committed & pushed everything to GitHub.

---

## ⚠️ Open Items / Next Steps
- [ ] Add **real workload** (e.g. Whisper, or another script).  
- [ ] Make config select which workload runs (not just dummy).  
- [ ] Improve error handling/logging.  
- [ ] Package into pip install -e . for easier usage.  

---

## 🏁 End of Day State
- Project is runnable.  
- Dummy workload proof-of-concept is working.  
- Repo is synced and ready for continuation.  
