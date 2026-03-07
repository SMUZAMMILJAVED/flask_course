from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/',methods=['POST',"GET"])
def home():
    if request.method =="POST":
        name=request.form['uname']
        password=request.form['upassword']
        return render_template('result.html',name=name,password=password)
        # return f"username is {name} and password is {password}"
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)