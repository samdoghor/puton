"""src/resources/index.py

Keyword arguments:
argument -- None
Return: 200 Status
"""

from flask import jsonify
from flask_restful import Resource


class IndexResource(Resource):
    """ This class check if home endpoint is running """

    @staticmethod
    def home():
        """ Test for 200 status code """

        return jsonify(
            {
                'code': 200,
                'code_message': 'Successful',
                'message': 'Server is running'
            }
        ), 200
