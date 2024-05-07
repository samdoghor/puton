"""src/resources/team.py

Keyword arguments:
argument -- id, **args
Return: Team's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import TeamModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class TeamResource(Resource):
    """This class performs CRUD Operation on Team"""

    @staticmethod
    @parse_params(
        Argument(
            "name",
            location="json",
            required=True,
            help="The name of the club"),
        Argument(
            "abbr",
            location="json",
            required=True,
            help="The abbreviation of the club"
        ),
        Argument(
            "flag",
            location="json",
            required=True,
            help="The flag of the club"),
        Argument(
            "founded",
            location="json",
            required=True,
            help="The year the club was founded",
        ),
        Argument(
            "country_id",
            location="json",
            required=True,
            help="The country to which the club belong",
        ),
    )
    def create(name, abbr, flag, founded, country_id):
        """creates a new club"""

        try:
            team = TeamModel.query.filter_by(name=name).first()

            if team:
                return (
                    jsonify(
                        {
                            "code": 409,
                            "code_message": "Data Conflict",
                            "message": f"{name} already exist in the database",
                        }
                    ),
                    409,
                )

            if not team:
                new_team = TeamModel(
                    name=name,
                    abbr=abbr,
                    flag=flag,
                    founded=founded,
                    country_id=country_id,
                )

                new_team.save()

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_message": "Successful",
                            "data": {
                                "team id": new_team.id,
                                "name": name,
                                "abbreviation": abbr,
                                "flag": flag,
                                "founded": founded,
                                "country id": country_id,
                                "created at": new_team.created_at,
                                "updated at": new_team.updated_at,
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

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def read_all():
        """retrieves all teams"""

        try:
            teams = TeamModel.query.all()

            if not teams:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No team record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if teams:
                teams_record = []

                for team in teams:
                    teams_record.append(
                        {
                            "team id": team.id,
                            "name": team.name,
                            "abbreviation": team.abbr,
                            "flag": team.flag,
                            "founded": team.founded,
                            "country id": team.country_id,
                            "created at": team.created_at,
                            "updated at": team.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": teams_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No team record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one team by id"""

        try:
            team = TeamModel.query.filter_by(id=id).first()

            if not team:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The team with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if team:
                team_record = {
                    "team id": team.id,
                    "name": team.name,
                    "abbreviation": team.abbr,
                    "flag": team.flag,
                    "founded": team.founded,
                    "country id": team.country_id,
                    "created at": team.created_at,
                    "updated at": team.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": team_record,
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
                "message": f"The team with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument("name", location="json", help="The name of the club"),
        Argument("abbr", location="json", help="The abbreviation of the club"),
        Argument("flag", location="json", help="The flag of the club"),
        Argument(
            "founded",
            location="json",
            help="The year the club was founded",
        ),
        Argument(
            "country_id",
            location="json",
            help="The country to which the club belong",
        ),
    )
    def update(id=None, **args):
        """retrieves a team by id and update the team"""

        try:
            team = TeamModel.query.filter_by(id=id).first()

            if not team:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The team with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if team:
                if "name" in args and args["name"] is not None:
                    team.name = args["name"]

                if "abbr" in args and args["abbr"] is not None:
                    team.abbr = args["abbr"]

                if "flag" in args and args["flag"] is not None:
                    team.flag = args["flag"]

                if "founded" in args and args["founded"] is not None:
                    team.founded = args["founded"]

                if "country_id" in args and args["country_id"] is not None:
                    team.country_id = args["country_id"]

                team.save()

                update_team = {
                    "team id": team.id,
                    "name": team.name,
                    "abbreviation": team.abbr,
                    "flag": team.flag,
                    "founded": team.founded,
                    "country id": team.country_id,
                    "created at": team.created_at,
                    "updated at": team.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_team,
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
        """delete one team by id"""

        try:
            team = TeamModel.query.filter_by(id=id).first()

            if not team:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The team with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            team.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The team with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The team with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
