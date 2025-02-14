from flask import Flask, request, jsonify
import os
from processor import format_document

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    formatted_doc = format_document(filepath)

    return jsonify({"message": "File processed", "output": formatted_doc}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5070, debug=True)
