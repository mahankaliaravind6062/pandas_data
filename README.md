# pandas_data
Python Package used to deal with pandas and databases like MySQL and MongoDB

## Instalation

```
pip install git+https://github.com/rcourivaud/PandasData.git
```

## Pandas MongoDB
Pandas link to MongoDB databases and collections..

### Import package
```
from pandas_data.pandas_mongodb import PandasMongoDB

pmdb = PandasMongoDB()
```

### Read dataframe from collection
```
df = pmdb.get_dataframe_from_collection(dbs,collection,query_dict)
```

### Insert dataframe into collection
```
pmdb.insert_dataframe_into_collection(dbs, collection, df)
```


## Pandas MySQL
Different function to deal with MySQL format, tables and procedures and Pandas Dataframes structure.

### Import package
```
from pandas_data.pandas_mysql import PandasMySQL

pms = PandasMySQL(host, port, usr, pwd)
```

### Import SQL Table into dataframe
```
df = pms.read_table("database_name", "table_name")
```

###  Upload dataframe to SQL database
```
pms.to_database("database_name", "table_name", df)
```

# pandas_textmining
Handling Text Mining with pandas and sklearn


## TFIDF

```
from pandas_textmining.tfidf_transformer import TfidfHelper

df = pd.DataFrame({'A': [1,2,3,4],
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'E': ["tester train train, train tester test",
                                         "train train trainer train", "test test test",
                                         "train train"],
                    'F': 'foo'})
tf = TfidfHelper()

print(tf.add_tfidf_on_dataframe(df, column_desciption="E", suffix="tf_"))

```
