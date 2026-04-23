from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
DB_CONFIG = {
    'host': 'database-1.c5gcqk2q4wru.us-east-1.rds.amazonaws.com',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'port': 5432
}

@app.route("/")
def home():
    return jsonify(message="Bem-vindo à API!")

@app.route("/health")
def health():
    return jsonify(status="ok", service="AULA CLOUD AWS", version="1.0.0")

@app.route("/echo/<texto>")
def echo(texto):
    return jsonify(echo=texto)

@app.route("/usuarios")
def get_usuarios():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT id, username FROM usuarios;")
        rows = cur.fetchall()
        usuarios = [ {"id": row[0], "username": row[1]} for row in rows ]
        cur.close()
        conn.close()
        return jsonify(usuarios=usuarios)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)