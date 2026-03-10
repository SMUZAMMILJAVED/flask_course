from flask import Flask,request,render_template
from dotenv import load_dotenv
from pymongo import MongoClient
import os
load_dotenv()
app=Flask(__name__)
uri=os.getenv("MONGO_URI")
client=MongoClient(uri)
db=client['student_db']
students_collection=db['students']
@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        name=request.form["std_name"]
        fName=request.form["f_name"]
        course=request.form["course"]
        students_collection.insert_one({
            'name':name,
            "fName":fName,
            "course":course
        })

    return render_template('index.html')
@app.route('/students')
def students():
    std_data=students_collection.find()
    return render_template('students.html',students=std_data)

if __name__=="__main__":
    app.run(debug=True)