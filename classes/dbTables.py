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

class PlayerTable(ParkourModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    score = IntegerField()
    class Meta:
        db_table = "player"