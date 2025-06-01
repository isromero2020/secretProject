from flask import Flask, render_template, redirect, url_for
import json
import os
import time

app = Flask(__name__)

STATE_FILE = "state.json"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {"isGirlfriend": False, "startTime": None}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

@app.route("/", methods=["GET"])
def index():
    state = load_state()
    if state["isGirlfriend"]:
        return render_template("girlfriend.html", start_time=state["startTime"])
    else:
        return render_template("index.html")

@app.route("/make-girlfriend", methods=["POST"])
def make_girlfriend():
    state = load_state()
    state["isGirlfriend"] = True
    state["startTime"] = int(time.time() * 1000)  # current time in milliseconds
    save_state(state)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
