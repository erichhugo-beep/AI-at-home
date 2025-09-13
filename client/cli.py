import os, sys, time, logging, ctypes
from logging.handlers import RotatingFileHandler
import typer, yaml
from dataclasses import dataclass

app = typer.Typer()
CONFIG_PATH = "config/client.yaml"
STATE_ACTIVE = "ACTIVE"
STATE_IDLE = "IDLE"

@dataclass
class Config:
    idle_threshold_seconds: int = 5
    debounce_seconds: int = 3
    log_dir: str = "./logs"
    primary_os: str = "auto"

def load_config() -> Config:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    base = Config().__dict__.copy()
    base.update(data)
    return Config(**base)

def ensure_logger(log_dir: str):
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger("client")
    logger.setLevel(logging.INFO)
    fh = RotatingFileHandler(os.path.join(log_dir, "client.log"), maxBytes=5000000, backupCount=5)
    fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.handlers.clear()
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

# Windows idle detection
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

def get_idle_seconds():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii)) == 0:
        return 0.0
    tick_now = ctypes.windll.kernel32.GetTickCount()
    idle_ms = tick_now - lii.dwTime
    return idle_ms / 1000.0

@app.command()
def doctor():
    typer.echo(f"Python {sys.version.split()[0]}")
    typer.echo("Idle detector: Windows API (GetLastInputInfo)")
    _ = load_config()
    typer.echo("Config loaded OK")

@app.command()
def run():
    cfg = load_config()
    logger = ensure_logger(cfg.log_dir)
    state = STATE_ACTIVE
    logger.info("START loop | threshold=%s debounce=%s", cfg.idle_threshold_seconds, cfg.debounce_seconds)
    try:
        while True:
            idle = get_idle_seconds()
            if state == STATE_ACTIVE and idle >= cfg.idle_threshold_seconds:
                state = STATE_IDLE
                logger.info("ENTER_IDLE idle=%.1fs", idle)
            elif state == STATE_IDLE and idle < 1.0:
                state = STATE_ACTIVE
                logger.info("ENTER_ACTIVE idle=%.1fs", idle)
            time.sleep(0.5)
    except KeyboardInterrupt:
        logger.info("STOP loop")

if __name__ == "__main__":
    app()
