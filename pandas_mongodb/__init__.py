from pymongo import MongoClient
import pandas as pd


class PandasMongoDB:
    def __init__(self, host="localhost", port=27017, usr=None, pwd=None):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)
        self.usr = usr
        self.pwd = pwd

    def get_dataframe_from_collection(self, db, col, find_query=None):
        if find_query is None:
            find_query = {}
        if self.usr and self.pwd:
            self.client[db].authenticate(self.usr, self.pwd, mechanism='SCRAM-SHA-1')
        return pd.DataFrame(list(self.client[db][col].find(find_query)))

    def insert_dataframe_into_collection(self, db, col, dataframe):
        if self.usr and self.pwd:
            self.client[db].authenticate(self.usr, self.pwd, mechanism='SCRAM-SHA-1')
        self.client[db][col].insert_many(dataframe.to_dict('records'))

    def delete_element_from_collection(self, db, col, find_query=None):
        if find_query is None:
            find_query = {}
        if self.usr and self.pwd:
            self.client[db].authenticate(self.usr, self.pwd, mechanism='SCRAM-SHA-1')
        result = self.client[db][col].delete_many(find_query)
        print("Remove {} element in {}.{}".format(str(result.deleted_count), db, col))
        return result

    def drop_collection(self, db,col):
        self.client[db].drop_collection(col)

    def drop_database(self, db):
        self.client.drop_database(db)





