"""src/resources/game.py

Keyword arguments:
argument -- id, **args
Return: Game's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import GameModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class GameResource(Resource):
    """This class performs CRUD Operation on Game"""

    @staticmethod
    @parse_params(
        Argument(
            "game_time",
            location="json",
            required=True,
            help="The time of the game"
        ),
        Argument(
            "game_date",
            location="json",
            required=True,
            help="The date of the game",
        ),
        Argument(
            "weather",
            location="json",
            required=True,
            help="Weather Condition of the game"
        ),
        Argument(
            "league_id",
            location="json",
            required=True,
            help="The league which the game belong to",
        ),
        Argument(
            "referee_id",
            location="json",
            required=True,
            help="The referee of the game",
        ),
        Argument(
            "season_id",
            location="json",
            required=True,
            help="The season which the game belong to",
        ),
        Argument(
            "venue_id",
            location="json",
            required=True,
            help="The venue where the game was held",
        ),
    )
    def create(game_time, game_date, weather, league_id, referee_id,
               season_id, venue_id):
        """creates a new game"""

        try:

            new_game = GameModel(
                game_time=game_time,
                game_date=game_date,
                weather=weather,
                league_id=league_id,
                referee_id=referee_id,
                season_id=season_id,
                venue_id=venue_id,
            )

            new_game.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "game id": new_game.id,
                            "game time": game_time,
                            "game date": game_date,
                            "weather": weather,
                            "league id": league_id,
                            "referee id": referee_id,
                            "season id": season_id,
                            "venue id": venue_id,
                            "created at": new_game.created_at,
                            "updated at": new_game.updated_at,
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
        """retrieves all games"""

        try:
            games = GameModel.query.all()

            if not games:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No game record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if games:
                games_record = []

                for game in games:
                    games_record.append(
                        {
                            "game id": game.id,
                            "game time": game.game_time.strftime("%H:%M"),
                            "game date": game.game_date.strftime("%Y-%m-%d"),
                            "weather": game.weather,
                            "league id": game.league_id,
                            "referee id": game.referee_id,
                            "season id": game.season_id,
                            "venue id": game.venue_id,
                            "created at": game.created_at,
                            "updated at": game.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": games_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No game record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one game by id"""

        try:
            game = GameModel.query.filter_by(id=id).first()

            if not game:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game:
                game_record = {
                    "game id": game.id,
                    "game time": game.game_time.strftime("%H:%M"),
                    "game date": game.game_date.strftime("%Y-%m-%d"),
                    "weather": game.weather,
                    "league id": game.league_id,
                    "referee id": game.referee_id,
                    "season id": game.season_id,
                    "venue id": game.venue_id,
                    "created at": game.created_at,
                    "updated at": game.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_record,
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
                "message": f"The game with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument(
            "game_time",
            location="json",
            help="The time of the game"
        ),
        Argument(
            "game_date",
            location="json",
            help="The date of the game",
        ),
        Argument(
            "weather",
            location="json",
            help="Weather Condition of the game"
        ),
        Argument(
            "league_id",
            location="json",
            help="The league which the game belong to",
        ),
        Argument(
            "referee_id",
            location="json",
            help="The referee of the game",
        ),
        Argument(
            "season_id",
            location="json",
            help="The season which the game belong to",
        ),
        Argument(
            "venue_id",
            location="json",
            help="The venue where the game was held",
        ),
    )
    def update(id=None, **args):
        """retrieves a game by id and update the game"""

        try:
            game = GameModel.query.filter_by(id=id).first()

            if not game:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game:
                if "game_time" in args and args["game_time"] is not None:
                    game.game_time = args["game_time"]

                if "game_date" in args and args["game_date"] is not None:
                    game.game_date = args["game_date"]

                if "weather" in args and args["weather"] is not None:
                    game.weather = args["weather"]

                if "league_id" in args and args["league_id"] is not None:
                    game.league_id = args["league_id"]

                if "referee_id" in args and args["referee_id"] is not None:
                    game.referee_id = args["referee_id"]

                if "season_id" in args and args["season_id"] is not None:
                    game.season_id = args["season_id"]

                if "venue_id" in args and args["venue_id"] is not None:
                    game.venue_id = args["venue_id"]

                game.save()

                update_game = {
                    "game id": game.id,
                    "game time": game.game_time.strftime("%H:%M"),
                    "game date": game.game_date.strftime("%Y-%m-%d"),
                    "weather": game.weather,
                    "league id": game.league_id,
                    "referee id": game.referee_id,
                    "season id": game.season_id,
                    "venue id": game.venue_id,
                    "created at": game.created_at,
                    "updated at": game.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_game,
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
                "message": f"The game with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def delete(id=None):
        """retrieves a game by id and delete the game"""

        try:
            game = GameModel.query.filter_by(id=id).first()

            if not game:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            game.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The game with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The game with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
