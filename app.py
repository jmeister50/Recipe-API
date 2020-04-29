from flask import Flask, jsonify, request, Response
import json
import configs as cfg
from recipe_model import *

app = cfg.app

@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    return(jsonify({'recipes': Recipe.get_all_recipes()}))

@app.route('/recipes', methods=['POST'])
def add_recipe():
    request_data = request.get_json()
    Recipe.add_recipe(
        
    request_data['recipe_id'],
    request_data['recipe_name'],
    request_data['recipe_type'],
    request_data['ingredients'],
    request_data['instructions']
        
    )
        
    response = Response("", 201, mimetype='application/json')
    response.headers['Location'] = "/recipes/" + str(request_data['recipe_id'])
    return response
    """else: 
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object passed in request.",
            "helpString": "Data passed in similar to this {'name': 'bookname', 'price': 7.99, 'isbn': 789456123"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json');
        return response"""


if __name__ == "__main__":
    app.run(port = 5000,debug=True)