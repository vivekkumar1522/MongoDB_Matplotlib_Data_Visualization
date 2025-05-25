import pymongo
import matplotlib.pyplot as plt
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sales_db"]
collection = db["sales_data"]
data = list(collection.find({}, {"_id": 0, "date": 1, "category": 1, "branch": 1, "sales": 1}))

df = pd.DataFrame(data)

print("Available columns in DataFrame:", df.columns)
print(df.head()) 

if "category" in df.columns:

    category_sales = df.groupby("category")["sales"].sum()
    print("\nAggregated Sales by Category:\n", category_sales)


    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].bar(category_sales.index, category_sales.values, color=['red', 'blue', 'green', 'purple'])
    ax[0].set_title("Total Sales by Category")
    ax[0].set_xlabel("Category")
    ax[0].set_ylabel("Sales")
    ax[1].pie(category_sales.values, labels=category_sales.index, autopct="%1.1f%%", colors=['red', 'blue', 'green', 'purple'])
    ax[1].set_title("Sales Distribution by Category")

    plt.tight_layout()
    plt.show()
else:
    print("\nERROR: 'category' field not found in dataset. Please check MongoDB data insertion.")
