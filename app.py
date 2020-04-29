from flask import Flask, jsonify, request, Response
import json
import configs as cfg

app = cfg.app

@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    return(jsonify(recipes))


if __name__ == "__main__":
    app.run(port = 5000)