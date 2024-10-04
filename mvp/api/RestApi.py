import requests
from requests import Response

class RestApi:
    def __init__(self, host:str=""):
        self.host = host
    
    def get_headers() -> dict:
        return {}
    
    def post(self, url:str, headers:dict, params:dict) -> Response:
        response = requests.post(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()