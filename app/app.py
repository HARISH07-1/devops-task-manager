from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

DB_PATH = "tasks.db"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create_task():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]

        conn = sqlite3.connect(DB_PATH)

        conn.execute(
            "INSERT INTO tasks(title, description) VALUES (?, ?)",
            (title, description)
        )

        conn.commit()
        conn.close()

        return redirect("/tasks")

    return render_template("create.html")


@app.route("/tasks")
def tasks():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    all_tasks = cursor.fetchall()

    conn.close()

    return render_template(
        "tasks.html",
        tasks=all_tasks
    )


@app.route("/delete/<int:id>")
def delete_task(id):

    conn = sqlite3.connect(DB_PATH)

    conn.execute(
        "DELETE FROM tasks WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/tasks")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_task(id):

    if request.method == "POST":

        status = request.form["status"]

        conn = sqlite3.connect(DB_PATH)

        conn.execute(
            "UPDATE tasks SET status=? WHERE id=?",
            (status, id)
        )

        conn.commit()
        conn.close()

        return redirect("/tasks")

    return render_template("update.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
