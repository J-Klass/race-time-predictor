import requests


def get_access_credentials(client_id, client_secret, code):
    """
    Obtain user's access token and ID from Strava authorization server
    :param client_id: Application's OAuth 2 client_id (obtained during app registration)
    :type client_id: str
    :param client_secret: Application's OAuth 2 client_secret (obtained during app registration)
    :type client_secret: str
    :param code: User's OAuth 2 code (returned after successful user sign-in)
    :type code: str
    :return: access_token, user_id
    :rtype: str, str
    """

    # Fetch access token using code
    params = {"client_id": client_id, "client_secret": client_secret, "code": code}
    r = requests.post("https://www.strava.com/oauth/token", params=params)
    data = r.json()

    if "errors" in data:
        raise ValueError(data["message"])

    return data["access_token"], data["athlete"]["id"]
