from flask import Flask, jsonify, request

from endpoints.servers import GET_servers
from endpoints.score import POST_score, GET_score
from classes.errors import JWException
from classes.dbTables import parkourDB

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Ensures the databases are connected prior to executing a request.
@application.before_request
def _db_connect():
    parkourDB.connect()

@application.route("/servers", methods=['GET'])
def servers():
    return GET_servers()

@application.route("/score", methods=['GET','POST'])
def score():
    if request.method == 'GET':
        return GET_score()
    else:
        return POST_score()

# Used to calculate if an instance is responding to requests.
@application.route("/health", methods=['GET'])
def health():
    return ('', 204)

@application.errorhandler(400)
def flaskNotFoundError(e):
    errorDict = {"error": "Bad Request", "error_description": "Malformed or missing data in JSON body"}
    response = jsonify(errorDict)
    response.status_code = 400
    return response

# Flask 404 HTML to JSON handler
@application.errorhandler(404)
def flaskNotFoundError(e):
    errorDict = {"error": "Not Found", "error_description": "Requested resource not found on Parkour API"}
    response = jsonify(errorDict)
    response.status_code = 404
    return response

# Flask 405 HTML to JSON handler
@application.errorhandler(405)
def flaskMethodNotAllowed(e):
    errorDict = {"error": "Method Not Allowed", "error_description": "This method is not allowed on this endpoint"}
    response = jsonify(errorDict)
    response.status_code = 405
    return response

# General JW Exception handler
@application.errorhandler(JWException)
def UHExceptionHandler(e):
    errorDict = {"error": e.error}
    if e.description is not None:
        errorDict["error_description"]= e.description
    if e.status is not None:
        errorDict["status"] = e.status
    response = jsonify(errorDict)
    response.status_code = e.HTTPStatus
    return response

# Unexpected error handler
@application.errorhandler(Exception)
def catchAll(e):
    errorDict = {"error": "Internal Sever Error", "error_description": "An unexpected error has occurred"}
    response = jsonify(errorDict)
    response.status_code = 500
    return response
# ----------------------------------------------------------------------------------------------------------------------

@application.teardown_request
def _db_close(exc):
    if not parkourDB.is_closed():
        parkourDB.close()

# run the app.
if __name__ == "__main__":
    application.run()
