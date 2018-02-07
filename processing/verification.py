# Crude pre-shared key verification method for leaderboard. Should be OAuth in future.
def verify(challenge):
    if challenge == "***REMOVED***":
        return True
    else:
        return False