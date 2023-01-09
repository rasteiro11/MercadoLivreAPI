import http.client
import json
from typing import List

import client
import site



TOKEN = "xgDvF9YCp0MQuK8X2IqIm88a3KCs0Q1l"

      

class MercadoLivre:
   def __init__(self):
        self.client = client.HttpClient("api.mercadolibre.com", TOKEN)

   def get_sites(self): 
      return json.load(self.client.do_request("GET", "/sites")) 



if __name__ == "__main__":
   ml_client = MercadoLivre()
   
   sites = ml_client.get_sites()

   for site in sites:
      print(site)
