import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set the style for professional visualizations
sns.set_theme(style="whitegrid")

# --- DATASET 1: Reasons for Dissatisfaction ---
# Insight: 18% of complaints were about preservatives (Potassium Nitrite)
complaints_data = {
    'Reason': ['No Issues', 'Too Much Preservatives', 'Stale Product', 'Damaged', 'Wrong Product'],
    'Percentage': [61, 18, 13, 4, 4]
}
df_complaints = pd.DataFrame(complaints_data)

# Create Chart 1
plt.figure(figsize=(10, 6))
colors = sns.color_palette('pastel')[0:5]
plt.pie(df_complaints['Percentage'], labels=df_complaints['Reason'], autopct='%.0f%%', colors=colors, startangle=140)
plt.title('Customer Feedback: Root Causes of Dissatisfaction', fontsize=14, fontweight='bold')
plt.savefig('chart_dissatisfaction.png') # Saves the image
print("Chart 1 Saved: Root Causes")

# --- DATASET 2: Delivery Efficiency ---
# Insight: 60% of users experience inconsistent delivery times ("Sometimes")
delivery_data = {
    'Response': ['Yes (Quick)', 'Sometimes (Inconsistent)', 'No (Slow)'],
    'Percentage': [35, 60, 5]
}
df_delivery = pd.DataFrame(delivery_data)

# Create Chart 2
plt.figure(figsize=(8, 6))
sns.barplot(x='Response', y='Percentage', data=df_delivery, palette='Blues_d')
plt.title('Operational Analysis: Delivery Speed Consistency', fontsize=14, fontweight='bold')
plt.ylabel('Percentage of Respondents')
plt.ylim(0, 100)
for index, row in df_delivery.iterrows():
    plt.text(index, row.Percentage + 2, f"{row.Percentage}%", color='black', ha="center")
plt.savefig('chart_delivery.png')
print("Chart 2 Saved: Delivery Efficiency")

# --- DATASET 3: Digital Adoption ---
# Insight: 40% of the market is still offline, validating the need for an App
channel_data = {
    'Channel Preference': ['Online', 'Offline'],
    'Percentage': [60, 40]
}
df_channel = pd.DataFrame(channel_data)

# Create Chart 3
plt.figure(figsize=(6, 6))
plt.pie(df_channel['Percentage'], labels=df_channel['Channel Preference'], autopct='%.0f%%', colors=['#66b3ff','#ff9999'])
plt.title('Market Opportunity: Online vs. Offline Preference', fontsize=14, fontweight='bold')
plt.savefig('chart_channel_pref.png')
print("Chart 3 Saved: Digital Adoption")
