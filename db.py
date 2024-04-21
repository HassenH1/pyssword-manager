from pymongo import MongoClient


class Database(MongoClient):
    DB_NAME = "test"
    COLLECTION_NAME = "collection"
    CONNECTION_STRING = "mongodb://host.docker.internal:8000"

    def __init__(self):
        super().__init__()
        self.initalize_db()

    # this is a decorator!!
    def _decorator(callback):
        print("Inside decorator")

        # "self" type problem here
        def closure(self):
            print("start closure", self.COLLECTION_NAME, ">====")
            if self.COLLECTION_NAME is None:
                print("INITIALZING AGAIN!")
                self.initalize_db()
            func = callback(self)
            print("end closure")
            return func

        print("End decorator")
        return closure

    @_decorator
    def initalize_db(self):
        self.connection = MongoClient(self.CONNECTION_STRING)
        self.db = self.connection[self.DB_NAME]
        self.collection = self.db.get_collection(self.COLLECTION_NAME)

    @_decorator
    def get_data(self):
        return list(self.collection.find())

    @_decorator
    def insert_one(self, data: tuple):
        print(data, "<==what is data?")
        self.collection.insert_one(data)


if __name__ == "__main__":
    db = Database()
    data = db.get_data()
    print(data, "<============data at the end?")
