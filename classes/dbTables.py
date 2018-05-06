import peewee as pw
from peewee import *
import os

# Define and connect to the API database
parkourDB = pw.MySQLDatabase("parkour", host=os.environ['RDS_HOSTNAME'], port=int(os.environ['RDS_PORT']), user=os.environ['RDS_USERNAME'], passwd=os.environ['RDS_PASSWORD'])
parkourDB.connect()
parkourDB.close()

class ParkourModel(Model):
    class Meta:
        database = parkourDB

class LeaderboardTable(ParkourModel):
    playerName = CharField(primary_key=True)
    displayName = CharField()
    goals = IntegerField()
    ownGoals = IntegerField()
    gamesWon = IntegerField()
    gamesDrawn = IntegerField()
    gamesLost = IntegerField()
    class Meta:
        db_table = "leaderboard"