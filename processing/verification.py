from classes.errors import Unauthorized

# Crude pre-shared key verification method for leaderboard. Should be OAuth in future.
def verify(challenge):
    if challenge == "***REMOVED***":
        return
    else:
        raise Unauthorized("Invalid pre-shared key")