from flask_pymongo import MongoClient


def init_database(app):
    # Initialize the Database Connection
    client = MongoClient(app.config.get("MONGO_URI"))
    db_name = app.config.get("MONGO_DBNAME")
    database = client[db_name]
    print(
        f" * -> Connected to MongoDB Atlas! - DB: {db_name} ")
    # Return mongoDBAtlas client
    return database
