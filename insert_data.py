import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sales_db"]
collection = db["sales_data"]

collection.delete_many({})  
print("✅ Old data deleted!")

sales_data = [
    {"date": "2025-05-20", "category": "Electronics", "branch": "A", "sales": 150},
    {"date": "2025-05-20", "category": "Clothing", "branch": "A", "sales": 200},
    {"date": "2025-05-21", "category": "Electronics", "branch": "B", "sales": 180},
    {"date": "2025-05-21", "category": "Clothing", "branch": "B", "sales": 250},
    {"date": "2025-05-22", "category": "Electronics", "branch": "A", "sales": 300},
]
collection.insert_many(sales_data)
print("✅ New data inserted successfully!")
