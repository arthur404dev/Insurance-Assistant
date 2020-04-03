from flask_pymongo import pymongo


def create_database(app):
    # Initialize the Database Connection
    client = pymongo.MongoClient(app.config.get("MONGO_URI"))
    db_name = app.config.get("MONGO_DBNAME")
    print(
        f" * -> Connected to MongoDB Atlas! - DB: {db_name} ")
    # Return mongoDBAtlas client
    return client
