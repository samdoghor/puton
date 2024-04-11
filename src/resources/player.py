"""src/resources/player.py

Keyword arguments:
argument -- id, **args
Return: Player's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError, IntegrityError

from models import PlayerModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params)


class PlayerResource(Resource):
    """This class performs CRUD Operation on Player"""

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True,
                 help="The first name of the player"),
        Argument("last_name", location="json", required=True,
                 help="The last name of the player"),
        Argument("middle_name", location="json", required=True,
                 help="The middle name of the player"),
        Argument(
            "date_of_birth", location="json", required=True,
            help="The date of birth of the player"
        ),
        Argument("height", location="json", required=True,
                 help="The height of the player"),
        Argument("weight", location="json", required=True,
                 help="The weight of the player"),
        Argument("rating", location="json", required=True,
                 help="The rating of the player"),
        Argument("postion", location="json", required=True,
                 help="The postion of the player"),
        Argument("injury", location="json", required=True, type=bool,
                 help="The injury status of the player"),
        Argument("country_id", location="json", required=True,
                 help="The country of the player"),
        Argument("team_id", location="json", required=True,
                 help="The team of the player"),

    )
    def create(first_name, last_name, middle_name, date_of_birth, height,
               weight, rating, postion, injury, country_id, team_id):
        """creates a new player"""

        try:
            new_player = PlayerModel(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                date_of_birth=date_of_birth,
                height=height,
                weight=weight,
                rating=rating,
                postion=postion,
                injury=injury,
                country_id=country_id,
                team_id=team_id
            )

            new_player.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "first name": first_name,
                            "last name": last_name,
                            "middle name": middle_name,
                            "date of birth": date_of_birth,
                            "height": height,
                            "weight": weight,
                            "rating": rating,
                            "postion": postion,
                            "injury": injury,
                            "country id": country_id,
                            "team id": team_id
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
        """retrieves all players"""

        try:
            players = PlayerModel.query.all()

            if not players:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No player record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if players:
                players_record = []

                for player in players:
                    players_record.append(
                        {
                            "player id": player.id,
                            "first name": player.first_name,
                            "last name": player.last_name,
                            "middle name": player.middle_name,
                            "date of birth": player.date_of_birth.strftime("%Y-%m-%d"),  # noqa
                            "height": player.height,
                            "weight": player.weight,
                            "rating": player.rating,
                            "postion": player.postion,
                            "injury": player.injury,
                            "country id": player.country_id,
                            "team id": player.team_id
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": players_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No player record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one player by id"""

        try:
            player = PlayerModel.query.filter_by(id=id).first()

            if not player:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The player with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if player:
                player_record = {
                    "player id": player.id,
                    "first name": player.first_name,
                    "last name": player.last_name,
                    "middle name": player.middle_name,
                    "date of birth": player.date_of_birth.strftime("%Y-%m-%d"),
                    "height": player.height,
                    "weight": player.weight,
                    "rating": player.rating,
                    "postion": player.postion,
                    "injury": player.injury,
                    "country id": player.country_id,
                    "team id": player.team_id
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": player_record,
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
                "message": f"The player with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument("first_name", location="json",
                 help="The first name of the player"),
        Argument("last_name", location="json",
                 help="The last name of the player"),
        Argument("middle_name", location="json",
                 help="The middle name of the player"),
        Argument(
            "date_of_birth", location="json",
            help="The date of birth of the player"
        ),
        Argument("height", location="json",
                 help="The height of the player"),
        Argument("weight", location="json",
                 help="The weight of the player"),
        Argument("rating", location="json",
                 help="The rating of the player"),
        Argument("postion", location="json",
                 help="The postion of the player"),
        Argument("injury", location="json", type=bool,
                 help="The injury status of the player"),
        Argument("country_id", location="json",
                 help="The country of the player"),
        Argument("team_id", location="json",
                 help="The team of the player"),
    )
    def update(id=None, **args):
        """retrieves a player by id and update the player"""

        try:
            player = PlayerModel.query.filter_by(id=id).first()

            if not player:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The player with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if player:
                if "first_name" in args and args["first_name"] is not None:
                    player.first_name = args["first_name"]

                if "last_name" in args and args["last_name"] is not None:
                    player.last_name = args["last_name"]

                if "middle_name" in args and args["middle_name"] is not None:
                    player.middle_name = args["middle_name"]

                if "date_of_birth" in args and args["date_of_birth"] is not None:  # noqa
                    player.date_of_birth = args["date_of_birth"]

                if "height" in args and args["height"] is not None:
                    player.height = args["height"]

                if "weight" in args and args["weight"] is not None:
                    player.weight = args["weight"]

                if "rating" in args and args["rating"] is not None:
                    player.rating = args["rating"]

                if "postion" in args and args["postion"] is not None:
                    player.postion = args["postion"]

                if "injury" in args and args["injury"] is not None:
                    player.injury = args["injury"]

                if "country_id" in args and args["country_id"] is not None:
                    player.country_id = args["country_id"]

                if "team_id" in args and args["team_id"] is not None:
                    player.team_id = args["team_id"]

                player.save()

                update_player = {
                    "player id": player.id,
                    "first name": player.first_name,
                    "last name": player.last_name,
                    "middle name": player.middle_name,
                    "date of birth": player.date_of_birth.strftime("%Y-%m-%d"),
                    "height": player.height,
                    "weight": player.weight,
                    "rating": player.rating,
                    "postion": player.postion,
                    "injury": player.injury,
                    "country id": player.country_id,
                    "team id": player.team_id
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_player,
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
        """delete one player by id"""

        try:
            player = PlayerModel.query.filter_by(id=id).first()

            if not player:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The player with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            player.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The player with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The player with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
