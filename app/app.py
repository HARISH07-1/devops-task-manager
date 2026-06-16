from prometheus_client import Counter, generate_latest
from flask import Response

tasks_created = Counter(
    "tasks_created_total",
    "Total number of tasks created"
)

app_requests = Counter(
    "app_requests_total",
    "Total application requests"
)

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
    app_requests.inc()
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create_task():
    tasks_created.inc()

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
    app_requests.inc()

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
    app_requests.inc()

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
    app_requests.inc()

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

def init_db():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'Pending'
    )
    """)

    conn.commit()
    conn.close()



@app.route("/metrics")
def metrics():

    return Response(
        generate_latest(),
        mimetype="text/plain"
    )

if __name__ == "__main__":

    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
