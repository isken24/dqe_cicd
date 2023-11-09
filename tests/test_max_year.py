from datetime import datetime


def test_max_year(cursor):
    """Check ModifiedDate does not contain future years"""
    today = datetime.today()
    year_today = today.year
    cursor.execute('Select MAX(DATEPART(YEAR, ModifiedDate)) from [Person].[Address]')
    records = cursor.fetchall()
    r = records[0][0]
    assert r <= year_today
