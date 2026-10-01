from csv_reader import *

sample_file = "tests/fixtures/sample_sales.csv"
data = read_csv_file(sample_file)


def test_read_csv_file_returns_csv_file():
    test_data = read_csv_file(sample_file)
    assert len(test_data) == 12
