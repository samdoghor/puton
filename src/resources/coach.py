"""src/resources/coach.py

Keyword arguments:
argument -- id, **args
Return: Coach's CRUD
"""

import uuid

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError, IntegrityError

from models import CoachModel
from utils import (Conflict, DataNotFound, Forbidden,
                     InternalServerError, parse_params)


class CoachResource(Resource):
    """This class performs CRUD Operation on Coach"""

    @staticmethod
    @parse_params(
        Argument(
            "first_name",
            location="json",
            required=True,
            help="The first name of the coach",
        ),
        Argument(
            "last_name",
            location="json",
            required=True,
            help="The last name of the coach",
        ),
        Argument(
            "middle_name",
            location="json",
            required=True,
            help="The middle name of the coach",
        ),
        Argument(
            "country_id",
            location="json",
            required=True,
            help="The country of the coach",
        ),
        Argument(
            "team_id",
            location="json",
            required=True,
            help="The team of the coach"
        ),
    )
    def create(
            first_name: str,
            last_name: str,
            middle_name: str,
            country_id: uuid,
            team_id: uuid,
    ):
        """creates a new coach"""

        try:
            new_coach = CoachModel(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                country_id=country_id,
                team_id=team_id,
            )

            new_coach.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "coach id": new_coach.id,
                            "first name": first_name,
                            "last name": last_name,
                            "middle name": middle_name,
                            "country id": country_id,
                            "team id": team_id,
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
                "message": "The country id or team id is incorrect",  # noqa
            }, 500

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def read_all():
        """retrieves all coaches"""

        try:
            coaches = CoachModel.query.all()

            if not coaches:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No coach record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if coaches:
                coaches_record = []

                for coach in coaches:
                    coaches_record.append(
                        {
                            "coach id": coach.id,
                            "first name": coach.first_name,
                            "last name": coach.last_name,
                            "middle name": coach.middle_name,
                            "country id": coach.country_id,
                            "created at": coach.created_at,
                            "updated at": coach.updated_at
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": coaches_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No coach record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one coach by id"""

        try:
            coach = CoachModel.query.filter_by(id=id).first()

            if not coach:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The coach with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if coach:
                coach_record = {
                    "coach id": coach.id,
                    "first name": coach.first_name,
                    "last name": coach.last_name,
                    "middle name": coach.middle_name,
                    "country id": coach.country_id,
                    "created at": coach.created_at,
                    "updated at": coach.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": coach_record,
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
                "message": f"The coach with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument("first_name", location="json",
                 help="The first name of the coach"),
        Argument("last_name", location="json",
                 help="The last name of the coach"),
        Argument("middle_name", location="json",
                 help="The middle name of the coach"),
        Argument("country_id", location="json",
                 help="The country of the coach"),
        Argument("team_id", location="json", help="The team of the coach"),
    )
    def update(id=None, **args):
        """retrieves a coach by id and update the coach"""

        try:
            coach = CoachModel.query.filter_by(id=id).first()

            if not coach:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The coach with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if coach:
                if "first_name" in args and args["first_name"] is not None:
                    coach.first_name = args["first_name"]

                if "last_name" in args and args["last_name"] is not None:
                    coach.last_name = args["last_name"]

                if "middle_name" in args and args["middle_name"] is not None:
                    coach.middle_name = args["middle_name"]

                if "country_id" in args and args["country_id"] is not None:
                    coach.country_id = args["country_id"]

                coach.save()

                update_coach = {
                    "coach id": coach.id,
                    "first name": coach.first_name,
                    "last name": coach.last_name,
                    "middle name": coach.middle_name,
                    "country id": coach.country_id,
                    "created at": coach.created_at,
                    "updated at": coach.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_coach,
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
        """delete one coach by id"""

        try:
            coach = CoachModel.query.filter_by(id=id).first()

            if not coach:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The coach with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            coach.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The coach with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The coach with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
