import matplotlib.pyplot as plt

# Test scores of students
scores = [45, 56, 67, 78, 45, 55, 62, 80, 90, 77, 58, 48]

# Define the bins (ranges)
bins = [40, 50, 60, 70, 80, 90, 100]

# Plot the histogram
plt.hist(scores, bins=bins, color='blue', edgecolor='black')

# Add labels and title
plt.xlabel("Score Ranges")
plt.ylabel("Number of Students")
plt.title("Student Test Score Distribution")

# Show the plot
plt.show()


# NOTE:
### **What is a Histogram?**

# A histogram is a type of bar chart that represents the **distribution of data**. It shows the number of data points that fall into specific ranges (called **bins**).

# ---

# ### **Key Parts of a Histogram**
# 1. **Bins (Ranges):** The intervals that group the data (e.g., 0-10, 10-20).
# 2. **Frequency:** The count of data points that fall into each bin (shown as the height of the bars).

# ---

# ### **Why Use a Histogram?**
# To visually analyze data distributions and find patterns like:
# - **Which range has the most data?**
# - **Are the data evenly distributed or skewed?**

# ---

# ### **Simple Example**
# Imagine you have the following test scores of students:
# `[45, 56, 67, 78, 45, 55, 62, 80, 90, 77, 58, 48]`

# You want to group the scores into bins like:
# - 40-50
# - 50-60
# - 60-70
# - 70-80
# - 80-90

# ---

# ### **How to Create a Histogram in Python**

# #### **Step-by-step Code**
# ```python
# import matplotlib.pyplot as plt

# # Test scores of students
# scores = [45, 56, 67, 78, 45, 55, 62, 80, 90, 77, 58, 48]

# # Define the bins (ranges)
# bins = [40, 50, 60, 70, 80, 90, 100]

# # Plot the histogram
# plt.hist(scores, bins=bins, color='blue', edgecolor='black')

# # Add labels and title
# plt.xlabel("Score Ranges")
# plt.ylabel("Number of Students")
# plt.title("Student Test Score Distribution")

# # Show the plot
# plt.show()
# ```

# ---

# ### **Explanation**
# 1. **Data (`scores`)**: The list of student scores.
# 2. **Bins (`bins`)**: Groups the scores into ranges (40–50, 50–60, etc.).
# 3. **`plt.hist`**: Draws the histogram.
# 4. **Labels (`xlabel`, `ylabel`)**: Explain the X and Y axes.
# 5. **`plt.show()`**: Displays the plot.

# ---

# ### **Output**
# The histogram will show:
# - A bar for each range.
# - The height of each bar indicates how many scores are in that range.

# ---

# ### **Practice Exercise**
# Try creating a histogram for these weights of people:
# `[55, 60, 45, 70, 65, 80, 50, 55, 75, 85, 90]`

# Bins: `[40, 50, 60, 70, 80, 90, 100]`

# Let me know if you'd like help with this! 😊
