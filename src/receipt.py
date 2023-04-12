class Receipt:
    def __init__(self, total, address, restaurant_name, end_date):
        self.total = int(total)
        self.address = address
        self.restaurant_name = restaurant_name
        self.end_date = end_date