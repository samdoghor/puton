"""
This module define all errors necessary
"""


class InternalServerError(Exception):
    """ Class for Internal Server Error """

    def __init__(self, message):
        self.code = 500
        self.message = message


class DuplicateData(Exception):
    """ Class for Duplicate Data Error """

    def __init__(self, message):
        self.code = 400
        self.message = message


class Unauthorized(Exception):
    """ Class for Unauthorised Error """

    def __init__(self, message) -> None:
        self.code = 401
        self.message = message


class AccessDenied(Exception):
    """ Class for Access Denied Error """

    def __init__(self, message) -> None:
        self.code = 403
        self.message = message


class DataNotFound(Exception):
    """ Class for Data Not Found Error """

    def __init__(self, message) -> None:
        self.code = 404
        self.message = message


class ResourceNotCreated(Exception):
    """ Class for Resource Not Created Error """

    def __init__(self, message) -> None:
        self.code = 500
        self.message = message


class NotificationFailed(Exception):
    """ Class for Notification Failed Error """

    def __init__(self, message) -> None:
        self.code = 500
        self.message = message


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "UserNotFound": {
        "message": "User with given name already exists",
        "status": 400
    },
    "UpdatingMovieError": {
        "message": "Updating movie added by other is forbidden",
        "status": 403
    },
    "DeletingMovieError": {
        "message": "Deleting movie added by other is forbidden",
        "status": 403
    },
    "MovieNotExistsError": {
        "message": "Movie with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    }
}
