import pytest
import pymssql
from variables import *

"""
@pytest.fixture(scope='module')
def connection_string():
    conn_str = f"server='{SERVER}',user='{USERNAME}',password='{PASSWORD}',database='{DATABASE}',tds_version='{TDS_V}'"

    yield conn_str
"""

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
