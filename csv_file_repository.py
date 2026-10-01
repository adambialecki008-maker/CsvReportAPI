import pandas as pd


def read_csv_file(csv_file: str):
    try:
        csv_file = pd.read_csv(csv_file)
        return csv_file
    except Exception as e:
        print(f"Error while reading csv file: {e}")
        return []


def count_total_revenue_for_one_sale(quantity: int, unit_price: float):
    revenue = quantity * unit_price
    return round(revenue, 2)


def count_total_revenue_for_all_file(data):
    rows = data.itertuples()
    total_revenue = 0
    for row in rows:
        total_revenue += count_total_revenue_for_one_sale(row.quantity, row.unit_price)
    return total_revenue


def count_total_orders_for_file(data):
    return len(data)


def count_total_units_sold(data):
    rows = data.itertuples()
    total_units_sold = 0
    for row in rows:
        total_units_sold += row.quantity
    return total_units_sold


def get_unique_clients(data):
    rows = data.itertuples()
    clients_list = []
    for row in rows:
        clients_list.append(row.customer)
    return set(clients_list)


def get_unique_products(data):
    rows = data.itertuples()
    products_list = []
    for row in rows:
        products_list.append(row.product)
    return set(products_list)


def count_total_revenue_per_client(data):
    revenues = {}
    rows = data.itertuples()
    for row in rows:
        client = row.customer
        revenues[client] = revenues.get(client, 0) + count_total_revenue_for_one_sale(
            row.quantity, row.unit_price
        )
    return revenues


def count_total_revenues_per_product(data):
    revenues = {}
    rows = data.itertuples()
    for row in rows:
        product = row.product
        revenues[product] = revenues.get(product, 0) + count_total_revenue_for_one_sale(
            row.quantity, row.unit_price
        )
    return revenues


def validate_columns(data):
    required_columns = ["date", "customer", "product", "quantity", "unit_price"]
    errors = []
    missing_columns = [
        column for column in required_columns if column not in data.columns
    ]
    for column in missing_columns:
        errors.append(f"Missing required column: {column}")
    return errors


def validate_quantity(data):
    rows = data.itertuples()
    errors = []
    for row in rows:
        if row.quantity <= 0 or not float(row.quantity).is_integer():
            errors.append(f"Wrong quantity in row {row.Index + 2}: {row.quantity}")
    return errors


def validate_unit_price(data):
    rows = data.itertuples()
    errors = []
    for row in rows:
        if row.unit_price < 0:
            errors.append(f"Wrong unit_price in row {row.Index+2}: {row.unit_price}")
    return errors


def is_empty_text(value):
    return pd.isna(value) or str(value).strip() == ""


def validate_customer(data):
    rows = data.itertuples()
    errors = []
    for row in rows:
        if is_empty_text(row.customer):
            errors.append(f"Missing customer name in row {row.Index+2}")
    return errors


def validate_product(data):
    rows = data.itertuples()
    errors = []
    for row in rows:
        if is_empty_text(row.product):
            errors.append(f"Missing product name in row {row.Index+2}")
    return errors


def validate_date(data):
    errors = []
    for row in data.itertuples():
        date = pd.to_datetime(
            row.date,
            format="%Y-%m-%d",
            errors="coerce",
        )
        if pd.isna(date):
            errors.append(f"Wrong date in row {row.Index + 2}: {row.date}")
    return errors


def validate_file(data):
    errors = []
    errors.extend(validate_date(data))
    errors.extend(validate_columns(data))
    errors.extend(validate_quantity(data))
    errors.extend(validate_unit_price(data))
    errors.extend(validate_customer(data))
    errors.extend(validate_product(data))
    if errors == []:
        return True
    else:
        return errors
