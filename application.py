from flask import Flask, jsonify

from endpoints.servers import GET_servers

# EB looks for an 'application' callable by default.
application = Flask(__name__)


@application.route("/servers", methods=['GET'])
def servers():
    return GET_servers()

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

# Unexpected error handler
@application.errorhandler(Exception)
def catchAll(e):
    errorDict = {"error": "Internal Sever Error", "error_description": "An unexpected error has occurred"}
    response = jsonify(errorDict)
    response.status_code = 500
    return response
# ----------------------------------------------------------------------------------------------------------------------

# run the app.
if __name__ == "__main__":
    application.run()
