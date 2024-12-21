import numpy as np
import matplotlib.pyplot as plt

# Data for sales
years = ['2021', '2022', '2023']
apples = [500, 600, 700]
bananas = [400, 500, 600]
oranges = [300, 400, 500]

# Bar width
barWidth = 0.25

# Positions for the bars
br1 = np.arange(len(years))  # Positions for apples
print(br1)
br2 = [x + barWidth for x in br1]  # Positions for bananas
br3 = [x + barWidth for x in br2]  # Positions for oranges
print(br2)
print(br3)


# Plot the bars
plt.bar(br1, apples, color='red', width=barWidth, label='Apples')
plt.bar(br2, bananas, color='yellow', width=barWidth, label='Bananas')
plt.bar(br3, oranges, color='orange', width=barWidth, label='Oranges')

# Add labels and title
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Sales (in units)', fontweight='bold')
plt.title('Fruit Sales Over 3 Years', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(years))], years)

# Add legend
plt.legend()

# Show the plot
plt.show()
