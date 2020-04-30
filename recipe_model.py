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

    def delete_recipe(_recipe_id):
        is_successful = Recipe.query.filter_by(recipe_id=_recipe_id).delete()
        db.session.commit()
        return bool(is_successful)

    def update_recipe_instructions(_recipe_id, _instructions):
        recipe_to_update = Recipe.query.filter_by(recipe_id=_recipe_id).first()
        recipe_to_update.instructions = _instructions 
        db.session.commit()

    def update_recipe_ingredients(_recipe_id, _ingredients):
        recipe_to_update = Recipe.query.filter_by(recipe_id=_recipe_id).first()
        recipe_to_update.ingredients = _ingredients 
        db.session.commit()

    def update_recipe_name(_recipe_id, _recipe_name):
        recipe_to_update = Recipe.query.filter_by(recipe_id=_recipe_id).first()
        recipe_to_update.recipe_name = _recipe_name 
        db.session.commit()

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