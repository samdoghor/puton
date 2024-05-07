"""src/resources/venue.py

Keyword arguments:
argument -- id, **args
Return: Venue's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import VenueModel
from utils import (Conflict, DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class VenueResource(Resource):
    """This class performs CRUD Operation on Venue"""

    @staticmethod
    @parse_params(
        Argument(
            "name",
            location="json",
            required=True, help="The name of the club's venue"
        ),
        Argument(
            "address",
            location="json",
            required=True,
            help="The address of the club's venue",
        ),
        Argument(
            "city",
            location="json",
            help="The city of the club's venue"),
        Argument(
            "capacity",
            location="json",
            required=True,
            help="The capacity of the club's venue",
        ),
        Argument(
            "team_id",
            location="json",
            required=True,
            help="The team to which the club venue belong",
        ),
    )
    def create(name, address, city, capacity, team_id):
        """creates a new club's venue"""

        try:
            venue = VenueModel.query.filter_by(name=name).first()

            if venue:
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

            if not venue:
                new_venue = VenueModel(
                    name=name,
                    address=address,
                    city=city,
                    capacity=capacity,
                    team_id=team_id,
                )

                new_venue.save()

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_message": "Successful",
                            "data": {
                                "venue id": new_venue.id,
                                "name": name,
                                "address": address,
                                "city": city,
                                "capacity": capacity,
                                "team id": team_id,
                                "created at": new_venue.created_at,
                                "updated at": new_venue.updated_at,
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
        """retrieves all venues"""

        try:
            venues = VenueModel.query.all()

            if not venues:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": "No venue record was found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if venues:
                venues_record = []

                for venue in venues:
                    venues_record.append(
                        {
                            "venue id": venue.id,
                            "name": venue.name,
                            "address": venue.address,
                            "city": venue.city,
                            "capacity": venue.capacity,
                            "team id": venue.team_id,
                            "created at": venue.created_at,
                            "updated at": venue.updated_at,
                        }
                    )

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": venues_record,
                        }
                    ),
                    200,
                )

        except DataNotFound as e:
            return {
                "code": e.code,
                "type": e.type,
                "code_mesaage": e.message,
                "message": "No venue record was found in the database",
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except Conflict as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    def read_one(id=None):
        """retrieves one venue by id"""

        try:
            venue = VenueModel.query.filter_by(id=id).first()

            if not venue:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The venue with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if venue:
                venue_record = {
                    "venue id": venue.id,
                    "name": venue.name,
                    "address": venue.address,
                    "city": venue.city,
                    "capacity": venue.capacity,
                    "team id": venue.team_id,
                    "created at": venue.created_at,
                    "updated at": venue.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": venue_record,
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
                "message": f"The venue with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

    @staticmethod
    @parse_params(
        Argument("name", location="json", help="The name of the club's venue"),
        Argument("address", location="json",
                 help="The address of the club's venue"),
        Argument("city", location="json", help="The city of the club's venue"),
        Argument(
            "capacity",
            location="json",
            help="The capacity of the club's venue",
        ),
        Argument(
            "team_id",
            location="json",
            help="The team to which the club venue belong",
        ),
    )
    def update(id=None, **args):
        """retrieves a venue by id and update the venue"""

        try:
            venue = VenueModel.query.filter_by(id=id).first()

            if not venue:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The venue with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            if venue:
                if "name" in args and args["name"] is not None:
                    venue.name = args["name"]

                if "address" in args and args["address"] is not None:
                    venue.address = args["address"]

                if "city" in args and args["city"] is not None:
                    venue.city = args["city"]

                if "capacity" in args and args["capacity"] is not None:
                    venue.capacity = args["capacity"]

                if "team_id" in args and args["team_id"] is not None:
                    venue.team_id = args["team_id"]

                venue.save()

                update_venue = {
                    "venue id": venue.id,
                    "name": venue.name,
                    "address": venue.address,
                    "city": venue.city,
                    "capacity": venue.capacity,
                    "team id": venue.team_id,
                    "created at": venue.created_at,
                    "updated at": venue.updated_at,
                }

                return (
                    jsonify(
                        {
                            "code": 200,
                            "code_mesaage": "Successful",
                            "data": update_venue,
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
        """delete one venue by id"""

        try:
            venue = VenueModel.query.filter_by(id=id).first()

            if not venue:
                return (
                    jsonify(
                        {
                            "code": 404,
                            "code_message": "Data Not Found",
                            "message": f"The venue with id {id} was not found in the database",  # noqa
                        }
                    ),
                    404,
                )

            venue.delete()

            return (
                jsonify(
                    {
                        "code": 200,
                        "code_mesaage": "Successful",
                        "message": f"The venue with id {id} was found in the database and was deleted",  # noqa
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
                "message": f"The venue with id {id} was not found in the database",  # noqa
            }

        except Forbidden as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}

        except InternalServerError as e:
            return {"code": e.code, "type": e.type, "code_mesaage": e.message}
