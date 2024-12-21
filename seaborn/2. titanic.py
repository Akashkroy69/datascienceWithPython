import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Set a larger context for better visibility
sns.set_context('notebook', font_scale=1.2)

# Count plot for passengers by class
sns.countplot(data=titanic, x='class', hue='who')
plt.title('Count of Passengers by Class and Who')
plt.show()

# Box plot for fare distribution by class
sns.boxplot(data=titanic, x='class', y='fare', hue='survived')
plt.title('Fare Distribution by Class and Survival Status')
plt.show()

# Heatmap for correlation matrix
corr = titanic.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Titanic Dataset')
plt.show()
