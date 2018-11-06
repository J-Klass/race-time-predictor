import requests

from server.exceptions import AuthError

api_url = "https://www.strava.com/api/v3"


def fetch_profile(access_token):
    """Fetch athlete's profile from Strava and return relevant information

    :param access_token: User's OAuth 2 access token for the Strava API
    :type access_token: str
    :return: Profile
    :rtype: dict
    """

    headers = {"Authorization": "Bearer " + access_token}

    # Fetch athlete profile
    r = requests.get(api_url + "/athlete", headers=headers)
    profile = r.json()
    if "errors" in profile:
        raise AuthError(profile["message"])

    return {
        "firstName": profile["firstname"],
        "lastName": profile["lastname"],
        "imgUrl": profile["profile"],
        "profileUrl": "https://www.strava.com/athletes/{}".format(profile["id"]),
    }


def fetch_stats(access_token, athlete_id):
    """Fetch athlete's stats from Strava and return relevant information

    :param access_token: User's OAuth 2 access token for the Strava API
    :type access_token: str
    :param athlete_id: User's Strava account ID
    :type athlete_id: str
    :return: Stats
    :rtype: dict
    """

    headers = {"Authorization": "Bearer " + access_token}

    # Fetch athlete stats
    r = requests.get(api_url + "/athletes/{}/stats".format(athlete_id), headers=headers)
    stats = r.json()
    if "errors" in stats:
        raise AuthError(stats["message"])

    return {
        "recentRuns": stats["recent_run_totals"],
        "yearRuns": stats["ytd_run_totals"],
        "allRuns": stats["all_run_totals"],
    }


def fetch_activities(access_token):
    """Fetch athlete's activities from Strava

    :param access_token: User's OAuth 2 access token for the Strava API
    :type access_token: str
    :return: Activities
    :rtype: list
    """

    headers = {"Authorization": "Bearer " + access_token}

    # Fetch list of athlete's activities
    r = requests.get(api_url + "/athlete/activities", headers=headers)
    activities = r.json()
    if "errors" in activities:
        raise AuthError(activities["message"])

    return activities
