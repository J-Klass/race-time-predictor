import json


def success(data):
    return json.dumps({"success": True, "data": data}), 200, {"ContentType": "application/json"}


def auth_error(exception):
    return (
        json.dumps({"success": False, "authError": str(exception)}),
        400,
        {"ContentType": "application/json"},
    )


def server_error(exception):
    return (
        json.dumps({"success": False, "serverError": str(exception)}),
        500,
        {"ContentType": "application/json"},
    )
