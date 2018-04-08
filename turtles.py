from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def take():
    return render_template("root.html")

@app.route('/ninja')
def all_ninjas():
    return render_template("all_ninjas.html")

@app.route('/ninja/<color>')
def color(color):
    if color == "blue":
        url = "blue.html"
    elif color == "orange":
        url = "orange.html"
    elif color == "red":
        url = "red.html"
    elif color == "purple":
        url = "purple.html"
    else:
        url = "notapril.html"


    return render_template(url)





app.run(debug=True) # run our server