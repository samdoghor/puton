"""src/resources/game_event.py

Keyword arguments:
argument -- id, **args
Return: Game Events's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import GameEventModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class GameEventResource(Resource):
    """This class performs CRUD Operation on Game Events"""

    @staticmethod
    @parse_params(
        Argument(
            "event_type",
            location="json",
            required=True,
            help="The event type"
        ),
        Argument(
            "event_time",
            location="json",
            required=True,
            help="The event time",
        ),
        Argument(
            "game_half",
            location="json",
            required=True,
            help="which half is the game"
        ),
        Argument(
            "game_id",
            location="json",
            required=True,
            help="The game to which the event belong to"),
        Argument(
            "game_player_id",
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
    def create(event_type, event_time, game_half, game_id, game_player_id,
               game_team_id):
        """creates a new league"""

        try:
            new_game_event = GameEventModel(
                event_type=event_type,
                event_time=event_time,
                game_half=game_half,
                game_id=game_id,
                game_player_id=game_player_id,
                game_team_id=game_team_id
            )

            new_game_event.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "event type id": new_game_event.id,
                            "event type": event_type,
                            "event time": event_time,
                            "game half": game_half,
                            "game id": game_id,
                            "game player id": game_player_id,
                            "game team id": game_team_id,
                            "created at": new_game_event.created_at,
                            "updated at": new_game_event.updated_at,
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
        """retrieves all game events"""

        try:
            game_events = GameEventModel.query.all()

            if not game_events:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No game event record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_events:
                game_events_record = []

                for game_event in game_events:
                    game_events_record.append(
                        {
                            "game event id": game_event.id,
                            "event type": game_event.event_type,
                            "event time": game_event.event_time,
                            "game half": game_event.game_half,
                            "game id": game_event.game_id,
                            "game player id": game_event.game_player_id,
                            "game team id": game_event.game_team_id,
                            "created at": game_event.created_at,
                            "updated at": game_event.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_events_record,
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
        """retrieves one game event by id"""

        try:
            game_event = GameEventModel.query.filter_by(id=id).first()

            if not game_event:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game event with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_event:
                game_event_record = {
                    "game event id": game_event.id,
                    "event type": game_event.event_type,
                    "event time": game_event.event_time,
                    "game half": game_event.game_half,
                    "game id": game_event.game_id,
                    "game player id": game_event.game_player_id,
                    "game team id": game_event.game_team_id,
                    "created at": game_event.created_at,
                    "updated at": game_event.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_event_record,
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
                "message": f"The game event with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument(
            "event_type",
            location="json",
            help="The event type"
        ),
        Argument(
            "event_time",
            location="json",
            help="The event time",
        ),
        Argument(
            "game_half",
            location="json",
            help="which half is the game"
        ),
        Argument(
            "game_id",
            location="json",
            help="The game to which the event belong to"),
        Argument(
            "game_player_id",
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
        """retrieves a game event by id and update the game event"""

        try:
            game_event = GameEventModel.query.filter_by(id=id).first()

            if not game_event:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game event with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_event:
                if "event_type" in args and args["event_type"] is not None:
                    game_event.event_type = args["event_type"]

                if "event_time" in args and args["event_time"] is not None:
                    game_event.event_time = args["event_time"]

                if "game_half" in args and args["game_half"] is not None:
                    game_event.game_half = args["game_half"]

                if "game_id" in args and args["game_id"] is not None:
                    game_event.game_id = args["game_id"]

                if "game_player_id" in args and args["game_player_id"] is not None:  # noqa
                    game_event.game_player_id = args["game_player_id"]

                if "game_team_id" in args and args["game_team_id"] is not None:
                    game_event.game_team_id = args["game_team_id"]

                game_event.save()

                update_game_event = {
                    "game event id": game_event.id,
                    "event type": game_event.event_type,
                    "event time": game_event.event_time,
                    "game half": game_event.game_half,
                    "game id": game_event.game_id,
                    "game player id": game_event.game_player_id,
                    "game team id": game_event.game_team_id,
                    "created at": game_event.created_at,
                    "updated at": game_event.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_game_event,
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
                "message": f"The game event with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def delete(id=None):
        """retrieves a game event by id and delete the game event"""

        try:
            game_event = GameEventModel.query.filter_by(id=id).first()

            if not game_event:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game event with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            game_event.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The game event with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The game event with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
