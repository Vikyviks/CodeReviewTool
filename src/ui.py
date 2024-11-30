from flask import Flask, request, jsonify
from static_analysis import analyze_code
from code_scanner import scan_code
import os

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    """
    API endpoint to scan code for issues.
    """
    file_path = request.json.get("file_path")
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    static_analysis_results = analyze_code(file_path)
    custom_scan_results = scan_code(file_path, "rules.json")

    return jsonify({
        "static_analysis": static_analysis_results,
        "custom_scan": custom_scan_results
    })

if __name__ == "__main__":
    app.run(debug=True)

