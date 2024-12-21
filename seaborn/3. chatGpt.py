import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd

# Load a built-in dataset
print("------tips: built in data set------")
tips = sb.load_dataset('tips')
print(tips.head())
print("------------")
# 1. scatterplot
# sb.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
# plt.title('Scatter Plot of Total Bill vs Tip')
# plt.show()

# 2. lineplot
# sb.lineplot(data=tips, x='size', y='tip', hue='day')
# plt.title('Line Plot of Tip vs Size')
# plt.show()

# 3. histogram
sb.histplot(data=tips, x='total_bill', bins=30, kde=True)
plt.title('Histogram of Total Bill')
plt.show()

