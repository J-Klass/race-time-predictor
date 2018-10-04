import json


def success(data):
    return json.dumps({"success": True, "data": data}), 200, {"ContentType": "application/json"}


def error(exception):
    return (
        json.dumps({"success": False, "error": str(exception)}),
        400,
        {"ContentType": "application/json"},
    )
