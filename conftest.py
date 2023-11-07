import pytest
import pymssql
from dotenv import load_dotenv


@pytest.fixture(scope='module')
def connection_string():
    load_dotenv()
    conn_str = f"""
                server={SERVER},
                user={USERNAME},
                password={PASSWORD},
                database={DATABASE},
                tds_version={TDS_V}"""

    yield conn_str


@pytest.fixture(scope='module')
def cnxn(connection_string):
    cnxn = pymssql.connect(connection_string)
    yield cnxn
    cnxn.close()


@pytest.fixture
def cursor(cnxn):
    cursor = cnxn.cursor()
    yield cursor
    cursor.close()
