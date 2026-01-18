from flask import Blueprint, jsonify
from .analysis import accidents_by_hour

api = Blueprint("api", __name__)

@api.route("/api/accidents/hourly", methods=["GET"])
def hourly_accidents():
    return jsonify(accidents_by_hour())
