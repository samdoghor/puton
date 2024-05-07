"""src/resources/coach_employ.py

Keyword arguments:
argument -- id, **args
Return: Coach Employ's CRUD
"""

import uuid

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError, IntegrityError

from models import CoachEmployModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class CoachEmployResource(Resource):
    """This class performs CRUD Operation on Coach"""

    @staticmethod
    @parse_params(
        Argument(
            "employment_type",
            location="json",
            required=True,
            help="The employment type of the coach",
        ),
        Argument(
            "coach_id",
            location="json",
            required=True,
            help="The coach id of the coach",
        ),
        Argument(
            "season_id",
            location="json",
            required=True,
            help="The season id of the coach",
        ),
        Argument(
            "team_id",
            location="json",
            required=True,
            help="The team id of the coach",
        )
    )
    def create(
        employment_type: str,
        coach_id: uuid,
        season_id: uuid,
        team_id: uuid,
    ):
        """creates a new coach employment"""

        try:
            new_coach_employment = CoachEmployModel(
                employment_type=employment_type,
                coach_id=coach_id,
                season_id=season_id,
                team_id=team_id,
            )

            new_coach_employment.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "coach employment id": new_coach_employment.id,
                            "employment type": employment_type,
                            "coach id": coach_id,
                            "season id": season_id,
                            "team id": team_id,
                            "created at": new_coach_employment.created_at,
                            "updated at": new_coach_employment.updated_at,
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
                "message": "The coach id or season id or team id is incorrect",  # noqa
            }, 500

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def read_all():
        """retrieves all coaches employment"""

        try:
            coaches_employment = CoachEmployModel.query.all()

            if not coaches_employment:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No coach employment record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if coaches_employment:
                coaches_employment_record = []

                for coach in coaches_employment:
                    coaches_employment_record.append(
                        {
                            "coach employment id": coach.id,
                            "employment type": coach.employment_type,
                            "coach id": coach.coach_id,
                            "season id": coach.season_id,
                            "team id": coach.team_id,
                            "created at": coach.created_at,
                            "updated at": coach.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": coaches_employment_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No coach employment record was found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one coach employment by id"""

        try:
            coach_employment = CoachEmployModel.query.filter_by(id=id).first()

            if not coach_employment:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The coach employment with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if coach_employment:
                coach_employment_record = {
                    "coach employment id": coach_employment.id,
                    "employment type": coach_employment.employment_type,
                    "coach id": coach_employment.coach_id,
                    "season id": coach_employment.season_id,
                    "team id": coach_employment.team_id,
                    "created at": coach_employment.created_at,
                    "updated at": coach_employment.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": coach_employment_record,
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
                "message": f"The coach employment with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument(
            "employment_type",
            location="json",
            help="The employment type of the coach",
        ),
        Argument(
            "coach_id",
            location="json",
            help="The coach id of the coach",
        ),
        Argument(
            "season_id",
            location="json",
            help="The season id of the coach",
        ),
        Argument(
            "team_id",
            location="json",
            help="The team id of the coach",
        )
    )
    def update(id=None, **args):
        """retrieves a coach employment by id and update the coach employment"""  # noqa

        try:
            coach_employment = CoachEmployModel.query.filter_by(id=id).first()

            if not coach_employment:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The coach employment with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if coach_employment:
                if "employment_type" in args and args["employment_type"] is not None:  # noqa
                    coach_employment.employment_type = args["employment_type"]

                if "coach_id" in args and args["coach_id"] is not None:
                    coach_employment.coach_id = args["coach_id"]

                if "season_id" in args and args["season_id"] is not None:
                    coach_employment.season_id = args["season_id"]

                if "team_id" in args and args["team_id"] is not None:
                    coach_employment.team_id = args["team_id"]

                coach_employment.save()

                update_coach_employment = {
                    "coach employment id": coach_employment.id,
                    "employment type": coach_employment.employment_type,
                    "coach id": coach_employment.coach_id,
                    "season id": coach_employment.season_id,
                    "team id": coach_employment.team_id,
                    "created at": coach_employment.created_at,
                    "updated at": coach_employment.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_coach_employment,
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
        """delete one coach employment by id"""

        try:
            coach_employment = CoachEmployModel.query.filter_by(id=id).first()

            if not coach_employment:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The coach employment with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            coach_employment.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The coach employment with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The coach employment with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
