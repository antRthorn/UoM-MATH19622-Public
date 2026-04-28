import numpy as np
from scipy import stats
# 1. Input the Load Cell experimental data
mass = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
voltage = np.array([3, 5, 4, 7, 6, 8, 9, 11, 10, 12])
# 2. Perform Linear Regression
slope, intercept, r_value, p_value, std_err = stats.linregress(mass, voltage)
# 3. Calculate R-squared
r_squared = r_value**2
# 4. Output the engineering model
print("--- Load Cell Calibration Model ---")
print(f"Sensitivity (m): {slope:.3f} mV/kg")
print(f"Zero-Offset (c): {intercept:.3f} mV")
print(f"Correlation (r): {r_value:.3f}")
print(f"Goodness of Fit (R^2): {r_squared:.3f}")
print(f"Equation: Y = {slope:.3f}X + {intercept:.3f}")
