"""src/resources/game_team.py

Keyword arguments:
argument -- id, **args
Return: Game Team's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import GameTeamModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params)


class GameTeamResource(Resource):
    """This class performs CRUD Operation on Game Teams"""

    @staticmethod
    @parse_params(
        Argument(
            "is_home",
            location="json",
            required=True,
            type=bool,
            help="Is the team home or away for the gmae"
        ),
        Argument(
            "game_id",
            location="json",
            required=True,
            help="The game to which the event belong to"),
        Argument(
            "team_id",
            location="json",
            required=True,
            help="The team to whom the event occured to",
        ),
    )
    def create(is_home, game_id, team_id):
        """creates a new game team"""

        try:
            new_game_player = GameTeamModel(
                is_home=is_home,
                game_id=game_id,
                team_id=team_id,
            )

            new_game_player.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "game_team id": new_game_player.id,
                            "home_team": is_home,
                            "game_id": game_id,
                            "team_id": team_id,
                            "created_at": new_game_player.created_at,
                            "updated_at": new_game_player.updated_at,
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
        """retrieves all game teams"""

        try:
            game_teams = GameTeamModel.query.all()

            if not game_teams:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No game team record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_teams:
                game_teams_record = []

                for game_team in game_teams:
                    game_teams_record.append(
                        {
                            "game_team id": game_team.id,
                            "home_team": game_team.is_home,
                            "game_id": game_team.game_id,
                            "team_id": game_team.team_id,
                            "created_at": game_team.created_at,
                            "updated_at": game_team.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_teams_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No game team record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one game team by id"""

        try:
            game_team = GameTeamModel.query.filter_by(id=id).first()

            if not game_team:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game team with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_team:
                game_team_record = {
                    "game_team_id": game_team.id,
                    "home_team": game_team.is_home,
                    "game_id": game_team.game_id,
                    "team_id": game_team.team_id,
                    "created_at": game_team.created_at,
                    "updated_at": game_team.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_team_record,
                        }
                    ),
                    200,
                )

        except DataError:
            return {
                "error_message": "Wrong ID format",
                "message": "The Id you are trying to retrieve is invalid, check UUID correct format.",  # noqa
            }, 500

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": f"The game team with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument(
            "is_home",
            location="json",
            type=bool,
            help="Is the team home or away for the gmae"
        ),
        Argument(
            "game_id",
            location="json",
            help="The game to which the event belong to"),
        Argument(
            "team_id",
            location="json",
            help="The team to whom the event occured to",
        ),
    )
    def update(id=None, **args):
        """retrieves a game team by id and update the game team"""

        try:
            game_team = GameTeamModel.query.filter_by(id=id).first()

            if not game_team:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game team with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_team:
                if "is_home" in args and args["is_home"] is not None:  # noqa
                    game_team.is_home = args["is_home"]

                if "game_id" in args and args["game_id"] is not None:
                    game_team.game_id = args["game_id"]

                if "team_id" in args and args["team_id"] is not None:  # noqa
                    game_team.team_id = args["team_id"]

                game_team.save()

                update_game_team = {
                    "game_team_id": game_team.id,
                    "home_team": game_team.is_home,
                    "game_id": game_team.game_id,
                    "team_id": game_team.team_id,
                    "created_at": game_team.created_at,
                    "updated_at": game_team.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_game_team,
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
                "message": f"The game team with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def delete(id=None):
        """retrieves a game team by id and delete the game team"""

        try:
            game_team = GameTeamModel.query.filter_by(id=id).first()

            if not game_team:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game team with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            game_team.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The game team with id {id} was found in the database and was deleted",  # noqa
                    }
                ),
                200,
            )

        except DataError:
            return {
                "error_message": "Wrong ID format",
                "message": "The Id you are trying to retrieve is invalid, check UUID correct format.",  # noqa
            }, 500

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": f"The game team with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
