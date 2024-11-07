from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('Home.html',home='active',about='',blog='',contact='',donate="",contact="")
@app.route("/about")
def about1():
    return render_template('AboutUs.html',home='',about='active',donate="",contact="")
    #,home='active',about='',blog='',contact='',donate=""
@app.route("/donate")
def donate():
    return render_template("donate.html",home='',about='',contact='',donate="active",contact="")


if __name__ == '__main__':
    app.run(debug=True)
