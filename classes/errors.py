from enum import IntEnum

# Integer enumeration for HTTP Status codes
class HTTPStatus(IntEnum):
    OK = 200
    BadRequest = 400
    Unauthorized = 401
    Internal = 500
    Forbidden = 403

# Default JW Exception Class - for controlled aborts
class JWException(Exception):
    error = None
    description = None
    status = None

    def __init__(self, error):
        Exception.__init__(self)
        self.error = error

# JW Exception Error Classes -------------------------------------------------------------------------------------------
class Unauthorized(JWException):
    def __init__(self, description):
        JWException.__init__(self, "Unauthorized")
        self.HTTPStatus = HTTPStatus.Unauthorized
        self.description = description

class BadRequest(JWException):
    def __init__(self, description):
        JWException.__init__(self, "Bad Request")
        self.HTTPStatus = HTTPStatus.BadRequest
        self.description = description