import requests

from .exceptions import AuthError

API_URL = "https://www.strava.com/api/v3"
MAX_ACTIVITIES_PER_PAGE = 200


def fetch_profile(access_token):
    """Fetch athlete's profile from Strava and return relevant information

    :param access_token: User's OAuth 2 access token for the Strava API
    :type access_token: str
    :return: Profile
    :rtype: dict
    """

    headers = {"Authorization": "Bearer " + access_token}

    # Fetch athlete profile
    r = requests.get(API_URL + "/athlete", headers=headers)
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
    r = requests.get(API_URL + "/athletes/{}/stats".format(athlete_id), headers=headers)
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
    activities = []
    page = 1
    while True:
        params = {"per_page": MAX_ACTIVITIES_PER_PAGE, "page": page}
        r = requests.get(API_URL + "/athlete/activities", headers=headers, params=params)
        new_activities = r.json()

        if "errors" in new_activities:
            raise AuthError(new_activities["message"])
        activities.extend(new_activities)

        # Continue fetching activities if necessary
        if len(new_activities) == MAX_ACTIVITIES_PER_PAGE:
            page += 1
        else:
            break

    return activities
