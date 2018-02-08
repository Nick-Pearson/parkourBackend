from flask import jsonify

def GET_servers():
    return jsonify(
        [
            {
                "name": "Main Server",
                "IP": "parkour.ultra-horizon.com"
            },
            {
                "name": "Local Server",
                "IP": "127.0.0.1"
            }
        ]
    )