"""Update Handler — optional self-update API.

The DSM UI probes this handler from the About tab.  Some source packages do
not ship self-update metadata, but api.cgi still imports the module eagerly;
without this stub every API request fails before dispatch.
"""


def handle(params):
    action = params.getvalue("action", "")
    if action == "check":
        return {
            "success": True,
            "data": {
                "update_available": False,
                "version": "",
                "notes": "",
                "spk_url": "",
            },
        }
    if action == "install":
        return {
            "success": False,
            "error": {
                "code": 501,
                "message": "Self-update is not available in this build.",
            },
        }
    return {
        "success": False,
        "error": {"code": 101, "message": "Unknown action"},
    }
