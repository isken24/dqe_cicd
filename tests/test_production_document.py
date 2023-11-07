import pytest


@pytest.mark.production
def test_fileextention_is_valid(cursor):
    """Check FileExtension is valid for all records"""
    cursor.execute('Select Distinct FileExtension From [production].[document]')
    records = cursor.fetchall()
    rs = [record[0] for record in records]
    assert rs == ['', '.doc']


@pytest.mark.production
def test_filename_not_empty(cursor):
    """Check all records have FileName specified"""
    cursor.execute('Select FileName from [production].[document]')
    records = cursor.fetchall()
    rs = [record[0] for record in records]
    assert '' not in rs
