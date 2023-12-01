from . import app
import os
import json
from flask import jsonify, request, make_response

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################

@app.route("/")
def index():
    return jsonify(dict(status="OK")), 200

@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    return data

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    return data[id]


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    # Extracting picture data from request body
    picture_data = request.get_json()
    # Check if picture with the same id exists
    for picture in data:
        if picture['id'] == picture_data['id']:
            return jsonify({"Message": f"picture with id {id} already present"}), 302
    print("picture data",picture_data)
    # Appending picture data to the data list
    data.append(picture_data)
    return jsonify({"Message": f"Picture with id {id} created successfully"}), 200


######################################################################
# UPDATE A PICTURE
7######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    picture_data = request.get_json()
    f = False
    for picture in data:
        if picture['id'] == id:
            picture.update(picture_data)
            f = True
            break
    # If picture doesn't exist, return 404 status code
    if not f:
        return jsonify({"message": "picture not found"}), 404
    return jsonify({"message": f"Picture with id {id} updated successfully"}), 200


######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    f = False
    for picture in data:
        if picture['id'] == id:
            del data[id]
            f = True
            break
    if not f:
        return jsonify({"message": "picture not found"}), 404
    return jsonify({"message": "picture Deleted"}), 204
