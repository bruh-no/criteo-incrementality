SELECT treatment, 
    COUNT(*) AS n_users,
    SUM(visit) AS n_visits,
    SUM(conversion) AS n_conversions,
    n_visits / n_users AS visit_rate,
    n_conversions / n_users AS conversion_rate
FROM criteo
GROUP BY treatment
ORDER BY treatment