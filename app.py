from flask import Flask, render_template, jsonify, request
import random

words=[]

templates = [
    {
        "inputs":5,
        "category":"Sports",
        "word":"Chess"
    },
    {
        "inputs":6,
        "category":"European Country Name",
        "word":"France"
    },
    {
        "inputs":9,
        "category":"Sports",
        "word":"Badminton"
    },
    {
        "inputs":8,
        "category":"A part of Art and Craft",
        "word":"Painting"
    },
    {
        "inputs":7,
        "category":"The most important part in the 3 divisions of Science",
        "word":"Biology"
    },
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status":"success",
        "word":random.choice(templates)
    })


if __name__ == "__main__":
    app.run(debug=True)