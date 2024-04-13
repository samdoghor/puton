"""src/resources/referee.py

Keyword arguments:
argument -- id, **args
Return: Referee's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from models import RefereeModel
from sqlalchemy.exc import DataError, IntegrityError
from utils import Conflict, DataNotFound, Forbidden, InternalServerError, parse_params


class RefereeResource(Resource):
    """This class performs CRUD Operation on Referee"""

    @staticmethod
    @parse_params(
        Argument(
            "first_name",
            location="json",
            required=True,
            help="The first name of the referee",
        ),
        Argument(
            "last_name",
            location="json",
            required=True,
            help="The last name of the referee",
        ),
        Argument(
            "middle_name",
            location="json",
            required=True,
            help="The middle name of the referee",
        ),
        Argument(
            "country_id",
            location="json",
            required=True,
            help="The country of the referee",
        ),
    )
    def create(first_name, last_name, middle_name, country_id):
        """creates a new referee"""

        try:
            new_referee = RefereeModel(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                country_id=country_id,
            )

            new_referee.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "first name": first_name,
                            "last name": last_name,
                            "middle name": middle_name,
                            "country id": country_id,
                        },
                    }
                ),
                200,
            )

        except DataError:
            return {
                "code": 500,
                "code_message": "Wrong DataType",
                "message": "A datatype error has occur, check the input and try again.",  # noqa
            }, 500

        except IntegrityError:
            return {
                "code": 500,
                "code_message": "Wrong DataType",
                "message": "The country id is incorrect",  # noqa
            }, 500

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def read_all():
        """retrieves all referees"""

        try:
            referees = RefereeModel.query.all()

            if not referees:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No referee record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if referees:
                referees_record = []

                for referee in referees:
                    referees_record.append(
                        {
                            "referee id": referee.id,
                            "first name": referee.first_name,
                            "last name": referee.last_name,
                            "middle name": referee.middle_name,
                            "country id": referee.country_id,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": referees_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No referee record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one referee by id"""

        try:
            referee = RefereeModel.query.filter_by(id=id).first()

            if not referee:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The referee with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if referee:
                referee_record = {
                    "referee id": referee.id,
                    "first name": referee.first_name,
                    "last name": referee.last_name,
                    "middle name": referee.middle_name,
                    "country id": referee.country_id,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": referee_record,
                        }
                    ),
                    200,
                )

        except DataError:
            return {
                "error message": "Wrong ID format",
                "message": "The Id you are trying to retrieve is invalid, check UUID correct format.",  # noqa
            }, 500

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": f"The referee with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", help="The first name of the referee"),
        Argument("last_name", location="json", help="The last name of the referee"),
        Argument("middle_name", location="json", help="The middle name of the referee"),
        Argument("country_id", location="json", help="The country of the referee"),
    )
    def update(id=None, **args):
        """retrieves a referee by id and update the referee"""

        try:
            referee = RefereeModel.query.filter_by(id=id).first()

            if not referee:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The referee with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if referee:
                if "first_name" in args and args["first_name"] is not None:
                    referee.first_name = args["first_name"]

                if "last_name" in args and args["last_name"] is not None:
                    referee.last_name = args["last_name"]

                if "middle_name" in args and args["middle_name"] is not None:
                    referee.middle_name = args["middle_name"]

                if "country_id" in args and args["country_id"] is not None:
                    referee.country_id = args["country_id"]

                referee.save()

                update_referee = {
                    "referee id": referee.id,
                    "first name": referee.first_name,
                    "last name": referee.last_name,
                    "middle name": referee.middle_name,
                    "country id": referee.country_id,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_referee,
                        }
                    ),
                    200,
                )

        except DataError:
            return {
                "code": 500,
                "code_message": "Wrong DataType",
                "message": "A datatype error has occur, check the input and try again.",  # noqa
            }, 500

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def delete(id=None):
        """delete one referee by id"""

        try:
            referee = RefereeModel.query.filter_by(id=id).first()

            if not referee:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The referee with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            referee.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The referee with id {id} was found in the database and was deleted",  # noqa
                    }
                ),
                200,
            )

        except DataError:
            return {
                "error message": "Wrong ID format",
                "message": "The Id you are trying to retrieve is invalid, check UUID correct format.",  # noqa
            }, 500

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": f"The referee with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
