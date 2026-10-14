from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
@app.route('/')
def dashboard():
    conn = sqlite3.connect("attendance.db")

    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        "SELECT * FROM attendance ORDER BY date DESC"
    ).fetchall()

    conn.close()

    total_present = sum(1 for r in rows if r["status"] == "Present")
    
    total_absent = sum(1 for r in rows if r["status"] == "Absent")

    return render_template(
        "dashboard.html",
        records=rows,
        total_present=total_present,
        total_absent=total_absent,
    )

if __name__ == "__main__":
    app.run(debug=True)