import pytest


@pytest.mark.production
def test_unitmeasurecode_len(cursor):
    """Check Unitmeasurecode not longer than 5 symbols"""
    cursor.execute('Select Distinct Unitmeasurecode From [production].[unitmeasure]')
    records = cursor.fetchall()
    codes = [record[0] for record in records]
    rs = [(len(code) < 6) for code in codes]
    assert all([result for result in rs])


@pytest.mark.production
def test_unitmeasure_duplicates(cursor):
    """Check for duplicates in Production.UnitMeasure"""
    cursor.execute("""SELECT  UnitMeasureCode, Name FROM Production.UnitMeasure
                      GROUP BY UnitMeasureCode, Name
                      HAVING Count(*) > 1""")
    rs = cursor.fetchall()
    assert len(rs) == 0
