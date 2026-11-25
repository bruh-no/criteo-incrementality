
WITH long AS (
    UNPIVOT criteo ON f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11
    INTO NAME feature VALUE value
)
SELECT feature,
    AVG(value) FILTER (WHERE treatment = 1) AS mean_t,
    AVG(value) FILTER (WHERE treatment = 0) AS mean_c,
    VAR_SAMP(value) FILTER (WHERE treatment = 1) AS var_t,
    VAR_SAMP(value) FILTER (WHERE treatment = 0) AS var_c,
    (mean_t - mean_c) / SQRT((var_t + var_c) / 2) AS smd
FROM long
GROUP BY feature
ORDER BY CAST(SUBSTR(feature, 2) AS INTEGER)