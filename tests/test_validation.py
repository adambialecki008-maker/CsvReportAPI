from validation import *
from csv_reader import read_csv_file

sample_file = "tests/fixtures/sample_sales.csv"
data = read_csv_file(sample_file)


def test_validate_columns_returns_errors_if_missing_column():
    no_valid_data = read_csv_file("tests/fixtures/invalid_sales_missing_unit_price.csv")
    assert validate_columns(no_valid_data) != []


def test_validate_columns_returns_empty_list_if_columns_ok():
    assert validate_columns(data) == []


def test_validate_quantity_returns_errors_if_quantity_bad():
    no_valid_data = read_csv_file("tests/fixtures/invalid_sales_values.csv")
    assert validate_quantity(no_valid_data) != []


def test_validate_quantity_returns_empty_list_if_quantity_ok():
    assert validate_quantity(data) == []


def test_validate_unit_price_returns_errors_if_its_lower_equal_0():
    no_valid_data = read_csv_file(
        "tests/fixtures/invalid_sales_negative_unit_price.csv"
    )
    assert validate_unit_price(no_valid_data) != []


def test_validate_unit_price_returns_empty_list_if_its_higher_than_0():
    assert validate_unit_price(data) == []


def test_validate_customer_returns_errors_if_any_mepty():
    no_valid_data = read_csv_file("tests/fixtures/invalid_sales_empty_customer.csv")
    assert validate_customer(no_valid_data) != []


def test_validate_customer_returns_empty_list_if_all_ok():
    assert validate_customer(data) == []


def test_validate_product_returns_errors_if_any_mepty():
    no_valid_data = read_csv_file("tests/fixtures/invalid_sales_empty_product.csv")
    assert validate_product(no_valid_data) != []


def test_validate_product_returns_empty_list_if_all_ok():
    assert validate_product(data) == []


def test_validate_file_returns_true_if_all_ok():
    assert validate_file(data) == True


def test_validate_file_returns_errors_if_something_is_bad():
    no_valid_data = read_csv_file("tests/fixtures/invalid_sales_mixed_errors.csv")
    assert validate_file(no_valid_data) != []


def test_validate_date_returns_errors_if_date_is_wrong():
    pass


def test_valdiate_date_returns_empty_if_date_is_ok():
    assert validate_date(data) == []


def test_validate_date_returns_no_errors_if_dates_ok():
    assert validate_date(data) == []


def test_validate_date_returns_error_if_date_bad():
    no_valid_data = read_csv_file("tests/fixtures/invalid_sales_mixed_errors.csv")
    errors = validate_date(no_valid_data)
    assert errors != []
