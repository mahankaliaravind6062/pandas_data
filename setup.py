from distutils.core import setup

setup(
    name='pandas_data',
    version='0.1',
    packages=['pandas_data', 'pandas_data.pandas_mysql', 'pandas_data.pandas_mongodb',
              'pandas_textmining.tfidf_transformer'],
    url='',
    license='',
    author='Raphaël Courivaud',
    author_email='',
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
