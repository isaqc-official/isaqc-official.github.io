import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

# Data for Beer-Lambert Law verification
concentrations = np.array([0, 20, 40, 60, 80, 100])  # Concentration percentages
# Replace these with your actual transmittance values
transmittance = np.array([100, 93.5, 85.5, 77.7, 73.5, 69.0])  # Example transmittance values (%)

# Convert transmittance to absorbance using A = -log10(T/100)
absorbance = -np.log10(transmittance / 100)

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Beer-Lambert Law verification (Concentration vs Absorbance)
ax1.scatter(concentrations, absorbance, color='blue', s=100, alpha=0.7, label='Data points')

# Linear regression for Beer-Lambert verification
X = concentrations.reshape(-1, 1)
reg = LinearRegression().fit(X, absorbance)
line_x = np.linspace(0, 100, 100)
line_y = reg.predict(line_x.reshape(-1, 1))

ax1.plot(line_x, line_y, 'r--', linewidth=2, label=f'Linear fit: A = {reg.coef_[0]:.4f}C + {reg.intercept_:.4f}')
ax1.set_xlabel('Concentration (%)', fontsize=12)
ax1.set_ylabel('Absorbance', fontsize=12)
ax1.set_title('Beer-Lambert Law Verification\n(Concentration vs Absorbance)', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Calculate R-squared
r_squared = reg.score(X, absorbance)
ax1.text(0.05, 0.95, f'R² = {r_squared:.4f}', transform=ax1.transAxes, 
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Plot 2: Calibration curve (Concentration vs Transmittance)
ax2.scatter(concentrations, transmittance, color='green', s=100, alpha=0.7, label='Data points')

# Exponential fit for transmittance curve
z = np.polyfit(concentrations, np.log(transmittance), 1)
p = np.poly1d(z)
curve_x = np.linspace(0, 100, 100)
curve_y = np.exp(p(curve_x))

ax2.plot(curve_x, curve_y, 'orange', linewidth=2, label='Exponential fit')
ax2.set_xlabel('Concentration (%)', fontsize=12)
ax2.set_ylabel('Transmittance (%)', fontsize=12)
ax2.set_title('Calibration Curve\n(Concentration vs Transmittance)', fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()

# Function to determine unknown concentration from transmittance
def find_unknown_concentration(unknown_transmittance):
    """
    Determine unknown concentration from transmittance value
    """
    unknown_absorbance = -np.log10(unknown_transmittance / 100)
    unknown_concentration = (unknown_absorbance - reg.intercept_) / reg.coef_[0]
    return unknown_concentration

# Example unknown samples
unknown_samples = [89.6, 81.6, 75.6]  # Example transmittance values

# Add unknown points and tracing lines to both plots
colors = ['red', 'purple', 'brown']
for i, trans in enumerate(unknown_samples):
    conc = find_unknown_concentration(trans)
    abs_val = -np.log10(trans / 100)
    
    # Plot 1: Add clean tracing lines for absorbance plot
    # Vertical line from x-axis to point
    ax1.axvline(x=conc, color=colors[i], linestyle='--', alpha=0.8, linewidth=1)
    # Horizontal line from y-axis to point
    ax1.axhline(y=abs_val, color=colors[i], linestyle='--', alpha=0.8, linewidth=1)
    # Simple circle marker at intersection
    ax1.scatter(conc, abs_val, color=colors[i], s=80, marker='o', 
               label=f'Unknown {i+1}', edgecolors='white', linewidth=1, zorder=5)
    
    # Plot 2: Add clean tracing lines for transmittance plot
    # Vertical line from x-axis to point
    ax2.axvline(x=conc, color=colors[i], linestyle='--', alpha=0.8, linewidth=1)
    # Horizontal line from y-axis to point
    ax2.axhline(y=trans, color=colors[i], linestyle='--', alpha=0.8, linewidth=1)
    # Simple circle marker at intersection
    ax2.scatter(conc, trans, color=colors[i], s=80, marker='o', 
               label=f'Unknown {i+1}', edgecolors='white', linewidth=1, zorder=5)

# Update legends to include unknown samples
ax1.legend(loc='upper left', fontsize=9)
ax2.legend(loc='upper right', fontsize=9)

# Add grid lines for better readability
ax1.grid(True, alpha=0.3, which='both')
ax2.grid(True, alpha=0.3, which='both')

# Example: Determine concentration for unknown samples
print("Beer-Lambert Law Verification Results:")
print(f"Linear equation: A = {reg.coef_[0]:.4f}C + {reg.intercept_:.4f}")
print(f"R-squared value: {r_squared:.4f}")
print("\n" + "="*50)

print("Unknown Sample Analysis:")
print("Graph-derived concentrations:")
for i, trans in enumerate(unknown_samples, 1):
    conc = find_unknown_concentration(trans)
    abs_val = -np.log10(trans / 100)
    print(f"Sample {i}: Transmittance = {trans}% → Absorbance = {abs_val:.4f} → Concentration = {conc:.2f}%")

# # Add text box with Beer-Lambert equation
# textstr = 'Beer-Lambert Law:\nA = εbc\nwhere:\nA = Absorbance\nε = Molar absorptivity\nb = Path length\nc = Concentration'
# props = dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
# fig.text(0.02, 0.02, textstr, fontsize=10, bbox=props)

plt.show()

# Create summary table
data_table = pd.DataFrame({
    'Concentration (%)': concentrations,
    'Transmittance (%)': transmittance,
    'Absorbance': absorbance.round(4)
})
print("\n" + "="*50)
print("Data Summary Table:")
print(data_table)
props = dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
fig.text(0.02, 0.02, textstr, fontsize=10, bbox=props)

plt.show()

# Create summary table
data_table = pd.DataFrame({
    'Concentration (%)': concentrations,
    'Transmittance (%)': transmittance,
    'Absorbance': absorbance.round(4)
})
print("\n" + "="*50)
print("Data Summary Table:")
print(data_table)
