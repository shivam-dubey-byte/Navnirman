from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def AboutUs():
    return render_template('AboutUs.html',home='',about='active',donate="",contact="")
@app.route("/history")
def history():
    return render_template('History.html',home='active',about='',donate="",contact="")
    #,home='active',about='',blog='',contact='',donate=""
@app.route("/donate")
def donate():
    return render_template("donate.html",home='',about='',donate="active",contact="")


if __name__ == '__main__':
    app.run(debug=True)
