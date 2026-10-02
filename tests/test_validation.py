from validation import *
from csv_file_repository import read_csv_file

sample_file = "tests/fixtures/sample_sales.csv"
data = read_csv_file(sample_file)


def test_validate_columns_returns_errors_if_missing_column():
    invalid_data = read_csv_file("tests/fixtures/invalid_sales_missing_unit_price.csv")
    assert validate_columns(invalid_data) != []


def test_validate_columns_returns_empty_list_if_columns_ok():
    assert validate_columns(data) == []


def test_validate_quantity_returns_errors_if_quantity_bad():
    invalid_data = read_csv_file("tests/fixtures/invalid_sales_values.csv")
    assert validate_quantity(invalid_data) != []


def test_validate_quantity_returns_empty_list_if_quantity_ok():
    assert validate_quantity(data) == []


def test_validate_unit_price_returns_errors_if_negative():
    invalid_data = read_csv_file(
        "tests/fixtures/invalid_sales_negative_unit_price.csv"
    )
    assert validate_unit_price(invalid_data) != []


def test_validate_unit_price_returns_empty_list_if_valid():
    assert validate_unit_price(data) == []


def test_validate_customer_returns_errors_if_empty():
    invalid_data = read_csv_file("tests/fixtures/invalid_sales_empty_customer.csv")
    assert validate_customer(invalid_data) != []


def test_validate_customer_returns_empty_list_if_all_ok():
    assert validate_customer(data) == []


def test_validate_product_returns_errors_if_empty():
    invalid_data = read_csv_file("tests/fixtures/invalid_sales_empty_product.csv")
    assert validate_product(invalid_data) != []


def test_validate_product_returns_empty_list_if_all_ok():
    assert validate_product(data) == []


def test_validate_file_returns_empty_list_if_all_ok():
    assert validate_file(data) == []


def test_validate_file_returns_errors_if_something_is_bad():
    invalid_data = read_csv_file("tests/fixtures/invalid_sales_mixed_errors.csv")
    assert validate_file(invalid_data) != []


def test_validate_date_returns_empty_if_dates_are_valid():
    assert validate_date(data) == []


def test_validate_date_returns_error_if_date_is_invalid():
    invalid_data = read_csv_file("tests/fixtures/invalid_sales_mixed_errors.csv")
    errors = validate_date(invalid_data)
    assert errors != []
