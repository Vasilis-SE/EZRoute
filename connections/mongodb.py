from pymongo import MongoClient
from pymongo import errors
from datetime import datetime

class MongoDB() :

    def __init__(self):
        self._mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    def connect_to_modes(self):
        today = datetime.today()

        try:
            database = self._mongo_client["transportation"]
            collection = database["modes"]
        except pymongo.errors.ConnectionFailure as e:
            LogErrorOnLogFile(
                "logs/ConnectionErrors/"+today.strftime("%d/%m/%Y"),
                "[" + today.strftime("%H:%M:%S") + "] Could not connect with transportation database! "
            )
        except pymongo.errors.CollectionInvalid as e:
            LogErrorOnLogFile(
                "logs/CollectionErrors/"+today.strftime("%d/%m/%Y"),
                "[" + today.strftime("%H:%M:%S") + "] Could not connect with modes collection! "
            )

        return collection

    def connect_to_means(self):
        today = datetime.today()

        try:
            database = self._mongo_client["transportation"]
            collection = database["means"]
        except pymongo.errors.ConnectionFailure as e:
            LogErrorOnLogFile(
                "logs/ConnectionErrors/"+today.strftime("%d/%m/%Y"),
                "[" + today.strftime("%H:%M:%S") + "] Could not connect with transportation database! "
            )
        except pymongo.errors.CollectionInvalid as e:
            LogErrorOnLogFile(
                "logs/CollectionErrors/"+today.strftime("%d/%m/%Y"),
                "[" + today.strftime("%H:%M:%S") + "] Could not connect with means collection! "
            )

        return collection

    def connect_to_countries(self):
        today = datetime.today()

        try:
            database = self._mongo_client["general"]
            collection = database["countries"]
        except pymongo.errors.ConnectionFailure as e:
            LogErrorOnLogFile(
                "logs/ConnectionErrors/"+today.strftime("%d/%m/%Y"),
                "[" + today.strftime("%H:%M:%S") + "] Could not connect with general database! "
            )
        except pymongo.errors.CollectionInvalid as e:
            LogErrorOnLogFile(
                "logs/CollectionErrors/"+today.strftime("%d/%m/%Y"),
                "[" + today.strftime("%H:%M:%S") + "] Could not connect with countries collection! "
            )

        return collection

    def connect_to_cities(self):
        today = datetime.today()

        try:
            database = self._mongo_client["general"]
            collection = database["cities"]
        except pymongo.errors.ConnectionFailure as e:
            LogErrorOnLogFile(
                "logs/ConnectionErrors/"+today.strftime("%d/%m/%Y"),
                "[" + today.strftime("%H:%M:%S") + "] Could not connect with general database! "
            )
        except pymongo.errors.CollectionInvalid as e:
            LogErrorOnLogFile(
                "logs/CollectionErrors/"+today.strftime("%d/%m/%Y"),
                "[" + today.strftime("%H:%M:%S") + "] Could not connect with cities collection! "
            )

        return collection

    def LogErrorOnLogFile(self, path="", message=""):
        f = open(path, "a+")
        f.write(message + "\n")
        f.close()