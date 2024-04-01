"""src/resources/team.py

Keyword arguments:
argument -- id, **args
Return: Team's CRUD
"""

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import TeamModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params)


class TeamResource(Resource):
    """ This class performs CRUD Operation on Team """

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the club"),
        Argument("abbr", location="json", required=True,
                 help="The abbreviation of the club"),
        Argument("flag", location="json", required=True,
                 help="The flag of the club"),
        Argument("founded", location="json", required=True,
                 help="The year the club was founded"),
        Argument("country_id", location="json", required=True,
                 help="The country to which the club belong"),
        Argument("league_id", location="json", required=True,
                 help="The league to which the club belong")
    )
    def create(name, abbr, flag, founded, country_id, league_id):
        """ creates a new club """

        try:
            country = TeamModel.query.filter_by(name=name).first()

            if country:
                return jsonify(
                    {
                        'code': 409,
                        'code_message': "Data Conflict",
                        'message': f"{name} already exist in the database"
                    }
                ), 409

            if not country:
                new_country = TeamModel(
                    name=name,
                    abbr=abbr,
                    flag=flag
                )

                new_country.save()

                return jsonify(
                    {
                        'code': 200,
                        'code_message': "Successful",
                        'data': {
                            'name': name,
                            'abbreviation': abbr,
                            'flag': flag
                        }
                    }
                ), 200

        except DataError:
            return {
                'code': 500,
                'code_message': "Wrong DataType",
                'message': "A datatype error has occur, check the input and try again."  # noqa
                }, 500

        except Forbidden as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'code_message': e.message
            }

        except Conflict as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_message': e.message
            }

        except InternalServerError as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_message': e.message
            }

    def read_all():
        """ retrieves all countries """

        try:
            countries = TeamModel.query.all()

            if not countries:
                return jsonify(
                    {
                        'code': 404,
                        'code_message': "Data Not Found",
                        'message': "No country record was found in the database"  # noqa
                    }
                ), 404

            if countries:
                countries_record = []

                for country in countries:
                    countries_record.append(
                        {
                            'country_id': country.id,
                            'name': country.name,
                            'abbreviation': country.abbr,
                            'flag': country.flag
                        }
                    )

                return jsonify(
                    {
                        'code': 200,
                        'code_mesaage': "Successful",
                        'data': countries_record
                    }
                ), 200

        except DataNotFound as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message,
                'message': "No country record was found in the database"
            }

        except Forbidden as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message
            }

        except Conflict as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message
            }

        except InternalServerError as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message
            }

    def read_one(id=None):
        """ retrieves one countries by id """

        try:
            country = TeamModel.query.filter_by(id=id).first()

            if not country:
                return jsonify(
                    {
                        'code': 404,
                        'code_message': "Data Not Found",
                        'message': f"The country with id {id} was found in the database"  # noqa
                    }
                ), 404

            if country:
                country_record = {
                    'id': country.id,
                    'name': country.name,
                    'abbreviation': country.abbr,
                    'flag': country.flag
                }

                return jsonify(
                    {
                        'code': 200,
                        'code_mesaage': "Successful",
                        'data': country_record
                    }
                ), 200

        except DataError:
            return {
                "error message": "Wrong ID format",
                "message": "The Id you are trying to retrieve is invalid, check UUID correct format."  # noqa
                }, 500

        except DataNotFound as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message,
                'message': f"The country with id {id} was found in the database"  # noqa
            }

        except Forbidden as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message
            }

        except InternalServerError as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message
            }

    @staticmethod
    @parse_params(
        Argument("name", location="json", help="The name of the country"),
        Argument("abbr", location="json",
                 help="The abbreviation of the country"),
        Argument("flag", location="json", help="The flag of the country")
    )
    def update(id=None, **args):
        """ retrieves a country by id and update the country """

        try:
            country = TeamModel.query.filter_by(id=id).first()

            if not country:
                return jsonify(
                    {
                        'code': 404,
                        'code_message': "Data Not Found",
                        'message': f"The country with id {id} was found in the database"  # noqa
                    }
                ), 404

            if country:
                if 'name' in args and args['name'] is not None:
                    country.name = args['name']

                if 'abbr' in args and args['abbr'] is not None:
                    country.abbr = args['abbr']

                if 'flag' in args and args['flag'] is not None:
                    country.flag = args['flag']

                country.save()

                update_country = {
                    'id': country.id,
                    'name': country.name,
                    'abbreviation': country.abbr,
                    'flag': country.flag
                }

                return jsonify(
                    {
                        'code': 200,
                        'code_mesaage': "Successful",
                        'data': update_country
                    }
                ), 200

        except DataError:
            return {
                'code': 500,
                'code_message': "Wrong DataType",
                'message': "A datatype error has occur, check the input and try again."  # noqa
                }, 500

        except Forbidden as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'code_message': e.message
            }

        except Conflict as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_message': e.message
            }

        except InternalServerError as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_message': e.message
            }

    def delete(id=None):
        """ delete one countries by id """

        try:
            country = TeamModel.query.filter_by(id=id).first()

            if not country:
                return jsonify(
                    {
                        'code': 404,
                        'code_message': "Data Not Found",
                        'message': f"The country with id {id} was found in the database"  # noqa
                    }
                ), 404

            country.delete()

            return jsonify(
                {
                    'code': 200,
                    'code_mesaage': "Successful",
                    'message': "The country with id {id} was found in the database and was deleted"  # noqa
                }
            ), 200

        except DataError:
            return {
                "error message": "Wrong ID format",
                "message": "The Id you are trying to retrieve is invalid, check UUID correct format."  # noqa
                }, 500

        except DataNotFound as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message,
                'message': f"The country with id {id} was found in the database"  # noqa
            }

        except Forbidden as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message
            }

        except InternalServerError as e:
            return {
                'code': e.code,
                'type': e.type,
                'code_mesaage': e.message
            }
