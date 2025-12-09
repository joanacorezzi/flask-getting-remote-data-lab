import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):

        response = requests.get(self.url)  # make the HTTP request
        return response.content             # return the response body as a string


    def load_json(self):
        
        body = self.get_response_body()    # get the raw text from the API
        data = json.loads(body)            # convert JSON text into Python data
        return data                        # return the Python object 