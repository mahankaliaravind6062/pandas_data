from distutils.core import setup

setup(
    name='PandasData',
    version='0.1',
    packages=['pandas_data.pandas_mysql', 'pandas_data.pandas_mongodb', 'pandas_textmining.tfidf_transformer'],
    url='',
    license='',
    author='Raphaël Courivaud',
    author_email='r.courivaud@gmail.com',
    description='',
    install_require=[
        'nltk',
        'nltk[punkt]',
        'nltk[stopwords]',
        'sklearn',
        'pandas',
        'pymongo'
    ],
    requires=['nltk', 'sklearn', 'pandas', 'pymongo', 'sqlalchemy']
)
