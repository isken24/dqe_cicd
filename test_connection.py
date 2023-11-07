import pymssql

conn = pymssql.connect(
    server='127.0.0.1',
    user='testlogin',
    password='testPa$$24',
    database='AdventureWorks2012',
    tds_version='7.0')

SQL_QUERY = """Select Count(*) from [Person].[Address]"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

cnt = cursor.fetchall()[0][0]


def test_connection():
    assert cnt == 19614
