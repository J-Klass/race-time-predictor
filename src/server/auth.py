import requests


def get_access_token(client_id, client_secret, code):
    # Fetch access token using code
    params = {"client_id": client_id, "client_secret": client_secret, "code": code}
    r = requests.post("https://www.strava.com/oauth/token", params=params)
    data = r.json()

    if "errors" in data:
        return None
    else:
        return data["access_token"]
