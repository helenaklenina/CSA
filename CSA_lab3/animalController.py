from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)


class Animal(db.Model):
    type = db.Column(db.String(64))
    name = db.Column(db.String(64), unique=True)
    price = db.Column(db.Float)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, type, name, price):
        self.name = name
        self.type = type
        self.price = price


class AnimalSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'name', 'price')


animal_schema = AnimalSchema()
animal_schema = AnimalSchema(many=True)


# Add new animal
@app.route('/animals/add_animal', methods=['POST'])
def add_animal():
    data = request.get_json()
    type = data['type']
    name = data['name']
    price = data['price']

    new_animal = Animal(type, name, price)

    db.session.add(new_animal)
    db.session.commit()
    return json.dumps('Added'), 200


# See all animals in shop
@app.route('/animals', methods=['GET'])
def get_animals():
    all_animals = Animal.query.all()
    result = animal_schema.dump(all_animals)
    return jsonify(result)

# See all animals of current type
@app.route('/animals/<type>', methods=['GET'])
def type_animals(type):
    animals = []
    animals = Animal.query.filter_by(type=type).all()
    result = animal_schema.dump(animals)
    return jsonify(result)


# See information about current animal
@app.route('/animals/<id>', methods=['GET'])
def get_animal(id):
    animal = Animal.query.get(id)
    print(animal)
    return animal_schema.jsonify(animal)


# Update information about animal
@app.route('/animals/edit_price/<id>', methods=['PUT'])
def update_price_animal(id):
    data = request.get_json()
    new_price = data['price']
    animal = Animal.query.filter_by(id=id).all()[0]
    animal.price = new_price
    db.session.commit()
    return json.dumps('Edited'), 200

# Update information about animal
@app.route('/animals/edit_name/<id>', methods=['PUT'])
def update_name_animal(id):
    data = request.get_json()
    new_name = data['name']
    animal = Animal.query.filter_by(id=id).all()[0]
    animal.name = new_name
    db.session.commit()
    return json.dumps('Edited'), 200


# Buy the animal
@app.route('/animals/buy/<id>', methods=['DELETE'])
def buy_animal(id):
    animal = Animal.query.get(id)
    db.session.delete(animal)
    db.session.commit()
    return json.dumps('Deleted'), 200


if __name__ == '__main__':
    app.run(debug=True)
