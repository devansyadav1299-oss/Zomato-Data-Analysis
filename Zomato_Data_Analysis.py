# ==============================================================================
# STEP 1: SET UP THE ENVIRONMENT AND IMPORT NECESSARY LIBRARIES
# ==============================================================================
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
# In notebooks, plots are displayed with the explicit ``plt.show()`` calls below.
# Configure inline plot rendering and default style mechanics
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 5)

# ==============================================================================
# STEP 2: LOAD THE DATASET
# ==============================================================================
# Load dataset into a Pandas DataFrame
# Load the dataset relative to this script so it works from any working directory.
data_path = Path(__file__).resolve().parents[1] / 'data' / 'Zomato data .csv'
df = pd.read_csv(data_path, encoding='cp1252')

print("--- Initial Data Info ---")
print(df.info())
print("\n--- First 5 Rows ---")
print(df.head())
# ==============================================================================
# STEP 3: CLEAN AND PREPARE THE DATA
# ==============================================================================
print("\n--- Step 3.1: Unique Values in Rate Column Before Cleansing ---")
print(df['rate'].unique()[:5])

# 1.) Convert Ratings: Strip spaces, strip "/5", and cast to floating point
df['rate'] = df['rate'].astype(str).str.strip()
df['rate'] = df['rate'].str.split('/').str[0]
df['rate'] = df['rate'].astype(float)

# Cleansing data transformations for cost columns for downstream analysis metrics
df['approx_cost(for two people)'] = (
    df['approx_cost(for two people)']
    .astype(str)
    .str.replace(',', '', regex=False)
    .astype(float)
)

# 2.) Verify Data Types and Null Signatures
print("\n--- Step 3.2: Column Data Types and Null Overview ---")
print(df.info())

# 3.) Conclusion
print("\n--- Step 3.3: Total Null Assertions Per Feature Column ---")
null_counts = df.isnull().sum()
print(null_counts)
assert null_counts.sum() == 0, "Warning: Unhandled missing indicators found in dataset!"
print("\nConclusion: Verified. There are no null values present in the cleaned data matrix.")

# ==============================================================================
# STEP 4: DATA ANALYSIS AND VISUALIZATION
# ==============================================================================

# ------------------------------------------------------------------------------
# Analysis 1: Types of Restaurants
# ------------------------------------------------------------------------------
plt.figure(figsize=(10, 5))
sns.countplot(
    y='listed_in(type)',
    data=df,
    order=df['listed_in(type)'].value_counts().index,
    palette='Set2'
)
plt.title("Distribution of Restaurant Types")
plt.xlabel("Count")
plt.ylabel("Restaurant Type")
plt.tight_layout()
plt.show()

print("\n--- Analysis 1 Metrics: Numerical Breakdown ---")
print(df['listed_in(type)'].value_counts())
print("Conclusion: Dining is the most common restaurant type preferred by customers.")

# ------------------------------------------------------------------------------
# Analysis 2: Votes by Restaurant Type
# ------------------------------------------------------------------------------
votes_by_type = df.groupby('listed_in(type)')['votes'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
votes_by_type.plot(kind='bar', color='#4C72B0')
plt.title("Total Votes by Restaurant Type")
plt.xlabel("Restaurant Type")
plt.ylabel("Aggregate Votes Received")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Analysis 3: Ratings Distribution
# ------------------------------------------------------------------------------
plt.figure(figsize=(8, 4))
sns.histplot(df['rate'], bins=15, kde=True, color='purple')
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating (Out of 5)")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()
print("Conclusion: The majority of restaurants fall into the rating bracket of 3.5 to 4.0.")

# ------------------------------------------------------------------------------
# Analysis 4: Restaurant Cost Preference for Couples
# ------------------------------------------------------------------------------
plt.figure(figsize=(10, 4))
sns.countplot(x='approx_cost(for two people)', data=df, palette='viridis')
plt.title("Approximate Dining Cost Distribution for Couples")
plt.xlabel("Cost for Two People")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Analysis 5: Online vs. Offline Ratings
# ------------------------------------------------------------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(x='online_order', y='rate', data=df, palette='Pastel1')
plt.title("Ratings Distribution: Online vs. Offline Orders")
plt.xlabel("Offers Online Ordering")
plt.ylabel("Rating Metric")
plt.tight_layout()
plt.show()
print("Conclusion: Restaurants offering online delivery channels receive higher average ratings.")

# ------------------------------------------------------------------------------
# Analysis 6: Online Orders by Restaurant Type
# ------------------------------------------------------------------------------
pivot_online_type = pd.pivot_table(
    df,
    index='listed_in(type)',
    columns='online_order',
    values='name',
    aggfunc='count',
    fill_value=0
)

plt.figure(figsize=(8, 5))
sns.heatmap(pivot_online_type, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Volume Heatmap: Online vs. Offline Orders by Business Type")
plt.xlabel("Online Ordering Channel")
plt.ylabel("Restaurant Business Type")
plt.tight_layout()
plt.show()
print("Conclusion: Cafes prefer online order infrastructure, while Dining relies on offline channels.")

# ==============================================================================
# SECTION 7: CORE TARGETED INSIGHT RECOVERY
# ==============================================================================
print("\n==============================================================================")
print("                           ZOMATO PROJECT KEY INSIGHTS                        ")
print("==============================================================================")

# 1.) Majority Ordering Profile
majority_order_type = df[df['online_order'] == 'Yes']['listed_in(type)'].value_counts().idxmax()
print(f"1.) Majority Customer Order Target Category: {majority_order_type}")

# 2.) Aggregate Voting Volume Table
print("\n2.) Aggregate Voting Volume Across Ecosystem Vectors:")
for rest_type, votes in votes_by_type.items():
    print(f"    - {rest_type}: {votes:,} votes")

# 3.) Dominant Rating Tiers
bins = [0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
labels = ["<2.5", "2.5-3.0", "3.0-3.5", "3.5-4.0", "4.0-4.5", "4.5-5.0"]
df['rating_range'] = pd.cut(df['rate'], bins=bins, labels=labels, include_lowest=True)
dominant_rating_tier = df['rating_range'].value_counts().idxmax()
print(f"\n3.) Dominant Restaurant Rating Concentration Tier: {dominant_rating_tier}")

# 4.) Couple Spending Average Matrix
avg_couple_spend = df[df['online_order'] == 'Yes']['approx_cost(for two people)'].mean()
print(f"\n4.) Average Online Order Basket Value Spent by Couples: ${avg_couple_spend:.2f}")

# 5.) Maximized Operational Rating Mode
max_mode_rating = df.groupby('online_order')['rate'].mean().idxmax()
print(f"5.) Delivery Mode Securing Maximum Statistical Rating Average: {max_mode_rating} Delivery")

# 6.) Target Promotion Recommendations for Disconnected Venues
target_offline_promo = df[df['online_order'] == 'No']['listed_in(type)'].value_counts().idxmax()
print(f"6.) Target Venue Vector for Direct Promotion Interventions: {target_offline_promo}")
print("==============================================================================")
