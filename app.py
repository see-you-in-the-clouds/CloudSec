import os
import json
from flask import Flask, request, send_file, render_template
from rules import validate_json
from report import generate_report

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"json"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def upload_form():
    """Serve the HTML upload form."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    """Handle file upload, process JSON, and return a downloadable report."""
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]
    if file.filename == "" or not allowed_file(file.filename):
        return "Invalid file type", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    with open(file_path, "r") as f:
        json_data = json.load(f)

    violations = validate_json(json_data)  # ✅ Only checking explicitly defined paths
    report_path = generate_report(file_path, violations)

    # Send report & delete both files after response
    response = send_file(report_path, as_attachment=True)
    cleanup_files([file_path, report_path])  # Cleanup after sending report

    return response


def cleanup_files(files):
    """Delete files from disk."""
    for file in files:
        if os.path.exists(file):
            os.remove(file)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)


def cleanup_files(files):
    """Delete files from disk."""
    for file in files:
        if os.path.exists(file):
            os.remove(file)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
