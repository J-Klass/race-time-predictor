import requests


api_url = "https://www.strava.com/api/v3"


def fetch_profile(access_token, athlete_id):
    headers = {"Authorization": "Bearer " + access_token}

    # Fetch athlete profile
    r1 = requests.get(api_url + "/athlete", headers=headers)
    profile = r1.json()

    # Fetch athlete stats
    r2 = requests.get(api_url + "/athletes/{0}/stats".format(athlete_id), headers=headers)
    stats = r2.json()

    return {
        "firstName": profile["firstname"],
        "lastName": profile["lastname"],
        "profileImg": profile["profile_medium"],
        "datePreference": profile["date_preference"],
        "measurementPreference": profile["measurement_preference"],
        "recentRuns": stats["recent_run_totals"],
        "yearRuns": stats["ytd_run_totals"],
        "allRuns": stats["all_run_totals"],
    }
