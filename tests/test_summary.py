from summary import *
from csv_reader import read_csv_file

sample_file = "tests/fixtures/sample_sales.csv"
data = read_csv_file(sample_file)


def test_count_total_revenue_for_one_sale_returns_proper_revenue():
    quantity = 10
    unit_price = 15
    revenue = count_total_revenue_for_one_sale(quantity, unit_price)
    assert revenue == 150


def test_count_total_revenue_for_all_file():
    total_revenue = count_total_revenue_for_all_file(data)
    assert total_revenue == 4648


def test_count_total_orders_for_file_returns_total_orders_count():
    total_orders_count = count_total_orders_for_file(data)
    assert total_orders_count == 12


def test_count_total_units_sold_returns_number_off_all_units():
    total_units_sold = count_total_units_sold(data)
    assert total_units_sold == 38


def test_et_unique_clients_returns_all_unique_clients():
    names_list = ["ACME", "TechPol", "IndustrialPro", "MechaSystems"]
    clients_list = get_unique_clients(data)
    assert set(names_list) == set(clients_list)


def test_get_unique_products_returns_all_unique_products():
    names_list = ["Filter B", "Filter C", "Filter A"]
    products_list = get_unique_products(data)
    assert set(names_list) == set(products_list)


def test_count_total_revenue_per_client():
    test_revenues = {
        "ACME": 851.0,
        "TechPol": 1508.5,
        "IndustrialPro": 1557.5,
        "MechaSystems": 731.0,
    }

    revenues = count_total_revenue_per_client(data)
    assert revenues == test_revenues


def test_count_total_revenue_per_product():
    test_revenues = {
        "Filter A": 1680.0,
        "Filter B": 1440.0,
        "Filter C": 1528.0,
    }

    revenues = count_total_revenues_per_product(data)
    assert revenues == test_revenues


def test_build_summary_data_returns_proper_data():
    expected_summary = {
        "total_revenue": 4648.0,
        "orders_count": 12,
        "units_sold": 38,
        "revenue_per_client": {
            "ACME": 851.0,
            "TechPol": 1508.5,
            "IndustrialPro": 1557.5,
            "MechaSystems": 731.0,
        },
        "revenue_per_product": {
            "Filter A": 1680.0,
            "Filter B": 1440.0,
            "Filter C": 1528.0,
        },
    }
    assert build_summary_data(data) == expected_summary
