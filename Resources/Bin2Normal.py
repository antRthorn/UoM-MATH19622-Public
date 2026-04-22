import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Setup the three scenarios
n_values = [10, 100, 1000]
p = 0.5

for n in n_values:
    # Set up the figure
    plt.figure(figsize=(4, 4))
    
    # Calculate parameters
    mu = n * p
    sigma = np.sqrt(n * p * (1 - p))
    
    # Define the x-axis range (only plot where the action is: +/- 4 standard deviations)
    x_min = int(mu - 4*sigma)
    x_max = int(mu + 4*sigma)
    
    # 1. Plot the Binomial Histogram (Bars)
    x_discrete = np.arange(x_min, x_max + 1)
    y_discrete = binom.pmf(x_discrete, n, p)
    
    # Adjust bar width based on n to make it look like a histogram
    bar_width = 1.0 if n == 10 else (1.0 if n == 100 else 1.0)
    plt.bar(x_discrete, y_discrete, width=bar_width, color='skyblue', edgecolor='black' if n < 1000 else 'none', alpha=0.7)
    
    # 2. Plot the Normal Approximation (Curve)
    x_continuous = np.linspace(x_min, x_max, 1000)
    y_continuous = norm.pdf(x_continuous, mu, sigma)
    plt.plot(x_continuous, y_continuous, 'r-', lw=2)
    
    # Clean up the plot
    plt.title(f"n = {n}")
    plt.xlabel("Number of Heads")
    plt.ylabel("Probability")
    plt.yticks([]) # Hide y-ticks to keep the slide clean
    
    # Save as PDF for Beamer
    plt.tight_layout()
    plt.savefig(f"Convergence_n{n}.pdf", transparent=True)
    plt.close()

print("Plots generated successfully!")
