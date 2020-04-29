from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import json
from configs import app

db = SQLAlchemy(app)

class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.String, primary_key=True)
    recipe_name = db.Column(db.String, nullable=False)
    recipe_type = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)

    def json(self):
        return{
        'recipe_id': self.recipe_id,
        'recipe_name': self.recipe_name,
        'recipe_type': self.recipe_type,
        'ingredients': self.ingredients,
        'instructions': self.instructions
        }

    def get_all_recipes():
        return [Recipe.json(recipes) for recipes in Recipe.query.all()]

    def add_recipe(_recipe_id, _recipe_name, _recipe_type, _ingredients, _instructions):
        new_recipe = Recipe(
            
            recipe_id=_recipe_id,
            recipe_name=_recipe_name,
            recipe_type=_recipe_type, 
            ingredients=_ingredients,
            instructions=_instructions
            )

        db.session.add(new_recipe)
        db.session.commit()

    def __repr__(self):
        recipe_object = {
        'recipe_id': self.recipe_id,
        'recipe_name': self.recipe_name,
        'recipe_type': self.recipe_type,
        'ingredients': self.ingredients,
        'instructions': self.instructions
        }

        return json.dumps(recipe_object)