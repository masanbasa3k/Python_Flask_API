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