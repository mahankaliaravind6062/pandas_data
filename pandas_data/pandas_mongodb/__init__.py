import pandas as pd
from pymongo import MongoClient


class PandasMongoDB:
    def __init__(self, host="localhost", port=27017, usr=None, pwd=None):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)
        self.usr = usr
        self.pwd = pwd
        self.is_authentificate = {}

    def get_dataframe_from_collection(self, db, col, find_query=None):
        if find_query is None:
            find_query = {}

        if self.authentificate(db):
            return pd.DataFrame(list(self.client[db][col].find(find_query)))
        else:
            print("Error on authentification")

    def get_all_collections(self, db):
        if self.authentificate(db):
            return self.client.db.collections_names()
        else:
            print("Error on authentification")

    def authentificate(self, db):
        if self.is_authentificate.get(db, False):
            return True
        else:
            if self.usr and self.pwd:
                if self.client[db].authenticate(self.usr, self.pwd, mechanism='SCRAM-SHA-1'):
                    self.is_authentificate[db] = True
                    return True
                else:
                    self.is_authentificate[db] = False
        return False

    def insert_dataframe_into_collection(self, db, col, dataframe):
        if self.authentificate(db):
            self.client[db][col].insert_many(dataframe.to_dict('records'))
        else:
            print("Error on authentification")

    def delete_element_from_collection(self, db, col, find_query=None):
        if find_query is None:
            find_query = {}
        if self.authentificate(db):
            result = self.client[db][col].delete_many(find_query)
            print("Remove {} element in {}.{}".format(str(result.deleted_count), db, col))
            return result
        else:
            print("Error on authentification")

    def drop_collection(self, db, col):
        if self.authentificate(db):
            self.client[db].drop_collection(col)

    def drop_database(self, db):
        if self.authentificate(db):
            self.client.drop_database(db)
