"""Small helpers for running the project's SQL files against a local DuckDB database."""

from pathlib import Path

import duckdb
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_ROOT / "data" / "criteo.duckdb"
SQL_DIR = PROJECT_ROOT / "sql"


def connect() -> duckdb.DuckDBPyConnection:
    """Open the project database. Paths in SQL files are relative to the project root."""
    con = duckdb.connect(str(DB_PATH))
    con.execute(f"SET file_search_path = '{PROJECT_ROOT.as_posix()}'")
    return con


def run_sql_file(name: str, con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame | None:
    """Run every statement in sql/<name>; return the last statement's result as a DataFrame."""
    own = con is None
    con = con or connect()
    try:
        statements = [s for s in (SQL_DIR / name).read_text().split(";") if _has_code(s)]
        result = None
        for stmt in statements:
            result = con.execute(stmt)
        return result.df() if result is not None and result.description else None
    finally:
        if own:
            con.close()


def _has_code(stmt: str) -> bool:
    return any(line.strip() and not line.strip().startswith("--") for line in stmt.splitlines())
