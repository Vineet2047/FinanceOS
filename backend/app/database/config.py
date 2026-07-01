from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "financeos.db"

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"
