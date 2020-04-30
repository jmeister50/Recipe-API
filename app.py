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
    #TODO---- Add user help string. 

@app.route('/recipes/<int:recipe_id>', methods=['PATCH'])
def update_recipe(recipe_id):
    request_data = request.get_json()
#    print(request_data)

    if("ingredients" in request_data):
        Recipe.update_recipe_ingredients(recipe_id, request_data['ingredients'])
    if("instructions" in request_data):
        Recipe.update_recipe_instructions(recipe_id, request_data['instructions'])
    if("recipe_name" in request_data):
        Recipe.update_recipe_name(recipe_id, request_data['recipe_name'])
    response = Response("", status=204)
    response.headers['Location'] = "/recipes/" + str(recipe_id)
    return response

#DELETE 

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    if Recipe.delete_recipe(recipe_id):
        response = Response("", status=204)
        return response
    invalidBookObjectErrorMsg = {

        "error": "Recipe with the ID provided was not found."

    }
    
    response = Response("", status=404, mimetype= 'application/json')
    return response;



if __name__ == "__main__":
    app.run(port = 5000,debug=True)