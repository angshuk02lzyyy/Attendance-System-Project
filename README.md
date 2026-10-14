# Employee Attendance System 🏢

A hybrid desktop + web application for managing employee attendance. Mark attendance offline through a Tkinter desktop GUI, and view reports through a Flask web dashboard — both sharing the same SQLite database.

---

## 🚀 Features

- 🖥️ **Desktop App** — Tkinter GUI to mark employees as Present or Absent
- 🌐 **Web Dashboard** — Flask-powered browser dashboard to view all attendance records
- 🟢 **Color Coded Status** — Present shown in green, Absent in red
- 🗄️ **Shared Database** — Both apps read/write the same SQLite database
- 📅 **Auto Date Stamping** — Today's date is automatically recorded with each entry
- 📊 **Summary Count** — Total Present and Absent count shown at the top of dashboard

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Desktop App | Tkinter (Python built-in) |
| Web Dashboard | Flask (Python) |
| Database | SQLite (Python built-in) |
| Frontend | HTML, CSS, Jinja2 |
| Tools | Git, GitHub |

---

## 📁 Project Structure

```
Attendance_System_Project/
├── desktop_app.py         # Tkinter desktop GUI — mark attendance
├── server.py              # Flask web server — view attendance dashboard
├── templates/
│   └── dashboard.html     # Attendance table with color coded status
├── attendance.db          # SQLite database (auto-created, not committed)
├── .gitignore
└── venv/
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)
- Tkinter and SQLite are built into Python — no extra install needed

### 1. Clone the repository
```bash
git clone https://github.com/angshuk02lzyyy/employee-attendance-system.git
cd employee-attendance-system
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install flask
```

### 4. Run the desktop app
```bash
python desktop_app.py
```
A desktop window opens — type an employee name and click Mark Present or Mark Absent.

### 5. Run the web dashboard (separate terminal)
```bash
python server.py
```

### 6. Open dashboard in browser
```
http://localhost:5001
```

---

## 🖥️ How It Works

```
desktop_app.py  →  writes to  →  attendance.db  →  read by  →  server.py
(Tkinter GUI)                   (SQLite database)              (Flask dashboard)
```

1. Open the Tkinter desktop app
2. Type an employee name
3. Click **Mark Present** or **Mark Absent**
4. A confirmation popup appears
5. Open the web dashboard to see all records in a table

---

## 📊 Database Schema

```sql
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    date TEXT,
    status TEXT
);
```

---

## 🌐 Web Dashboard Routes

| Method | Route | Description |
|---|---|---|
| GET | `/` | Shows full attendance table with summary |

---

## 👨‍💻 Author

**Angshuk Chakraborty**  
📧 angshuk02@gmail.com  
🔗 [GitHub](https://github.com/angshuk02lzyyy)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).