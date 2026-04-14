from scipy.stats import norm
# Define our battery parameters
mu = 9.0      # Mean (loc)
sigma = 0.1   # Standard Deviation (scale)
# Find the area up to the upper limit (9.2V)
upper_area = norm.cdf(9.2, loc=mu, scale=sigma)
# Find the area up to the lower limit (8.8V)
lower_area = norm.cdf(8.8, loc=mu, scale=sigma)
# The probability of being between 8.8V and 9.2V
prob_between = upper_area - lower_area
print(f"Probability between 8.8V and 9.2V: {prob_between:.4f}")
# Output: Probability between 8.8V and 9.2V: 0.9545 (or 95.45%)