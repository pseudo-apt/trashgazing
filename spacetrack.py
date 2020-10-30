import json
import requests

base_url = "https://space-track.org"

class SpaceTrackClient():

    def __init__(self, api_user, api_password):
        """Initialize the client"""
        self.api_user = api_user
        self.api_password = api_password
        self.session = requests.Session()

    def authenticate(self):
        login_url = f"{base_url}/ajaxauth/login"
        login_data = {"identity": self.api_user, "password": self.api_password}
        resp = self.session.post(url=login_url, data=login_data)

        if resp.status_code != 200:
            raise Exception(f"Login failed: HTTP {resp.status_code}, {resp.text}")

    def get_space_debris(self):
        tle_url = f"{base_url}/basicspacedata/query/class/tle_latest/OBJECT_TYPE/DEBRIS/orderby/ORDINAL%20asc/emptyresult/show"
        resp = self.session.get(tle_url)

        if resp.status_code != 204:
            raise Exception(f"Couldn't complete request: HTTP {resp.status_code}, {resp.text}")

        return resp.text

    def close(self):
        logout_url = f"{base_url}/ajaxauth/logout"
        resp = self.session.post(logout_url)
        
        if resp.status_code != 200:
            raise Exception(f"Logout failed: HTTP {resp.status_code}, {resp.text}")