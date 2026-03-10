from flask import Flask,render_template,request
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
app=Flask(__name__)
uri=os.getenv("MONGO_URI")
client=MongoClient(uri)
db = client["student_db"]
students_collection = db["students"]
@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        name=request.form['uname']
        password=request.form['upass']
        students_collection.insert_one({
            "name":name,
            "password":password
        })
        return "data saved in Database"
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)