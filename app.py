from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Jenkins Pipeline!"

if __name__ == "__main__":
    app.run(port=5000)
