"""Phase 1 sanity checks: group sizes, outcome rates, exposure leakage."""

from criteo_incrementality.db import run_sql_file

if __name__ == "__main__":
    print(run_sql_file("02_sanity_checks.sql").to_string(index=False))
