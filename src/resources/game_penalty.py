"""src/resources/game_penalty.py

Keyword arguments:
argument -- id, **args
Return: Game Penalty's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import GamePenaltyModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class GamePenaltyResource(Resource):
    """This class performs CRUD Operation on Game Penalty"""

    @staticmethod
    @parse_params(
        Argument(
            "is_penalty_shootout",
            location="json",
            type=bool,
            required=True,
            help="Is the penalty event a penalty shootout?"
        ),
        Argument(
            "is_goal",
            location="json",
            type=bool,
            required=True,
            help="Was the penalty a goal",
        ),
        Argument(
            "game_event_id",
            location="json",
            required=True,
            help="Which event id is this penalty"
        ),
    )
    def create(is_penalty_shootout, is_goal, game_event_id):
        """creates a new game penalty event"""

        try:
            new_game_penalty = GamePenaltyModel(
                is_penalty_shootout=is_penalty_shootout,
                is_goal=is_goal,
                game_event_id=game_event_id,
            )

            new_game_penalty.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "game penalty id": new_game_penalty.id,
                            "is penalty shootout": is_penalty_shootout,
                            "is goal": is_goal,
                            "game event id": game_event_id,
                            "created at": new_game_penalty.created_at,
                            "updated at": new_game_penalty.updated_at
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
        """retrieves all game penalties"""

        try:
            game_penalties = GamePenaltyModel.query.all()

            if not game_penalties:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No game penalty record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_penalties:
                game_penalties_record = []

                for game_penalty in game_penalties:
                    game_penalties_record.append(
                        {
                            "game penalty id": game_penalty.id,
                            "is penalty shootout": game_penalty.is_penalty_shootout,  # noqa
                            "is goal": game_penalty.is_goal,
                            "game event id": game_penalty.game_event_id,
                            "created at": game_penalty.created_at,
                            "updated at": game_penalty.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_penalties_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No game penalty record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one game penalty by id"""

        try:
            game_penalty = GamePenaltyModel.query.filter_by(id=id).first()

            if not game_penalty:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game penalty with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_penalty:
                game_penalty_record = {
                    "game penalty id": game_penalty.id,
                    "is penalty shootout": game_penalty.is_penalty_shootout,  # noqa
                    "is goal": game_penalty.is_goal,
                    "game event id": game_penalty.game_event_id,
                    "created at": game_penalty.created_at,
                    "updated at": game_penalty.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": game_penalty_record,
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
                "message": f"The game peanlty with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument(
            "is_penalty_shootout",
            location="json",
            type=bool,
            help="Is the penalty event a penalty shootout?"
        ),
        Argument(
            "is_goal",
            location="json",
            type=bool,
            help="Was the penalty a goal",
        ),
        Argument(
            "game_event_id",
            location="json",
            help="Which event id is this penalty"
        ),
    )
    def update(id=None, **args):
        """retrieves a game penalty by id and update the game penalty"""

        try:
            game_penalty = GamePenaltyModel.query.filter_by(id=id).first()

            if not game_penalty:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game penalty with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if game_penalty:
                if "is_penalty_shootout" in args and args["is_penalty_shootout"] is not None:  # noqa
                    game_penalty.is_penalty_shootout = args["is_penalty_shootout"]  # noqa

                if "is_goal" in args and args["is_goal"] is not None:
                    game_penalty.is_goal = args["is_goal"]

                if "game_event_id" in args and args["game_event_id"] is not None:  # noqa
                    game_penalty.game_event_id = args["game_event_id"]

                game_penalty.save()

                update_game_penalty = {
                    "game penalty id": game_penalty.id,
                    "is penalty shootout": game_penalty.is_penalty_shootout,  # noqa
                    "is goal": game_penalty.is_goal,
                    "game event id": game_penalty.game_event_id,
                    "created at": game_penalty.created_at,
                    "updated at": game_penalty.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_game_penalty,
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
                "message": f"The game penalty with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def delete(id=None):
        """retrieves a game penalty by id and delete the game penalty"""

        try:
            game_penalty = GamePenaltyModel.query.filter_by(id=id).first()

            if not game_penalty:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The game penalty with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            game_penalty.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The game penalty with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The game penalty with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
