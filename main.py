import http.client

TOKEN = "xgDvF9YCp0MQuK8X2IqIm88a3KCs0Q1l"

class MercadoLivre:
   def __init__(self):
        self.client = http.client.HTTPSConnection("api.mercadolibre.com")
        self.client.request("GET", "/sites")
        res = self.client.getresponse()
        print(res.read())
            



if __name__ == "__main__":
    client = MercadoLivre()
