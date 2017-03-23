# PandasData
Python Package used to deal with pandas and databases like MySQL and MongoDB

## Instalation

```
pip install git+https://github.com/rcourivaud/PandasData.git
```

## Pandas MongoDB
Pandas link to MongoDB databases and collections..

### Import package
```
from pandas_mongodb import PandasMongoDB

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
from pandas_mysql import PandasMySQL

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