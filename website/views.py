from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
import secrets

secret_key = secrets.token_hex(16)
def validate_token(token):
    return token == secret_key

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user, token=secret_key)

def load_sample_data():
    with open('data.json', 'r') as file:
        return json.load(file)
sample_data = load_sample_data()


# API endpoint with authentication
@views.route('/api/data', methods=['GET'])
def get_data():
    token = request.headers.get('Authorization')

    if token and validate_token(token):
        return jsonify(sample_data)
    else:
        return jsonify({"message": "Unauthorized"}), 401
    
@views.route('/api/data', methods=['POST'])
def create_data():
    token = request.headers.get('Authorization')
    if token and validate_token(token):
        # Extract the data from the request and process it
        # Example: data = request.get_json()
        # Process the data and save it to the database
        return jsonify({"message": "Data created successfully"}), 201
    else:
        return jsonify({"message": "Unauthorized"}), 401

@views.route('/api/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    token = request.headers.get('Authorization')
    if token and validate_token(token):
        # Extract the updated data from the request and process it
        # Example: data = request.get_json()
        # Process the data and update the corresponding data in the database
        return jsonify({"message": "Data updated successfully"}), 200
    else:
        return jsonify({"message": "Unauthorized"}), 401

@views.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    token = request.headers.get('Authorization')
    if token and validate_token(token):
        # Delete the corresponding data from the database
        return jsonify({"message": "Data deleted successfully"}), 200
    else:
        return jsonify({"message": "Unauthorized"}), 401
