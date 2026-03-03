from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    # return "hello world!"
    return render_template('index.html')

@app.route('/about')
def about():
    return "about route!"

@app.route('/blog')
def blog():
    # return "blog route!"
     return render_template('blog.html')

@app.route('/user/<name>')
def user(name):
    return f"hello {name}"
if __name__=="__main__":
    app.run(debug=True)
