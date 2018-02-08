from flask import jsonify
from flask import request
from processing.verification import verify
from classes.errors import BadRequest
from classes.JSONStatus import Status
from classes.dbTables import LeaderboardTable

def POST_score():
    userScoreArray = request.get_json()
    try:
        verify(request.headers.get("Authorization"))
    except KeyError:
        raise BadRequest("Malformed JSON in POST body")
    for userScore in userScoreArray:
        userId = userScore[0]
        score = userScore[1]
        LeaderboardTable.create(name = userId, score = score)
    return jsonify({
        "status": Status.SUCCESS
    })

def GET_score():
    userScoreArray = []
    users = LeaderboardTable.select()
    for user in users:
        userScoreArray.append([user.name, user.score])
    userScoreArray.sort()
    return jsonify(userScoreArray)