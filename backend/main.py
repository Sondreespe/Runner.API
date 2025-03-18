from flask import request,jsonify
from config import app,db
from models import Runs

#show sessions
@app.route("/runs", methods=["GET"])
def get_runs():
    runs = Runs.query.all()
    json_runs = list(map(lambda x: x.to_json(), runs))
    return jsonify({"runs": json_runs})


#add runs
@app.route("/add", methods=["POST"])
def add_run():
    title = request.json.get("title")
    distance = request.json.get("distance")
    time = request.json.get("time")
    note = request.json.get("note")

    if not time or not distance or not title:
        return(
            jsonify({"message": "you must enter time, distandce and a title"}), 400,
        )
    
    new_run = Runs(title=title, distance = distance, time = time, note= note)
    try:
        db.session.add(new_run)
        db.session.commit()
    except Exception as e:
        return jsonify({"message" : str(e)}), 400
    
    return jsonify({"message": "Session added"}), 201

# update runs
@app.route("/update_run/<int:run_id>", methods=["PATCH"])
def update_run(run_id):
    run = Runs.query.get(run_id)

    if not run:
        return jsonify({"message": "Session not found"}),404
    
    #updates what is updated
    data= request.json
    run.title = data.get("title", data.title)
    run.distance = data.get("distance", data.distance)
    run.time = data.get("time", data.time)
    run.note = data.get("note", data.note)

    db.session.commit()

    return jsonify({"message": "Run updated"}),200

#deleting runs

@app.route("/delete_run/<int:run_id>", methods=["DELETE"])
def delete_contact(run_id):
    run = Runs.query.get(run_id)

    if not run:
        return jsonify({"message": "Run not found"}),404

    db.session.delete(run)
    db.session.commit()

    return jsonify({"message": "Run deleted"}),200

 
if __name__ == "__main__":
    with app.app_context():
        db.create_all()



    app.run(debug=True)


