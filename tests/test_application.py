from backend import DataAccess


def test_insert():
    data_access = DataAccess()
    prev_size = len(list(data_access.view_all()))
    global new_record
    new_record = data_access.insert("TestCoffee", "4604 West Ox Rd", "Fairfax", "VA", "22030")
    curr_size = len(list(data_access.view_all()))
    assert prev_size + 1 == curr_size


def test_delete():
    data_access = DataAccess()
    prev_size = len(list(data_access.view_all()))
    data_access.delete(new_record)
    curr_size = len(list(data_access.view_all()))
    assert prev_size - 1 == curr_size


def test_search():
    data_access = DataAccess()
    record = data_access.insert("TestCoffee", "4604 West Ox Rd", "Fairfax", "VA", "22030")
    result = data_access.search("TestCoffee")
    data_access.delete(record)
    assert len(list(result)) == 1
