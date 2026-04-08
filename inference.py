from flask import Flask, request, jsonify
from student_env import StudentEnv

app = Flask(__name__)

env = None

@app.route("/reset", methods=["POST"])
@app.route("/reset/", methods=["POST"])
def reset():
    global env
    try:
        env = StudentEnv()
        state = env.reset()
        return jsonify({
            "state": state,
            "success": True
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


@app.route("/step", methods=["POST"])
@app.route("/step/", methods=["POST"])
def step():
    global env
    try:
        data = request.get_json(silent=True)

        if not data:
            action = "study"
        else:
            action = data.get("action", "study")

        state, reward, done = env.step(action)

        return jsonify({
            "state": state,
            "reward": round(float(reward), 2),  # IMPORTANT
            "done": bool(done),
            "success": True
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
