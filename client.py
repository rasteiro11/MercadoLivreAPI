import http.client

from main import TOKEN

class HttpClient:
   def __init__(self, base_uri, token):
        self.client = http.client.HTTPSConnection(base_uri)
        self.token = ""

   def do_request(self, method, route) -> http.client.HTTPResponse:
      if self.token != "" :
         self.client.request(method, route, "", {"Authorization": "Bearer " + self.token})
      else:
         self.client.request(method, route)
      return self.client.getresponse()

