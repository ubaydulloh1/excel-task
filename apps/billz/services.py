import requests


class BillzApiService:
    def __init__(self):
        self.jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfcGxhdGZvcm1faWQiOiI3ZDRhNGMzOC1kZDg0LTQ5MDItYjc0NC0wNDg4YjgwYTRjMDEiLCJjb21wYW55X2lkIjoiNGI3ZjU0MDYtNTI2NS00YmVmLTk5NWQtZGM4MzdlZTQyMTc2IiwiZGF0YSI6IiIsImV4cCI6MTcxNTAxMDMzMCwiaWF0IjoxNzEzNzE0MzMwLCJpZCI6IjY4NDdjN2FjLThiNTAtNGI4Zi04Yzk1LWZkMjcxMzI5NTc3NSIsInVzZXJfaWQiOiI3ZDYzZmRlNi1mM2QyLTRmNWUtOTAwOS1iZWNiNWMwMThkNjAifQ.mMUfLGFH47pBSr2AEn4p57mZOt1DOV_f8GbQZk9ZEOE"
        self.headers = {
            "Authorization": "Bearer {}".format(self.jwt_token)
        }
        self.BASE_URL = "https://api-admin.billz.ai"

    def renew_token(self):
        pass

    def fetch_base(self, endpoint) -> (bool, dict):
        url = self.BASE_URL + endpoint

        try:
            resp = requests.get(url=url, headers=self.headers, timeout=7)
        except (requests.ConnectionError, requests.Timeout) as e:
            return False, {"error": e}

        try:
            data = resp.json()
        except requests.JSONDecodeError as e:
            return False, {"error": e}

        return True, data

    def fetch_product_categories(self):
        endpoint = "/v2/category?is_deleted=false"
        return self.fetch_base(endpoint=endpoint)

    def fetch_products(self):
        endpoint = "/v2/products"
        return self.fetch_base(endpoint=endpoint)

    def fetch_brands(self):
        endpoint = "/v2/brand"
        return self.fetch_base(endpoint=endpoint)

    def fetch_shops(self):
        endpoint = "/v1/shop"
        return self.fetch_base(endpoint=endpoint)

    def fetch_measurement_units(self):
        endpoint = "/v1/measurement_unit"
        return self.fetch_base(endpoint=endpoint)
