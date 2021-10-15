from chess import app
from flask import render_template
@app.route("/")
def Home():
    return  render_template('Home.html')

@app.route("/About")
def About():
    return render_template('About.html')
@app.route("/Teachers")
def Teachers():
    return render_template('Teachers.html')
@app.route("/Contact")
def Contact():
    return render_template('Contact.html')
