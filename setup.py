from distutils.core import setup

setup(
    name='PandasData',
    version='0.1',
    packages=['pandas_mysql', 'pandas_mongodb'],
    url='',
    license='Raphaël Courivaud',
    author='Raphaël Courivaud',
    install_requirement=[
        'pandas',
        'sqlalchemy',
        'pymongo',
        "https://github.com/rcourivaud/PandasData"
    ],
    author_email='r.courivaud@gmail.com',
    description='Python library used to deal with database and python pandas', requires=['pandas', 'pymongo',
                                                                                         'sqlalchemy']
)
