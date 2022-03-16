from dotenv import dotenv_values
from pathlib import Path

env_config = dotenv_values(dotenv_path=Path(__file__).resolve().parent.parent / "env/.env")
BASE_DIR = Path(__file__).resolve().parent.parent
