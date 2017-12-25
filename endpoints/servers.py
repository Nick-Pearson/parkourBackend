from flask import jsonify

def GET_servers():
    return jsonify(
        [
            {
                "name": "Main Server",
                "IP": "35.176.231.55"
            },
            {
                "name": "Local Server",
                "IP": "127.0.0.1"
            }
        ]
    )