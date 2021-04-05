import json
import requests

base_url = "https://space-track.org"

class SpaceTrackClient():
    """
        Client to interface with space-track.org
    """
    def __init__(self, api_user, api_password):
        """ Initialize the client """
        self.api_user = api_user
        self.api_password = api_password
        self.session = requests.Session()

    def authenticate(self):
        """ Authenticate the user """
        login_url = f"{base_url}/ajaxauth/login"
        login_data = {"identity": self.api_user, "password": self.api_password}
        resp = self.session.post(url=login_url, data=login_data)

        if resp.status_code != 200:
            raise Exception(f"Login failed: HTTP {resp.status_code}, {resp.text}")

    def get_space_debris(self):
        """ Retrieve space debris positions using the tle_latest dataset """
        tle_url = f"{base_url}/basicspacedata/query/class/tle_latest/ORDINAL/1/EPOCH/>now-1/orderby/NORAD_CAT_ID/format/json"
        resp = self.session.get(tle_url)

        if resp.status_code != 200:
            raise Exception(f"Couldn't complete request: HTTP {resp.status_code}")

        return resp.text

    def close(self):
        """ Send a logout request """
        logout_url = f"{base_url}/ajaxauth/logout"
        resp = self.session.get(logout_url)
        
        if resp.status_code != 200:
            raise Exception(f"Logout failed: HTTP {resp.status_code}, {resp.text}")
