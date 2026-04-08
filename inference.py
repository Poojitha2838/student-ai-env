from flask import Flask, request, jsonify
from student_env import StudentEnv

app = Flask(_name_)

env = StudentEnv()

@app.route("/reset", methods=["POST"])
def reset():
    global env
    env = StudentEnv()
    state = env.reset()
    return jsonify({"state": state})

@app.route("/step", methods=["POST"])
def step():
    global env
    data = request.get_json(silent=True)

    # Handle empty request safely
    if not data:
        action = "study"
    else:
        action = data.get("action", "study")

    state, reward, done = env.step(action)

    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# IMPORTANT: force correct startup
if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8000, debug=False)
