from flask import Flask, request, jsonify
from flask_cors import CORS
from schema import schema

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def graphql_server():
    try:
        data = request.get_json()
        print("\n Petición recibida:")
        print(data)

        if not data or "query" not in data:
            return jsonify({"error": "No query found"}), 400

        result = schema.execute(
            data.get("query"),
            variable_values=data.get("variables"),
            operation_name=data.get("operationName")
        )

        response = {}
        if result.errors:
            response["errors"] = [str(e) for e in result.errors]
        if result.data:
            response["data"] = result.data

        return jsonify(response)

    except Exception as e:
        print("Excepción:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Servidor ejecutándose en http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)