import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("iris")

# Basic Info
print(df.head())
print(df.info())
print(df.describe())

# Univariate Analysis
# sns.histplot(df['sepal_length'])
# plt.show()

# # Multivariate Analysis
# sns.pairplot(df, hue='species')
# plt.show()

# # Correlation Heatmap
# sns.heatmap(df.corr(), annot=True)
# plt.show()

# # Outlier Detection
# sns.boxplot(x=df['sepal_length'])
# plt.show()

# Automated Report with Pandas Profiling (if installed)
# from pandas_profiling import ProfileReport
# profile = ProfileReport(df, title="Iris Data Report")
# profile.to_widgets()

