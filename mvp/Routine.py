from mvp.api import WebPageTestAPI


class Routine:
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def __call__(self, link:str):
        print(link)
        api = WebPageTestAPI(self.api_key)
        print(api.run_test(link))