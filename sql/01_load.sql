-- Load the raw CSV into a typed table, then save a Parquet copy for fast reads.
CREATE OR REPLACE TABLE criteo AS
SELECT
    f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11,
    CAST(treatment  AS TINYINT) AS treatment,
    CAST(conversion AS TINYINT) AS conversion,
    CAST(visit      AS TINYINT) AS visit,
    CAST(exposure   AS TINYINT) AS exposure
FROM read_csv('data/raw/criteo-research-uplift-v2.1.csv.gz', header = true);

COPY criteo TO 'data/criteo.parquet' (FORMAT parquet);
