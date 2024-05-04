"""src/resources/game_player.py

Keyword arguments:
argument -- id, **args
Return: Game Player's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import GamePlayerModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class GamePlayerResource(Resource):
    """This class performs CRUD Operation on Game Players"""

    @staticmethod
    @parse_params(
        Argument(
            "starting_lineup",
            location="json",
            required=True,
            type=bool,
            help="Is player included in lineup"
        ),
        Argument(
            "substitute",
            location="json",
            required=True,
            type=bool,
            help="Is player a substitute",
        ),
        Argument(
            "minutes_played",
            location="json",
            required=True,
            help="Minutes the player played"
        ),
        Argument(
            "game_id",
            location="json",
            required=True,
            help="The game to which the event belong to"),
        Argument(
            "player_id",
            location="json",
            required=True,
            help="The player to whom the event occured to",
        ),
        Argument(
            "game_team_id",
            location="json",
            required=True,
            help="The team to whom the event occured to",
        ),
    )
    def create(starting_lineup, substitute, minutes_played, game_id, player_id,
               game_team_id):
        """creates a new game player"""

        try:
            new_game_player = GamePlayerModel(
                starting_lineup=starting_lineup,
                substitute=substitute,
                minutes_played=minutes_played,
                game_id=game_id,
                player_id=player_id,
                game_team_id=game_team_id
            )

            new_game_player.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "game player id": new_game_player.id,
                            "starting lineup": starting_lineup,
                            "substitute": substitute,
                            "minutes played": minutes_played,
                            "game id": game_id,
                            "player id": player_id,
                            "game team id": game_team_id,
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
        """retrieves all game players"""

        try:
            game_players = GamePlayerModel.query.all()

            if not game_players:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No game player record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_players:
                game_players_record = []

                for game_player in game_players:
                    game_players_record.append(
                        {
                            "game player type id": game_player.id,
                            "starting lineup": game_player.starting_lineup,
                            "substitute": game_player.substitute,
                            "minutes played": game_player.minutes_played,
                            "game id": game_player.game_id,
                            "player id": game_player.player_id,
                            "game team id": game_player.game_team_id,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_players_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No game event record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one game player by id"""

        try:
            game_player = GamePlayerModel.query.filter_by(id=id).first()

            if not game_player:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game player with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_player:
                game_player_record = {
                    "game player type id": game_player.id,
                    "starting lineup": game_player.starting_lineup,
                    "substitute": game_player.substitute,
                    "minutes played": game_player.minutes_played,
                    "game id": game_player.game_id,
                    "player id": game_player.player_id,
                    "game team id": game_player.game_team_id,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_player_record,
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
                "message": f"The game player with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument(
            "starting_lineup",
            location="json",
            type=bool,
            help="Is player included in lineup"
        ),
        Argument(
            "substitute",
            location="json",
            type=bool,
            help="Is player a substitute",
        ),
        Argument(
            "minutes_played",
            location="json",
            help="Minutes the player played"
        ),
        Argument(
            "game_id",
            location="json",
            help="The game to which the event belong to"),
        Argument(
            "player_id",
            location="json",
            help="The player to whom the event occured to",
        ),
        Argument(
            "game_team_id",
            location="json",
            help="The team to whom the event occured to",
        ),
    )
    def update(id=None, **args):
        """retrieves a game player by id and update the game player"""

        try:
            game_player = GamePlayerModel.query.filter_by(id=id).first()

            if not game_player:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game player with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_player:
                if "starting_lineup" in args and args["starting_lineup"] is not None:  # noqa
                    game_player.starting_lineup = args["starting_lineup"]

                if "substitute" in args and args["substitute"] is not None:
                    game_player.substitute = args["substitute"]

                if "minutes_played" in args and args["minutes_played"] is not None:  # noqa
                    game_player.minutes_played = args["minutes_played"]

                if "game_id" in args and args["game_id"] is not None:
                    game_player.game_id = args["game_id"]

                if "player_id" in args and args["player_id"] is not None:  # noqa
                    game_player.player_id = args["player_id"]

                if "game_team_id" in args and args["game_team_id"] is not None:
                    game_player.game_team_id = args["game_team_id"]

                game_player.save()

                update_game_player = {
                    "game player type id": game_player.id,
                    "starting lineup": game_player.starting_lineup,
                    "substitute": game_player.substitute,
                    "minutes played": game_player.minutes_played,
                    "game id": game_player.game_id,
                    "player id": game_player.player_id,
                    "game team id": game_player.game_team_id,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_game_player,
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
                "message": f"The game player with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def delete(id=None):
        """retrieves a game player by id and delete the game player"""

        try:
            game_player = GamePlayerModel.query.filter_by(id=id).first()

            if not game_player:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game player with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            game_player.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The game player with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The game player with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
