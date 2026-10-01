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


def build_summary_data(data):
    summary_data = {
        "total_revenue": count_total_revenue_for_all_file(data),
        "orders_count": count_total_orders_for_file(data),
        "units_sold": count_total_units_sold(data),
        "revenue_per_client": count_total_revenue_per_client(data),
        "revenue_per_product": count_total_revenues_per_product(data),
    }

    return summary_data
