from os import environ

# Import Env variables
MONGO_URI_BASE = environ.get('MONGO_URI_BASE')
MONGO_USER = environ.get('MONGO_USER')
MONGO_PASS = environ.get('MONGO_PASS')
MONGO_CLUSTER = environ.get('MONGO_CLUSTER')
MONGO_DBNAME = environ.get('MONGO_DBNAME')
MONGO_DBOPTIONS = environ.get('MONGO_DBOPTIONS')
# Define Global variables
MONGO_URI = MONGO_URI_BASE + MONGO_USER + MONGO_PASS + \
    MONGO_CLUSTER + MONGO_DBNAME + MONGO_DBOPTIONS
