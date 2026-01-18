from flask import Flask
from app.routes import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")
def home():
    return {"message": "Traffic Accident Backend Running"}

if __name__ == "__main__":
    app.run()
