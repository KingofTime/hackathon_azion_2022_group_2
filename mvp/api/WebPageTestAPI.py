import time

from mvp.api import RestApi


class WebPageTestAPI(RestApi):
    def __init__(self, api_key: str):
        super().__init__(host="https://www.webpagetest.org")
        self.api_key = api_key

    def get_headers(self) -> dict:
        return {
            'X-WPT-API-KEY': self.api_key
        }
    
    def run_test(self, url: str, location:str='Dulles:Chrome', connectivity:str='Cable'):
        endpoint = f"{self.host}/runtest.php"
        params = {
            'url': url,
            'location': location,
            'connectivity': connectivity,
            'f': 'json',
            'fvonly': 'true',
            'video': 'false'
        }

        return self.post(endpoint, self.get_headers(), params=params)

    def get_test_result(self, test_id:str):
        endpoint = f"{self.host}/jsonResult.php"
        params = {
            "test":test_id
        }

        while True:
            response = self.get(endpoint, headers=self.get_headers(), params=params)
            if not response:
                print("Failed to get test results.")
                break
            status = response.get('statusCode')
            if status == 200:
                return response
            elif status in [100, 101]:
                print("Waiting for test completion...")
                time.sleep(10)
            else:
                print(f"Test error: Status {status}")
                return None