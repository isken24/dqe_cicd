import pymssql

conn = pymssql.connect(
    server='127.0.0.1',
    user='testlogin',
    password='testPa$$24',
    database='AdventureWorks2012',
    #as_dict=True,
    tds_version='7.0'
)
"""
SERVER = '127.0.0.1'
DATABASE = 'AdventureWorks2012'
USERNAME = 'testlogin'
PASSWORD = 'testPa$$24'
DRIVER = 'ODBC Driver 17 for SQL Server'
"""

SQL_QUERY = """Select Count(*) from [Person].[Address]"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()[0][0]

print(records)


