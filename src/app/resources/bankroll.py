# resources-bankroll.py

"""
This module defines the financial mgt. of the user
"""


# imports

from flask import Blueprint, render_template

bankroll_blueprint = Blueprint("bankroll", __name__)

@bankroll_blueprint.route("/bankrolls", methods=['GET'])
def view_finance():
    
    
    return render_template('/pages/bankroll.html')


@bankroll_blueprint.route("/bankrolls/add-new", methods=['GET', 'POST'])
@bankroll_blueprint.route("/bankrolls/<string:name>", methods=['GET'])
