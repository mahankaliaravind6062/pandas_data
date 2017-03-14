from pandas.io import sql
import pandas as pd
from sqlalchemy import create_engine


class PandasMySQL:
    def __init__(self, host="localhost", port=3306, usr="root", pwd=""):
        """
        :param host: MySQL Host
        :param port:
        :param usr:
        :param pwd:
        """
        self.host = host
        self.port = port
        self.user = usr
        self.pwd = pwd
        print("MySQL url : pandas_mysql://{0}:{1}@{2}:{3}".format(self.user, self.pwd, self.host, self.port))

    def execute_stored_procedure(self, proc_name, params, base):
        """
        Excecute stored procedure on table selected with some parameters

        :param proc_name:
        :param params:
        :param base:
        :return:
        """
        conn = self.connect_to_database(db=base)
        connection = conn.connect()
        result = connection.execute(proc_name, params)
        connection.close()
        return result

    def connect_to_database(self, db):
        """
        Connect to MySQL Database and return engine to use it in pandas librairy

        :param db:
        :return:
        """
        engine = create_engine(
            'pandas_mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(self.user, self.pwd, self.host,
                                                                             str(self.port), db), echo=False)
        return engine

    def open_csv_file(self, path, **args):
        """
        :param path:
        :param args:
        :return:
        """
        return pd.read_csv(path, args)

    def read_table(self, db, table_name):
        """
        Read table from database
        :param db:
        :param table_name:
        :return: Pandas dataframe
        """
        engine = self.connect_to_database(db=db)
        return pd.read_sql_table(table_name=table_name, con=engine)

    def to_csv(self, dataframe, file_path, encoding="utf-8", index=False):
        """
        :param dataframe:
        :param file_path:
        :return:
        """
        dataframe.to_csv("./" + file_path, encoding=encoding, index=index, )

    def to_database(self, dataframe, name, db, if_exists, chunksize=50e3, dtypes={}):
        """
        :param dataframe:
        :param name:
        :param db:
        :param if_exists:
        :param chunksize:
        :param dtypes:
        :return:
        """

        conn = self.connect_to_database(db=db)
        if dataframe.shape[0] != 0:
            print(
                "Writing to table : " + name + " and database : " + db + " if exists : " + if_exists + " shape : " + str(
                    dataframe.shape))
        dataframe.to_sql(name=name, con=conn, if_exists=if_exists, chunksize=chunksize, dtype=dtypes)

    def drop_table(self, name, db):
        """
        Drop selected Table

        :param name:
        :param db:
        :return:
        """
        conn = self.connect_to_database(db=db)
        print("Drop table : " + name + " and database : " + db)
        sql.execute('DROP TABLE IF EXISTS %s' % name, conn)
