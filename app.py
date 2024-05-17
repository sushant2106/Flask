from flask import Flask,request,jsonify
from  flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.app_context().push()
db=SQLAlchemy(app)
db.create_all()

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),unique=True)
    role=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f'User {self.username}'
    

    

@app.route('/user',methods=["POST"])
def user():
    name=request.json.get("username",None)
    role=request.json.get("role",None)
    new_user=User(username=name,role=role)
    db.session.add(new_user)
    db.session.commit()


@app.route('/add')
def fun():
    return "I am add"







if __name__=='__main__': 
    app.run(debug=True)