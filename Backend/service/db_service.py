from pymongo import MongoClient

# establing connection
try:
    connect = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# connecting or switching to the database
db = connect.demoDB

# creating or switching to demoCollection
collection = db.demoCollection


def init_db():
    print("Hello World!")

    # personOne = {"name": "Mustafa Sidiqi", "age": 23}
    # psersonTwo = {"name": "Musti", "age": 25}
    # # Inserting both document one by one
    # collection.insert_one(personOne)
    # collection.insert_one(psersonTwo)

    # Printing the data inserted
    cursor = collection.find()
    for record in cursor:
        print(record)

def get_user(id):
    pass

def get_book(id): 
    pass

def get_user_books(user_id):
    pass

def book_query(title, id, isbn):
    pass 
