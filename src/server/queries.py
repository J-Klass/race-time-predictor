import requests


api_url = "https://www.strava.com/api/v3"


def fetch_profile(access_token, athlete_id):
    """
    Fetch athlete's profile and stats from Strava and combine relevant information into a dict
    :param access_token: User's OAuth 2 access token for the Strava API
    :type access_token: str
    :param athlete_id: User's Strava account ID
    :type athlete_id: str
    :return: profile
    :rtype: dict
    """

    headers = {"Authorization": "Bearer " + access_token}

    # Fetch athlete profile
    r1 = requests.get(api_url + "/athlete", headers=headers)
    profile = r1.json()
    if "errors" in profile:
        raise ValueError(profile["message"])

    # Fetch athlete stats
    r2 = requests.get(api_url + "/athletes/{0}/stats".format(athlete_id), headers=headers)
    stats = r2.json()
    if "errors" in stats:
        raise ValueError(stats["message"])

    return {
        "firstName": profile["firstname"],
        "lastName": profile["lastname"],
        "profileImg": profile["profile_medium"],
        "recentRuns": stats["recent_run_totals"],
        "yearRuns": stats["ytd_run_totals"],
        "allRuns": stats["all_run_totals"],
    }


def fetch_activities(access_token):
    """
    Fetch athlete's activities from Strava
    :param access_token: User's OAuth 2 access token for the Strava API
    :type access_token: str
    :return: activities
    :rtype: list
    """

    headers = {"Authorization": "Bearer " + access_token}

    # Fetch list of athlete's activities
    r = requests.get(api_url + "/athlete/activities", headers=headers)
    activities = r.json()
    if "errors" in activities:
        raise ValueError(activities["message"])

    return activities
