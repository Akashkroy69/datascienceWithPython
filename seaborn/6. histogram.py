import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset('tips')

# Create a histogram
sns.histplot(df['total_bill'], bins=10)
plt.show()
