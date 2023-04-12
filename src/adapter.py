from receipt import Receipt
class ReceiptAdapter:
  def select_attributes(self, restaurant_receipt):
      address = restaurant_receipt['location_address']
      end_date = restaurant_receipt['obligation_end_date_yyyymmdd']
      name = restaurant_receipt['location_name']
      total = restaurant_receipt['total_receipts']
      return {'address': address, 'end_date': end_date, 'restaurant_name': name, 'total': total}

  def run(self, restaurant_receipts):
    receipts = []
    for restaurant_receipt in restaurant_receipts:
      receipt_attrs = self.select_attributes(restaurant_receipt) # {}
      # {'address': address, 'end_date': end_date, 'name': name, 'total': total}
      receipt = Receipt(**receipt_attrs)
      receipts.append(receipt)
    return receipts