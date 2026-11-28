import numpy as np
from scipy import stats


def diff_in_proportions(x_t, n_t, x_c, n_c, alpha=0.05):
    """Absolute lift (p_t - p_c) with a normal-approximation confidence interval.

    x_t, x_c: number of successes (e.g. visits) in treatment and control
    n_t, n_c: number of users in treatment and control
    """

    p_t = x_t / n_t
    p_c = x_c / n_c

    lift = p_t - p_c

    se = np.sqrt((p_t * (1 - p_t) / n_t) + (p_c * (1 - p_c) / n_c))

    z_crit = stats.norm.ppf(1 - alpha / 2)    # 1.96 when alpha = 0.05
    ci_low, ci_high = lift - z_crit * se, lift + z_crit * se

    z = lift / se

    rel_lift = lift / p_c

    return {"lift": lift, "se": float(se), "z": z, "ci_low": ci_low, "ci_high": ci_high, "rel_lift": rel_lift}