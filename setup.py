from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pandas_data',
    version='0.1',
    packages=['pandas_data', 'pandas_data.pandas_mysql', 'pandas_data.pandas_mongodb',
              'pandas_data.pandas_textmining', "pandas_data.pandas_elasticsearch"],
    url='',
    license='',
    author='Raphaël Courivaud',
    author_email='',
    description='',
    install_require=required + [
        'nltk[punkt]',
        'nltk[stopwords]',
    ],
    requires=['nltk', 'sklearn', 'pandas', 'pymongo', 'sqlalchemy']
)
