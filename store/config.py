import os

def try_parse(type, value: str):
    try:
        return type(value)
    except Exception:
        return None

POSTGRES_HOST = os.environ.get("POSTGRES_HOST") or "mypostgresserver2.postgres.database.azure.com"
POSTGRES_PORT = try_parse(int, os.environ.get("POSTGRES_PORT")) or 5432
POSTGRES_USER = os.environ.get("POSTGRES_USER") or "myadmin"
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASS") or "pass"
POSTGRES_DB = os.environ.get("POSTGRES_DB") or "flexibleserverdb"
