import pandas as pd
from pymongo import MongoClient
from tqdm import tqdm


class PandasMongoDB:
    def __init__(self, host="localhost", port=27017, usr=None, pwd=None):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)
        self.usr = usr
        self.pwd = pwd
        self.is_authentificate = {}

    def get_dataframe_from_collection(self, db, col, limit=None, find_query=None):
        if not find_query:
            find_query = {}

        if self.authentificate(db):
            if not limit:
                limit = self.client[db][col].count()
            return pd.DataFrame(list(self.client[db][col].find(find_query).limit(limit)))
        else:
            print("Error on authentification")

    def get_all_collections(self, db):
        if self.authentificate(db):
            return self.client[db].collection_names()
        else:
            print("Error on authentification")

    def insert_one(self, doc, db, col):
        if self.authentificate(db):
            try:
                self.client[db][col].insert_one(doc)
            except Exception as e:
                print(e)
        else:
            print("Error on authentification")

    def authentificate(self, db):
        if not self.usr and not self.pwd or self.is_authentificate.get(db, False):
            return True
        else:
            if self.usr and self.pwd:
                if self.client[db].authenticate(self.usr, self.pwd, mechanism='SCRAM-SHA-1'):
                    self.is_authentificate[db] = True
                    print("Authentified on db :" + db)
                else:
                    self.is_authentificate[db] = False
        return self.is_authentificate[db]

    def insert_dataframe_into_collection(self, db, col, dataframe):
        dataframe["_id"] = dataframe.index
        if self.authentificate(db):
            try:
                self.client[db][col].insert_many(
                    [{k: v for k, v in elt.items() if v} for elt in dataframe.to_dict('records')], ordered=False)
            except Exception as e:
                for r, row in tqdm(dataframe.iterrows()):
                    self.client[db][col].insert_one({k: v for k, v in row.to_dict() if v})
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
