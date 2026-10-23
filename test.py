import matplotlib.pyplot as plt
import pandas as pd

data_file_path = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"

df = pd.read_csv(data_file_path)
# 1. Get value counts and plot
df['Contract'].value_counts().plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])

# 2. Add titles and labels for clarity
plt.title('Distribution of Contract Types', fontsize=14)
plt.xlabel('Contract Type', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)

# 3. Keep the x-axis labels horizontal (optional)
plt.xticks(rotation=0)

# 4. Display the graph
plt.show()