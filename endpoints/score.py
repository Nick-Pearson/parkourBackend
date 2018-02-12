from flask import jsonify
from flask import request
from processing.verification import verify
from classes.errors import BadRequest
from classes.JSONStatus import Status
from classes.dbTables import LeaderboardTable

def POST_score():
    jsonBody = request.get_json()
    try:
        verify(request.headers.get("Authorization"))
        userScoreArray = jsonBody["scores"]
        minigameId = jsonBody["minigameId"]
        sessionId = jsonBody["sessionId"]
    except KeyError:
        raise BadRequest("Malformed JSON in POST body.")
    except TypeError:
        raise BadRequest("Content-Type: application/json missing in request header.")
    for userScore in userScoreArray:
        try:
            userId = str(userScore[0])
            score = int(userScore[1])
            LeaderboardTable.create(name = userId, score = score, minigameId = int(minigameId), sessionId = int(sessionId))
        except ValueError:
            raise BadRequest("Malformed JSON elements in POST body.")
    return jsonify({
        "status": Status.SUCCESS
    })

def GET_score():
    userScoreArray = []
    minigameId = request.args.get("minigameId")
    sessionId = request.args.get("sessionId")
    users = LeaderboardTable.select()
    try:
        if minigameId is not None:
            minigameId = int(minigameId)
            users = users.where(LeaderboardTable.minigameId == minigameId)
        if sessionId is not None:
            sessionId = int(sessionId)
            users = users.where(LeaderboardTable.sessionId == sessionId)
    except (ValueError):
        raise BadRequest("Malformed query parameters in request")
    for user in users:
        userScoreArray.append([user.name, user.score])
    userScoreArray.sort(key= lambda userScore: userScore[1], reverse=True)
    return jsonify(userScoreArray)