# ---------------------------------------------------------------
# Analyzing the Iris Dataset with Pandas & Visualizing with Matplotlib
# Author: Brendah Mwihaki Kiragu
# ---------------------------------------------------------------

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set a clean plotting style
sns.set_style("whitegrid")

# ---------------------------------------------------------------
# Task 1: Load and Explore the Dataset
# ---------------------------------------------------------------
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map(dict(zip(range(3), iris.target_names)))

    print("\n✅ Dataset successfully loaded!\n")
    print("First five rows:")
    print(df.head())

    # Display dataset structure
    print("\nDataset Info:")
    print(df.info())

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Clean dataset if missing values exist
    if df.isnull().sum().sum() > 0:
        df = df.dropna() 
        print("\n⚠️ Missing values handled!")

except FileNotFoundError:
    print("❌ Error: Dataset file not found. Please check your path!")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

# ---------------------------------------------------------------
# Task 2: Basic Data Analysis
# ---------------------------------------------------------------

print("\nBasic Statistical Summary:\n")
print(df.describe())

# Group by species and calculate mean for numerical columns
grouped_means = df.groupby("species").mean()
print("\nAverage Measurements by Species:\n")
print(grouped_means)

# Example interesting finding
print("\n📌 Observation: The 'virginica' species generally has the largest petal length and width on average.\n")

# ---------------------------------------------------------------
# Task 3: Data Visualization
# ---------------------------------------------------------------

# Set figure size for better visuals
plt.figure(figsize=(12, 8))

# 1. Line chart - Simulate a trend using cumulative sum of sepal length
df_sorted = df.sort_values("sepal length (cm)")
df_sorted["cumulative_sepal_length"] = df_sorted["sepal length (cm)"].cumsum()

plt.subplot(2, 2, 1)
plt.plot(df_sorted.index, df_sorted["cumulative_sepal_length"], color="purple", linewidth=2)
plt.title("Cumulative Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Cumulative Sepal Length")

# 2. Bar chart - Average petal length per species (fixed FutureWarning)
plt.subplot(2, 2, 2)
sns.barplot(
    x="species",
    y="petal length (cm)",
    hue="species",
    data=df,
    palette="viridis",
    legend=False
)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")

# 3. Histogram - Distribution of sepal width
plt.subplot(2, 2, 3)
plt.hist(df["sepal width (cm)"], bins=15, color="teal", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")

# 4. Scatter plot - Sepal length vs Petal length
plt.subplot(2, 2, 4)
sns.scatterplot(
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species",
    data=df,
    palette="deep"
)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")

# Adjust layout for better readability
plt.tight_layout()

# Save plots to a PNG file instead of showing (WSL-safe)
plt.savefig("iris_visualizations.png")
print("\n✅ Visualizations saved as 'iris_visualizations.png'. Open the file to view the plots.")

# ---------------------------------------------------------------
# Final Insights / Observations
# ---------------------------------------------------------------
print("\n🔍 Key Findings:")
print("- Setosa has the smallest petal measurements, while Virginica has the largest.")
print("- Sepal width is fairly evenly distributed across samples.")
print("- There is a positive correlation between sepal length and petal length.")
print("- Average petal length varies significantly across species, making it a good feature for classification.\n")

print("✅ Analysis complete! Ready for submission.")
