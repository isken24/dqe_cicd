import pytest
from datetime import datetime


@pytest.mark.person
@pytest.mark.parametrize("expected_count", [19614])
def test_row_count(cursor, expected_count):
    """Check row count in Person.Address table"""
    cursor.execute('Select Count(*) from [Person].[Address]')
    records = cursor.fetchall()
    r = records[0][0]
    assert r == expected_count


@pytest.mark.person
def test_max_year(cursor):
    """Check ModifiedDate does not contain future years"""
    today = datetime.today()
    year_today = today.year
    cursor.execute('Select MAX(DATEPART(YEAR, ModifiedDate)) from [Person].[Address]')
    records = cursor.fetchall()
    r = records[0][0]
    assert r <= year_today
