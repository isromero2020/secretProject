from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    print(f"Received input: {name}")
    return f"Thanks, {name}!"

if __name__ == "__main__":
    app.run()
