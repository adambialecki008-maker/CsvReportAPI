import pandas as pd


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
    return errors
