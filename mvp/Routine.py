from mvp.api import WebPageTestAPI


class Routine:
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def __call__(self, link:str):
        api = WebPageTestAPI(self.api_key)
        response = api.run_test(link)
        response_data = response.get("data")
        if response_data:
            test_id = response_data.get("testId")
            test_result = api.get_test_result(test_id)
