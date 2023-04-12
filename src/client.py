import requests

class Client:
  URL = "https://data.texas.gov/resource/naix-2893.json?location_name=MAX%27S%20WINE%20DIVE"

  def make_request(self):
    response = requests.get(self.URL)
    restaurant_receipts = response.json()
    return restaurant_receipts