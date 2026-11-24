-- Phase 1: can we trust this experiment?
-- One row per group: sizes, outcome rates, and exposure.
-- Exposure must be 0 for every control user, or treatment leaked into control.
SELECT
    treatment,
    COUNT(*)                         AS n_users,
    COUNT(*) / SUM(COUNT(*)) OVER () AS share_of_users,
    AVG(visit)                       AS visit_rate,
    AVG(conversion)                  AS conversion_rate,
    AVG(exposure)                    AS exposure_rate,
    SUM(CASE WHEN f0 IS NULL THEN 1 ELSE 0 END) AS null_f0
FROM criteo
GROUP BY treatment
ORDER BY treatment;
