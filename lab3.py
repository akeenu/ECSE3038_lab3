from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from marshmallow import Schema, fields, ValidationError
from bson.json_util import dumps
from json import loads

profile_db = {
    "success": True,
    "data": {
        "last_updated": "2/3/2021, 8:48:51 PM",
        "username": "Akeenu Allen",
        "role": "Electronics Engineer",
        "color": "Burgundy"
    }
}

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://supm:qwerty123@cluster0.ejobu.mongodb.net/lab3?retryWrites=true&w=majority"
mongo = PyMongo(app)

class TankScheama(Schema):
    Location = fields.String()
    Latitude = fields.String()
    Longitude = fields.String()
    Percent_full = fields.Integer()

@app.route("/home")
def home():
    return "welcome home"

@app.route("/tanks") ##methods=["POST"]
def get_tanks():
    mongo.db.tanks.find()
    tanks = mongo.db.tanks.find()
    return jsonify(loads(dumps(tanks)))

@app.route ("/tanks", methods = ["POST"])
def add_Tank ():
    try:
        nwTank = TankScheama().load(request.json)
        tank_ID = mongo.db.tanks.insert_one(nwTank).inserted_id
        tank = mongo.db.tanks.find_one(tank_ID)
        return loads(dumps(tank))
    except ValidationError as ve:
         return ve.messages, 400

@app.route ("/tanks/<ObjectId:id>", methods = ["PATCH"])
def update_tank(id):
    mongo.db.tanks.update_one({"_id": id}, {"$set": request.json})
    tank = mongo.db.tanks.find_one(id)
    return loads(dumps(tank))

@app.route ("/tanks/<ObjectId:id>", methods = ["DELETE"])
def delete_tank(id):
    results = mongo.db.tanks.delete_one({"_id": id})
    if results.deleted_count == 1:
       return {
           "Success": True
        }
    else:
        return {
               "Success": False
            }, 400

if __name__ =="__main__" :
    app.run (port=3000, debug = True )



















#/class ProfileScheama(Schema):
  #  Username = fields.String
 #   fav_colour = fields.String
 #   Role = fields.String

#@app.route("/fruit", methods=["POST"])
#def add_fruit():
    #try:

#@app.route("/fruit/<ObjectId:id>", methods=["PATCH"])
#def update_fruit(id):
 #   mongo.db.fruits.update_one({"_id": id},{"$set": request.json})
#    fruit = mongo.db.fruits.find_one(id) 

#@app.route("/fruit/<ObjectId:id>", methods=["DELETE"])
#def delete_fruit(id):


  #  mongo.db.fruits.find()


#if __name__ == "__main__":
 #   app.run(debug=True)##
