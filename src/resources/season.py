"""src/resources/season.py

Keyword arguments:
argument -- id, **args
Return: Season's CRUD
"""

from datetime import datetime

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import SeasonModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class SeasonResource(Resource):
    """This class performs CRUD Operation on Season"""

    @staticmethod
    @parse_params(
        Argument(
            "start_date",
            location="json",
            required=True,
            help="The date the league started",
        ),
        Argument(
            "end_date",
            location="json",
            required=True,
            help="The date the league ended"
        ),
        Argument(
            "current_season",
            location="json",
            required=True,
            type=bool,
            help="Is this the current season",
        ),
    )
    def create(start_date, end_date, current_season):
        """creates a new season"""

        try:
            season = SeasonModel.query.filter_by(
                start_date=datetime.strptime(start_date, "%Y-%m-%d")
            ).first()

            if season:
                return (
                    jsonify(
                        {
                            "code": 409,
                            "code_message": "Data Conflict",
                            "message": f"The season {start_date} already exist in the database",  # noqa
                        }
                    ),
                    409,
                )

            if not season:
                new_season = SeasonModel(
                    start_date=start_date,
                    end_date=end_date,
                    current_season=current_season,
                )

                new_season.save()

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_message": "Successful",
                            "data": {
                                "season id": new_season.id,
                                "start date": start_date,
                                "end date": end_date,
                                "current season": current_season,
                                "created at": new_season.created_at,
                                "updated at": new_season.updated_at,
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
        """retrieves all seasons"""

        try:
            seasons = SeasonModel.query.all()

            if not seasons:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No season record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if seasons:
                seasons_record = []

                for season in seasons:
                    seasons_record.append(
                        {
                            "season id": season.id,
                            "start date": season.start_date.year,
                            "end date": season.end_date.year,
                            "current season": season.current_season,
                            "created at": season.created_at,
                            "updated at": season.updated_at
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": seasons_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No season record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one season by id"""

        try:
            season = SeasonModel.query.filter_by(id=id).first()

            if not season:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The season with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if season:
                season_record = {
                    "season id": season.id,
                    "start date": season.start_date.year,
                    "end date": season.end_date.year,
                    "current season": season.current_season,
                    "created at": season.created_at,
                    "updated at": season.updated_at
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": season_record,
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
                "message": f"The season with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument("start_date", location="json",
                 help="The date the league started"),
        Argument("end_date", location="json",
                 help="The date the league ended"),
        Argument(
            "current_season",
            location="json",
            type=bool,
            help="Is this the current season",
        ),
    )
    def update(id=None, **args):
        """retrieves a season by id and update the season"""

        try:
            season = SeasonModel.query.filter_by(id=id).first()

            if not season:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The season with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if season:
                if "start_date" in args and args["start_date"] is not None:
                    season.start_date = args["start_date"]

                if "end_date" in args and args["end_date"] is not None:
                    season.end_date = args["end_date"]

                if (
                    "current_season" in args
                    and args["current_season"] is not None  # noqa
                ):
                    season.current_season = args["current_season"]

                season.save()

                update_season = {
                    "season id": season.id,
                    "start date": season.start_date.year,
                    "end date": season.end_date.year,
                    "current season": season.current_season,
                    "created at": season.created_at,
                    "updated at": season.updated_at
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_season,
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
                "message": f"The season with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def delete(id=None):
        """retrieves a season by id and delete the season"""

        try:
            season = SeasonModel.query.filter_by(id=id).first()

            if not season:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The season with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            season.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The season with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The season with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
