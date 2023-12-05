from . import app
from . import db
from flask import jsonify, request, make_response,render_template

obj = db.dataBase()  # Creating an object

@app.route("/")
def index():
    dataMdb = obj.findData()
    return render_template('index.html', dataMdb=dataMdb)

@app.route("/find/<int:id>", methods=["GET"])
def findeOne(id):
    data = obj .findOneData(id)
    return data

@app.route("/insert/<int:id>", methods=["GET"])
def inserOne(id):
    insertData = obj.inserOneData(id)
    if insertData :
        return {"inserted id": f"data with {id} inserted"}, 201
    return {"Message": f"data with id {id} already present"}, 302

@app.route("/delete/<int:id>", methods=["GET"])
def deleteOne(id):
    deletedata = obj.deleteOneData(id)
    if deletedata.deleted_count == 0 :
        return jsonify({"message": "data not found"}), 404
    return jsonify({"message": "data deleted"}), 202

@app.route("/update/<int:id>", methods=["GET"])
def updateOne(id):
    updateData = obj.updateOneData(id)
    if updateData.matched_count == 0 :
        return jsonify({"message": "data not found"}), 404
    return jsonify({"message": "data updated"}), 202
