import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# ✅ Get MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI")
print(MONGO_URI)
# ✅ MongoDB Connection
client = MongoClient(MONGO_URI)
db = client["library_manager"]
collection = db["books"]

# ✅ Function to add book
def add_book(book):
    collection.insert_one(book)

# ✅ Function to get all books
def get_all_books():
    return list(collection.find())  

# ✅ Function to delete a book
def delete_book(title):
    return collection.delete_one({"title": title})

# ✅ Function to search a book
def search_book(title):
    return collection.find_one({"title": title})

# ✅ Function to get statistics
def get_statistics():
    total_books = collection.count_documents({})
    read_books = collection.count_documents({"status": "yes"})
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    return total_books, read_books, read_percentage
