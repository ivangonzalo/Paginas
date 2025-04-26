from flask import Flask, request, jsonify, render_template
from collections import deque
import os

app = Flask(__name__)

# Últimos 100 valores recibidos
datos = deque(maxlen=100)

@app.route("/")
def home():
    return "¡Hola! La API está funcionando. Usa /ver para ver los datos."

@app.route("/data", methods=["GET"])
def recibir_dato():
    valor = request.args.get("sensor")
    if valor:
        try:
            valor_float = float(valor)
            datos.append(valor_float)
            print("Dato recibido:", valor_float)
            return f"Dato recibido correctamente: {valor}"
        except ValueError:
            return "Valor inválido", 400
    return "No se recibió el valor 'sensor'", 400

@app.route("/ver")
def ver():
    return render_template("index.html")

@app.route("/api/datos")
def api_datos():
    return jsonify(list(datos))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usar el puerto de Render o 5000 si no está definido
    app.run(host="0.0.0.0", port=port)

