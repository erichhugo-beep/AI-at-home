# AIatHome

AIatHome is a lightweight client for monitoring system idle/active state and running workloads when your computer is idle.

## Features
- Detects idle and active time automatically.
- Configurable thresholds for idle detection.
- Extensible workload system (start with dummy workload).
- Simple configuration via `config/client.yaml`.

## Quick Start

### 1. Clone the repo
powershell
git clone https://github.com/erichhugo-beep/AI-at-home.git
cd AI-at-home

### 2. Create and activate virtual environment
powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

### 3. Install dependencies
powershell
pip install -r requirements.txt

### 4. Run client
powershell
python .\client\cli.py run

Logs will appear in `./logs/client.log`.

## Configuration
Edit `config/client.yaml`:
yaml
idle_threshold_seconds: 5
debounce_seconds: 3
log_dir: ./logs
primary_os: auto

## License
MIT License
