import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import date

def init_db():
    conn = sqlite3.connect("attendance.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_name TEXT,
            date TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def mark_attendance(status):

    name = name_entry.get()

    if not name.strip():
        messagebox.showwarning("Missing name", "Please enter an employee name.")
        return

    conn = sqlite3.connect("attendance.db")
    conn.execute(
        "INSERT INTO attendance (employee_name, date, status) VALUES (?, ?, ?)",
        (name, str(date.today()), status),
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Saved", f"{name} marked as {status} for today.")

    name_entry.delete(0, tk.END)

window = tk.Tk()

window.title("Employee Attendance")

window.geometry("300x180")

tk.Label(window, text="Employee Name:").pack(pady=5)

name_entry = tk.Entry(window, width=30)

name_entry.pack(pady=5)

tk.Button(
    window,
    text="Mark Present",
    command=lambda: mark_attendance("Present")
).pack(pady=5)

tk.Button(
    window,
    text="Mark Absent",
    command=lambda: mark_attendance("Absent")
).pack(pady=5)

init_db()
window.mainloop()