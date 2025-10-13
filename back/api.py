from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Bem-vindo à API FlexMedia!")

@app.route("/health")
def health():
    return jsonify(status="ok", service="flexmedia", version="1.0.0")

@app.route("/echo/<texto>")
def echo(texto):
    return jsonify(echo=texto)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

