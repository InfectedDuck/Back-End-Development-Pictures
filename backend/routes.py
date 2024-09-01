from . import app
import os
import json
from flask import jsonify, request

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")

# Load the data from the JSON file
with open(json_url, "r") as f:
    data = json.load(f)

######################################################################
# RETURN HEALTH OF THE APP
######################################################################
@app.route("/health")
def health():
    return jsonify(status="OK"), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################
@app.route("/count")
def count():
    """Return length of data"""
    if data:
        return jsonify(length=len(data)), 200
    return jsonify(message="Internal server error"), 500

######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data), 200

######################################################################
# GET A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    picture = next((item for item in data if item["id"] == id), None)
    if picture:
        return jsonify(picture), 200
    return jsonify(message="Picture not found"), 404
######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    if not request.is_json:
        return jsonify({"message": "Invalid content type"}), 400
    
    new_picture = request.get_json()
    existing_picture = next((item for item in data if item["id"] == new_picture["id"]), None)
    
    if existing_picture:
        return jsonify({"Message": f"picture with id {new_picture['id']} already present"}), 302
    
    data.append(new_picture)
    return jsonify(new_picture), 201

######################################################################
# UPDATE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    if not request.is_json:
        return jsonify({"message": "Invalid content type"}), 400
    
    updated_picture = request.get_json()
    existing_picture = next((item for item in data if item["id"] == id), None)
    
    if existing_picture:
        # Update the existing picture with new data
        index = data.index(existing_picture)
        data[index] = updated_picture
        return jsonify(updated_picture), 200
    
    return jsonify({"message": "picture not found"}), 404

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    global data
    picture_to_delete = next((item for item in data if item["id"] == id), None)
    
    if picture_to_delete:
        data = [item for item in data if item["id"] != id]
        
        # Optional: Write updated data back to the JSON file
        with open(json_url, "w") as f:
            json.dump(data, f, indent=4)
        
        return '', 204
    
    return jsonify({"message": "Picture not found"}), 404
