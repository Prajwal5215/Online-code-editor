from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    code = request.json.get("code")
    lang = request.json.get("language")  # Get selected language

    try:
        if lang == "Python":
            # Run Python code
            result = subprocess.run(
                ["python", "-c", code],
                capture_output=True, text=True
            )
        elif lang == "JavaScript":
            # Run JavaScript code with Node.js
            result = subprocess.run(
                ["node", "-e", code],
                capture_output=True, text=True
            )
        else:
            return jsonify({"output": "❌ Unsupported language selected."})

        return jsonify({"output": result.stdout + result.stderr})

    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
