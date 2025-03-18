from config import db

class Runs(db.Model):
    id           = db.Column(db.Integer, primary_key = True)
    distance     = db.Column(db.Integer,unique = False, nullable = False)
    time         = db.Column(db.Integer,unique = False, nullable = False)
    note         = db.Column(db.String(100), unique= False, nullable= True) #optional

    def to_json(self):
        return{
            "id": self.id,
            "title": self.title,
            "distance": self.distance,
            "time": self.time,
            "note": self.note,
        }