import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# fix gender
df['gender'] = df['gender'].str.strip()

# graphs together
plt.figure(figsize=(15,5))

# Graph 1 - Gender
plt.subplot(1,3,1)
df.groupby('gender')['purchase_amount'].sum().plot(kind='bar')
plt.title("Gender Spending")

# Graph 2 - Product Category
plt.subplot(1,3,2)
df['product_category'].value_counts().plot(kind='bar')
plt.title("Product Category")

# Graph 3 - Age vs Spending
plt.subplot(1,3,3)
df.groupby('age')['purchase_amount'].mean().plot()
plt.title("Age vs Spending")

plt.tight_layout()
plt.show()