"""src/resources/league.py

Keyword arguments:
argument -- id, **args
Return: League's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import LeagueModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class LeagueResource(Resource):
    """This class performs CRUD Operation on League"""

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the league"),
        Argument(
            "abbr",
            location="json",
            required=True,
            help="The abbreviation of the league",
        ),
        Argument(
            "league_type",
            location="json",
            required=True,
            help="The type of league"
        ),
        Argument(
            "logo",
            location="json",
            required=True,
            help="The logo of the league"),
        Argument(
            "country_id",
            location="json",
            required=True,
            help="The country which the league belong to",
        ),
    )
    def create(name, abbr, league_type, logo, country_id):
        """creates a new league"""

        try:
            league = LeagueModel.query.filter_by(name=name).first()

            if league:
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

            if not league:
                new_league = LeagueModel(
                    name=name,
                    abbr=abbr,
                    league_type=league_type,
                    logo=logo,
                    country_id=country_id,
                )

                new_league.save()

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_message": "Successful",
                            "data": {
                                "league id": new_league.id,
                                "name": name,
                                "abbr": abbr,
                                "league type": league_type,
                                "flag": logo,
                                "country id": country_id,
                                "created at": new_league.created_at,
                                "updated at": new_league.updated_at,
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
        """retrieves all league"""

        try:
            leagues = LeagueModel.query.all()

            if not leagues:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No league record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if leagues:
                leagues_record = []

                for league in leagues:
                    leagues_record.append(
                        {
                            "league id": league.id,
                            "name": league.name,
                            "abbr": league.abbr,
                            "league type": league.league_type,
                            "flag": league.logo,
                            "country id": league.country_id,
                            "created at": league.created_at,
                            "updated at": league.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": leagues_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No league record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one league by id"""

        try:
            league = LeagueModel.query.filter_by(id=id).first()

            if not league:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The league with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if league:
                league_record = {
                    "league id": league.id,
                    "name": league.name,
                    "abbr": league.abbr,
                    "league type": league.league_type,
                    "flag": league.logo,
                    "country id": league.country_id,
                    "created at": league.created_at,
                    "updated at": league.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": league_record,
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
                "message": f"The league with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument("name", location="json", help="The name of the league"),
        Argument("abbr", location="json",
                 help="The abbreviation of the league"),
        Argument("league_type", location="json", help="The type of league"),
        Argument("logo", location="json", help="The logo of the league"),
        Argument(
            "country_id",
            location="json",
            help="The country which the league belong to"
        ),
    )
    def update(id=None, **args):
        """retrieves a league by id and update the league"""

        try:
            league = LeagueModel.query.filter_by(id=id).first()

            if not league:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The league with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if league:
                if "name" in args and args["name"] is not None:
                    league.name = args["name"]

                if "abbr" in args and args["abbr"] is not None:
                    league.abbr = args["abbr"]

                if "league_type" in args and args["league_type"] is not None:
                    league.league_type = args["league_type"]

                if "logo" in args and args["logo"] is not None:
                    league.logo = args["logo"]

                if "country_id" in args and args["country_id"] is not None:
                    league.country_id = args["country_id"]

                league.save()

                update_league = {
                    "league id": league.id,
                    "name": league.name,
                    "abbr": league.abbr,
                    "league type": league.league_type,
                    "flag": league.logo,
                    "country id": league.country_id,
                    "created at": league.created_at,
                    "updated at": league.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_league,
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

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": f"The league with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def delete(id=None):
        """retrieves a league by id and delete the league"""

        try:
            league = LeagueModel.query.filter_by(id=id).first()

            if not league:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The league with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            league.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The league with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The league with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
