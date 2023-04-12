from client import Client
from receipt import Receipt
from adapter import ReceiptAdapter

client = Client()
restaurant_receipts = client.make_request()
receipts = ReceiptAdapter().run(restaurant_receipts)

