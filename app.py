from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

recipes = {
    'recipe_id': '0',
    'recipe_name': 'Wagyu Strip Steak',
    'recipe_type': 'Dinner',
    'ingredients': 'Wagyu Strip, Salt, Pepper, Olive Oil',
    'instructions':'Heat Pan. Add 1 tablespoon of olive oil. Once oil is smoking add steak and cook for 3 minutes per side. Let rest for 5 minutes.',
}

@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    return(jsonify(recipes))


if __name__ == "__main__":
    app.run(port = 5000)