import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

#Line chart: sales over days
# plt.plot(df["day"], df["sales"], marker='o', linestyle='-', color='blue')
# plt.title("Sales Over Days")
# plt.xlabel("Day")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.show()

#Bar chart: sales over days
# plt.bar(df["day"], df["sales"], color='green')
# plt.title("Sales Over Days")
# plt.xlabel("Day")
# plt.ylabel("Sales")
# plt.show()

# Pie chart: sales by region
# plt.pie(df["sales"], labels=df["region"], autopct='%1.1f%%')
# plt.title("Sales by Region")
# plt.show()

# Histogram: sales distribution
plt.hist(df["sales"], bins=5, color='orange', edgecolor='black')
plt.title("Sales Distribution")
plt.xlabel("Sales Range")
plt.ylabel("Frequency")
plt.show()