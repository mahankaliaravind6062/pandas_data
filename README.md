# PandasData
Python Package used to deal with pandas and databases like MySQL and MongoDB

## Instalation

```
pip install git+https://github.com/rcourivaud/PandasData.git
```

## Pandas MongoDB

Pandas link to MongoDB databases and collections..


## Pandas MySQL

Different function to deal with MySQL format, tables and procedures and Pandas Dataframes structure.


```
from pandas_mysql import PandasMySQL

pms = PandasMySQL(host, port, usr, pwd)

df = pms.read_table("database_name", "table_name")

```