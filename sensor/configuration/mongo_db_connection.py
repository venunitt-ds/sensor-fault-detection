import pymongo
from sensor.constants.database import DATABASE_NAME
import certifi
ca = certifi.where()
class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://venuplla:venu2023@ineuron.8x1bgv4.mongodb.net/?retryWrites=true&w=majority"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            #print(self.database.list_collection_names())
            
        except Exception as e:
            raise e

