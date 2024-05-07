"""src/resources/player_transfer.py

Keyword arguments:
argument -- id, **args
Return:  Player Transfer's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError, IntegrityError

from models import PlayerTransferModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class PlayerTransferResource(Resource):
    """This class performs CRUD Operation on Players Transfer"""

    @staticmethod
    @parse_params(
        Argument(
            "amount",
            location="json",
            required=True,
            help="The fee for the transfer",
        ),
        Argument(
            "transfer_window",
            location="json",
            required=True,
            help="The transfer window",
        ),
        Argument(
            "transfer_type",
            location="json",
            required=True,
            help="The transfer type",
        ),
        Argument(
            "player_id",
            location="json",
            required=True,
            help="The id of the player to whom was transfered ",
        ),
        Argument(
            "season_id",
            location="json",
            required=True,
            help="The season id in which the player was transfer",
        ),
        Argument(
            "team_id",
            location="json",
            required=True,
            help="The team id the player was transfer to",
        )
    )
    def create(
        amount,
        transfer_window,
        transfer_type,
        player_id,
        season_id,
        team_id,
    ):
        """creates a new player transfer"""

        try:
            new_player_transfer = PlayerTransferModel(
                amount=amount,
                transfer_window=transfer_window,
                transfer_type=transfer_type,
                player_id=player_id,
                season_id=season_id,
                team_id=team_id,
            )

            new_player_transfer.save()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_message": "Successful",
                        "data": {
                            "player transfer id": new_player_transfer.id,
                            "amount": amount,
                            "transfer window": transfer_window,
                            "transfer type": transfer_type,
                            "player id": player_id,
                            "season id": season_id,
                            "team id": team_id,
                            "created at": new_player_transfer.created_at,
                            "updated at": new_player_transfer.updated_at,
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
                "message": "The player id or season id or team id is incorrect",  # noqa
            }, 500

        except Forbidden as e:
            return {"Code": e.code, "Type": e.type, "code_message": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_message": e.message}

    @staticmethod
    def read_all():
        """retrieves all player transfer"""

        try:
            players_transfer = PlayerTransferModel.query.all()

            if not players_transfer:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No player transfer record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if players_transfer:
                players_transfer_record = []

                for player_transfer in players_transfer:
                    players_transfer_record.append(
                        {
                            "player transfer id": player_transfer.id,
                            "amount": player_transfer.amount,
                            "transfer window": player_transfer.transfer_window,
                            "transfer type": player_transfer.transfer_type,
                            "player id": player_transfer.player_id,
                            "season id": player_transfer.season_id,
                            "team id": player_transfer.team_id,
                            "created at": player_transfer.created_at,
                            "updated at": player_transfer.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": players_transfer_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No player transfer record was found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one player transfer by id"""

        try:
            player_transfer = PlayerTransferModel.query.filter_by(
                id=id).first()

            if not player_transfer:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The player transfer with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if player_transfer:
                player_transfer_record = {
                    "player transfer id": player_transfer.id,
                    "amount": player_transfer.amount,
                    "transfer window": player_transfer.transfer_window,
                    "transfer type": player_transfer.transfer_type,
                    "player id": player_transfer.player_id,
                    "season id": player_transfer.season_id,
                    "team id": player_transfer.team_id,
                    "created at": player_transfer.created_at,
                    "updated at": player_transfer.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": player_transfer_record,
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
                "message": f"The player transfer with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument(
            "amount",
            location="json",
            help="The fee for the transfer",
        ),
        Argument(
            "transfer_window",
            location="json",
            help="The transfer window",
        ),
        Argument(
            "transfer_type",
            location="json",
            help="The transfer type",
        ),
        Argument(
            "player_id",
            location="json",
            help="The id of the player to whom was transfered ",
        ),
        Argument(
            "season_id",
            location="json",
            help="The season id in which the player was transfer",
        ),
        Argument(
            "team_id",
            location="json",
            help="The team id the player was transfer to",
        )
    )
    def update(id=None, **args):
        """retrieves a player transfer by id and update the player transfer"""  # noqa

        try:
            player_transfer = PlayerTransferModel.query.filter_by(
                id=id).first()

            if not player_transfer:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The player transfer with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if player_transfer:
                if "amount" in args and args["amount"] is not None:  # noqa
                    player_transfer.amount = args["amount"]

                if "transfer_window" in args and args["transfer_window"] is not None:  # noqa
                    player_transfer.transfer_window = args["transfer_window"]

                if "transfer_type" in args and args["transfer_type"] is not None:  # noqa
                    player_transfer.transfer_type = args["transfer_type"]

                if "player_id" in args and args["player_id"] is not None:
                    player_transfer.player_id = args["player_id"]

                if "season_id" in args and args["season_id"] is not None:
                    player_transfer.season_id = args["season_id"]

                if "team_id" in args and args["team_id"] is not None:
                    player_transfer.team_id = args["team_id"]

                player_transfer.save()

                update_player_transfer = {
                    "player transfer id": player_transfer.id,
                    "amount": player_transfer.amount,
                    "transfer window": player_transfer.transfer_window,
                    "transfer type": player_transfer.transfer_type,
                    "player id": player_transfer.player_id,
                    "season id": player_transfer.season_id,
                    "team id": player_transfer.team_id,
                    "created at": player_transfer.created_at,
                    "updated at": player_transfer.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_player_transfer,
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
        """delete one player transfer by id"""

        try:
            player_transfer = PlayerTransferModel.query.filter_by(
                id=id).first()

            if not player_transfer:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The player transfer with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            player_transfer.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The player transfer with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The player transfer with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
