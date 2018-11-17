import json


def success(data):
    return json.dumps({"success": True, "data": data}), 200, {"ContentType": "application/json"}


def auth_error(exception):
    return (
        json.dumps(
            {"success": False, "errorType": "Authentication error", "error": str(exception)}
        ),
        400,
        {"ContentType": "application/json"},
    )


def server_error(exception):
    return (
        json.dumps({"success": False, "errorType": "Server error", "error": str(exception)}),
        500,
        {"ContentType": "application/json"},
    )
