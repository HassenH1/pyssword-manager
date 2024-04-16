from pymongo import MongoClient


class Database(MongoClient):
    def __init__(self):
        super().__init__()
        self.CONNECTION_STRING = "mongodb://host.docker.internal:8000"
        self.client = MongoClient(self.CONNECTION_STRING)
        self.DB_NAME = "test"

    def get_database(self):
        return self.client[self.DB_NAME]

    def insert_to_database(self, data):
        print(data, "<==what is data?")


# Just testing here
if __name__ == "__main__":
    db = Database()
    data = db.get_database().get_collection("collection").find()
    for doc in data:
        print(doc)
