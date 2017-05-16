import pandas as pd
from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm


class PandasElastic:
    def __init__(self, host=None, hosts=None, usr="elastic", pwd="changeme"):
        self.elastic = Elasticsearch(host=host, hosts=hosts, http_auth=(usr, pwd))

    def index_dataframe(self, df, index_name, doc_type, properties, if_exists="delete"):
        self._create_index(index_name=index_name, properties=properties, if_exists=if_exists)
        bulked_data = self._bulk_data(df=df, index_name=index_name, doc_type=doc_type)
        if self._push_data(bulk=bulked_data, index_name=index_name):
            print("Indexation Done")

    def _create_index(self, index_name, properties, if_exists):
        if if_exists == "delete":
            try:
                self.elastic.indices.delete(index_name)
            except:
                pass

        self.elastic.indices.create(index_name, body=properties)

    def _bulk_data(self, df, index_name, doc_type, how="comprehension"):
        if how == "comprehension":
            bulk_data = [{
                             '_op_type': 'index',
                             '_index': index_name,
                             '_type': doc_type,
                             '_source': doc
                         } for doc in df.to_dict(orient="records")]

        elif how == "iterrows":
            bulk_data = []
            for r, row in tqdm(df.iterrows()):
                try:
                    doc = row.to_dict()
                    data_dict = {
                        '_op_type': 'index',
                        '_index': index_name,
                        '_type': doc_type,
                        '_source': doc
                    }
                    bulk_data.append(data_dict)
                except Exception as e:
                    print(e)
        return bulk_data

    def _push_data(self, bulk, index_name):
        try:
            helpers.bulk(client=self.elastic, actions=bulk)
            self.elastic.indices.refresh()
            print(self.elastic.count(index=index_name))
            return True
        except Exception as e:
            print(e)
            return False
