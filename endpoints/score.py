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
        playerName = str(jsonBody["playerName"])
        goals = int(jsonBody["goals"])
        ownGoals = int(jsonBody["ownGoals"])
        gameOutcome = str(jsonBody["gameOutcome"])
        if not (gameOutcome in ["W", "D", "L"]):
            raise KeyError
    except KeyError:
        raise BadRequest("Malformed JSON in POST body.")
    except TypeError:
        raise BadRequest("Content-Type: application/json missing in request header.")
    except ValueError:
        raise BadRequest("Goals or OwnGoals should be of integer type!")
    player, created = LeaderboardTable.get_or_create(playerName=playerName.lower(),
                                                     defaults={'goals': 0, 'ownGoals': 0,
                                                               "gamesWon": 0, "gamesDrawn": 0, "gamesLost": 0})
    if created:
        player.displayName = playerName
    print (player.goals)
    player.goals += goals
    player.ownGoals += ownGoals
    if gameOutcome == "W":
        player.gamesWon += 1
    elif gameOutcome == "D":
        player.gamesDrawn += 1
    elif gameOutcome == "L":
        player.gamesLost += 1
    player.save()

    return jsonify({
        "status": Status.SUCCESS
    })

def GET_score():
    playerScoreArray = []
    players = LeaderboardTable.select()
    for player in players:
        score = player.goals * 6
        score += player.ownGoals * -6
        score += player.gamesWon * 3
        score += player.gamesDrawn
        playerScoreArray.append([player.displayName, score])
    playerScoreArray.sort(key= lambda player: player[1], reverse=True)
    return jsonify(playerScoreArray[:10])