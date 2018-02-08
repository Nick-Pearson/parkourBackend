from flask import jsonify
from flask import request
from processing.verification import verify
from classes.errors import BadRequest
from classes.JSONStatus import Status

def POST_score():
    body = request.get_json()
    try:
        verify(request.headers.get("Authorization"))
        # DO DB Interaction here...
    except KeyError:
        raise BadRequest("Malformed JSON in POST body")
    return jsonify({
        "status": Status.SUCCESS
    })