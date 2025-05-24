import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv(r'C:\Users\dell\OneDrive\Desktop\daily_activity.csv')

# Set correct day order
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Group by day of the week
avg_data = df.groupby('dotw')[['total_steps', 'calories']].mean().reindex(days_order)

# Plot side-by-side bar chart
x = np.arange(len(days_order))
width = 0.35

plt.figure(figsize=(10,6))
plt.bar(x - width/2, avg_data['total_steps'], width, label='Average Steps', color='skyblue')
plt.bar(x + width/2, avg_data['calories'], width, label='Average Calories Burned', color='orange')

plt.xlabel('Day of the Week')
plt.ylabel('Average')
plt.title('Average Steps and Calories Burned by Day')
plt.xticks(x, days_order, rotation=45)
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()




