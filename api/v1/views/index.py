#!/usr/bin/python3
"""
Index.py to create flask and connect to API
"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


apiText = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def api_Status():
    """
    apiStatus
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def apiStats():
    """apiStats"""
    return_dict = {}
    for key, value in apiText.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)

if __name__ == "__main__":
    pass
