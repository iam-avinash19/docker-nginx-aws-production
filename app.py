from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Level 2 Project 🚀 Docker + Nginx + AWS"

app.run(host="0.0.0.0", port=5000)