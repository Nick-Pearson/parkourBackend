from classes.errors import Unauthorized
import os

# Crude pre-shared key verification method for leaderboard. Should be OAuth in future.
def verify(challenge):
    if challenge == os.environ['PASSWORD']:
        return
    else:
        raise Unauthorized("Invalid pre-shared key")