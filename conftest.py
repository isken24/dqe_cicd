import pytest
import pymssql


@pytest.fixture(scope='module')
def cnxn():
    cnxn = pymssql.connect(server='host.docker.internal',
    user='testlogin',
    password='testPa$$24',
    database='AdventureWorks2012',
    tds_version='7.0')
    yield cnxn
    cnxn.close()


@pytest.fixture
def cursor(cnxn):
    cursor = cnxn.cursor()
    yield cursor
    cursor.close()
