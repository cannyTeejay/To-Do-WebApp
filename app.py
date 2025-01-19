from flask import Flask,render_template,redirect,url_for,request


app = Flask(__name__)




tasks = []

@app.route("/home", methods=["GET","POST"])
def home():
    return render_template("index.html",tasks=tasks)

@app.route("/",methods = ["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/signin",methods = ["GET","POST"])
def signin():
    return render_template("signin.html")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/add_task",methods = ["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
        return redirect(url_for("home"))
    return redirect(url_for("home"))

@app.route("/delete_task/<string:task>", methods = ["POST"])
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)