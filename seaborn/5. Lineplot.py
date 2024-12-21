import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset('fmri')

print(df.head())
# Create a line plot
sns.lineplot(x='timepoint', y='signal',hue="region", data=df)
plt.show()
