"""Load the raw CSV into data/criteo.duckdb and write data/criteo.parquet."""

from criteo_incrementality.db import connect, run_sql_file

if __name__ == "__main__":
    con = connect()
    run_sql_file("01_load.sql", con)
    n = con.execute("SELECT COUNT(*) FROM criteo").fetchone()[0]
    print(f"Loaded {n:,} rows")  # expect 13,979,592
    con.close()
