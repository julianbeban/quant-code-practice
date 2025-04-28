import matplotlib.pyplot as plt

# Data from the updated table
funds = ['CSC Portfolio', 'S&P 500 (SPX)', 'VGSTX', 'SWGRX', 'BETFX']
returns = [-5.83, -6.06, -0.66, 0.37, -0.90]
std_devs = [17.23, 38.17, 30.64, 19.86, 20.03]
colors = ['darkblue', 'darkgrey', 'slategrey', 'lightsteelblue', 'whitesmoke']  # Colors

# Create plot
plt.figure(figsize=(10, 6))
plt.grid(True, linestyle='--', alpha=0.7)
for i in range(len(funds)):
    plt.scatter(std_devs[i], returns[i], s=300, color=colors[i], label=funds[i], alpha=1.0, edgecolors='black')

# Labels and title
plt.title('Risk vs. Return Profile (Updated)', fontsize=16)
plt.xlabel('Standard Deviation (%)', fontsize=14)
plt.ylabel('YTD Return (%)', fontsize=14)

# Customize x and y axis range
plt.xlim(10, 40)
plt.ylim(-10, 5)

# Add legend
plt.legend(title='Portfolio/Fund')
plt.legend(markerscale = 0.5) 

# Show plot
plt.tight_layout()
plt.show()
