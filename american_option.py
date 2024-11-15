#!/usr/bin/env python3
import numpy as np

# provider
pp = np
def american_option(number_grid_points,
                    time_delta,
                    strike,
                    volatility,
                    risk_free_rate,
                    expiry,
                    dtype=pp.float64):
    # Define the coordinate grid
    s_min = 0.01
    s_max = 300.0
    grid = pp.linspace(s_min, s_max, num=number_grid_points, dtype=dtype)

