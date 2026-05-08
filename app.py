import os
import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request, redirect, url_for, flash, session
import jinja2

# ------------------- Configuration -------------------
# Password for accessing the application.
# It's better to set this via an environment variable for security.
APP_PASSWORD = os.environ.get('APP_PASSWORD', 'admin123')

DB_CONFIG = {
    'host': 'localhost',
    'database': 'University_Clubs',
    'user': 'root',
    'password': 'Netone2004#*'
}

# ------------------- Embedded HTML Templates -------------------
TEMPLATES = {
    'base.html': '''<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Club Manager{% endblock %}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #3a3a3a;
            color: #333;
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .app-container {
            display: flex;
            flex: 1;
            max-width: 1400px;
            margin: 20px auto;
            background-color: #f0f0f0;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .sidebar {
            width: 260px;
            background: #2c2c2c;
            color: #ddd;
            padding: 20px 0;
            display: flex;
            flex-direction: column;
        }
        .sidebar-header {
            padding: 0 20px 20px 20px;
            border-bottom: 1px solid #555;
            margin-bottom: 20px;
        }
        .sidebar-header h2 {
            color: white;
            font-size: 1.5rem;
            margin: 0;
        }
        .sidebar-header p {
            color: #aaa;
            font-size: 0.9rem;
            margin-top: 5px;
        }
        .nav-links {
            list-style: none;
            flex: 1;
        }
        .nav-links li {
            margin: 5px 0;
        }
        .nav-links a {
            display: block;
            padding: 10px 20px;
            color: #ddd;
            text-decoration: none;
            transition: all 0.2s;
            border-left: 4px solid transparent;
        }
        .nav-links a:hover {
            background: #3f3f3f;
            color: white;
            border-left-color: #f0f0f0;
        }
        .user-info {
            padding: 15px 20px;
            border-top: 1px solid #555;
            font-size: 0.9rem;
            color: #aaa;
        }
        .user-info a {
            color: #ddd;
            text-decoration: none;
        }
        .user-info a:hover {
            color: white;
        }
        .main-content {
            flex: 1;
            background: #f9f9f9;
            padding: 25px;
            min-height: 500px;
        }
        .flash {
            list-style: none;
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
            border-radius: 4px;
            padding: 12px 15px;
            margin-bottom: 20px;
        }
        .flash.error {
            background: #f8d7da;
            color: #721c24;
            border-color: #f5c6cb;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 1px 5px rgba(0,0,0,0.1);
        }
        th {
            background: #4f4f4f;
            color: white;
            padding: 12px 8px;
            font-weight: 600;
            text-align: left;
        }
        td {
            padding: 10px 8px;
            border-bottom: 1px solid #ccc;
        }
        tr:nth-child(even) { background-color: #f2f2f2; }
        tr:hover { background-color: #e6e6e6; }
        input[type="text"], input[type="number"], input[type="date"], input[type="password"], select, textarea {
            padding: 8px 10px;
            border: 1px solid #aaa;
            border-radius: 4px;
            background: white;
            font-size: 14px;
            width: 100%;
            max-width: 300px;
        }
        input:focus, select:focus {
            border-color: #666;
            outline: none;
            box-shadow: 0 0 5px #aaa;
        }
        input[type="submit"], button, .button {
            background: #4f4f4f;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: background 0.2s;
        }
        input[type="submit"]:hover, button:hover, .button:hover { background: #2c2c2c; }
        a { color: #2c2c2c; }
        a:hover { color: #000; }
        h1, h2, h3 { color: #2c2c2c; margin-bottom: 15px; }
        footer {
            background: #2c2c2c;
            color: #aaa;
            text-align: center;
            padding: 15px;
            font-size: 0.9em;
            border-top: 1px solid #555;
            margin-top: auto;
        }
        @media (max-width: 700px) {
            .app-container { flex-direction: column; }
            .sidebar { width: 100%; }
            .nav-links a { border-left: none; border-bottom: 1px solid #444; }
        }
    </style>
</head>
<body>
    <div class="app-container">
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>🎓 Club Manager</h2>
                <p>University Clubs</p>
            </div>
            <ul class="nav-links">
                {% if session.get('logged_in') %}
                <li><a href="{{ url_for('index') }}">🏠 Home</a></li>
                <li><a href="{{ url_for('students') }}">👥 Students</a></li>
                <li><a href="{{ url_for('instructors') }}">👨‍🏫 Instructors</a></li>
                <li><a href="{{ url_for('activities') }}">📅 Activities</a></li>
                <li><a href="{{ url_for('memberships') }}">🔗 Memberships</a></li>
                <li><a href="{{ url_for('audit') }}">📋 Audit Log</a></li>
                <li><a href="{{ url_for('moderator_budget') }}">💰 Moderator Budget</a></li>
                <li><a href="{{ url_for('club_details_view') }}">🔍 Club Details View</a></li>
                {% else %}
                <li><a href="{{ url_for('login') }}">🔐 Login</a></li>
                {% endif %}
            </ul>
            <div class="user-info">
                {% if session.get('logged_in') %}
                Logged in | <a href="{{ url_for('logout') }}">Logout</a>
                {% else %}
                Not logged in
                {% endif %}
            </div>
        </aside>
        <main class="main-content">
            {% with messages = get_flashed_messages(with_categories=true) %}
              {% if messages %}
                {% for category, message in messages %}
                  <ul class="flash {{ category }}">
                    <li>{{ message }}</li>
                  </ul>
                {% endfor %}
              {% endif %}
            {% endwith %}
            {% block content %}{% endblock %}
        </main>
    </div>
    <footer>&copy; 2026 University Clubs Management System</footer>
</body>
</html>''',

    'login.html': '''{% extends "base.html" %}
{% block title %}Login{% endblock %}
{% block content %}
<h1>Login</h1>
<form method="post">
    <label>Password:</label>
    <input type="password" name="password" required>
    <br><br>
    <input type="submit" value="Login">
    <br><br>
    <
</form>
{% endblock %}''',

    'index.html': '''{% extends "base.html" %}
{% block title %}Clubs{% endblock %}
{% block content %}
<h1>University Clubs</h1>
<table border="1">
    <tr><th>ID</th><th>Name</th><th>Meeting Day</th><th>Meeting Time</th></tr>
    {% for club in clubs %}
    <tr>
        <td>{{ club.club_id }}</td>
        <td>{{ club.club_name }}</td>
        <td>{{ club.meeting_day }}</td>
        <td>{{ club.meeting_time }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}''',

    'club_detail.html': '''{% extends "base.html" %}
{% block title %}{{ club.club_name }}{% endblock %}
{% block content %}
<h1>{{ club.club_name }}</h1>
<ul>
    <li><strong>Budget:</strong> {{ club.budget }}</li>
    <li><strong>Meeting:</strong> {{ club.meeting_day }} at {{ club.meeting_time }}</li>
    <li><strong>Moderator:</strong> {{ club.moderator_name }}</li>
</ul>
<p><a href="{{ url_for('index') }}">Back to clubs</a></p>
{% endblock %}''',

    'students.html': '''{% extends "base.html" %}
{% block title %}Students{% endblock %}
{% block content %}
<h1>Students</h1>
<table>
    <tr><th>ID</th><th>Name</th><th>Email</th><th>Reg No</th><th>Program</th><th>Year</th><th>Faculty</th></tr>
    {% for s in students %}
    <tr>
        <td>{{ s.student_id }}</td>
        <td>{{ s.fullname }}</td>
        <td>{{ s.email }}</td>
        <td>{{ s.reg_no }}</td>
        <td>{{ s.program }}</td>
        <td>{{ s.year_of_study }}</td>
        <td>{{ s.faculty }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}''',

    'instructors.html': '''{% extends "base.html" %}
{% block title %}Instructors{% endblock %}
{% block content %}
<h1>Instructors</h1>
<table>
    <tr><th>ID</th><th>Name</th><th>Email</th><th>Staff No</th><th>Department</th><th>Position</th><th>Salary</th></tr>
    {% for i in instructors %}
    <tr>
        <td>{{ i.instructor_id }}</td>
        <td>{{ i.fullname }}</td>
        <td>{{ i.email }}</td>
        <td>{{ i.staff_no }}</td>
        <td>{{ i.department }}</td>
        <td>{{ i.position }}</td>
        <td>{{ i.salary }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}''',

    'activities.html': '''{% extends "base.html" %}
{% block title %}Activities{% endblock %}
{% block content %}
<h1>Activities</h1>
<p><a href="{{ url_for('add_activity') }}"><button>Add New Activity</button></a></p>
<table>
    <tr><th>ID</th><th>Club</th><th>Type</th><th>Date</th><th>Time</th><th>Location</th></tr>
    {% for a in activities %}
    <tr>
        <td>{{ a.activity_id }}</td>
        <td>{{ a.club_name }}</td>
        <td>{{ a.activity_type }}</td>
        <td>{{ a.activity_date }}</td>
        <td>{{ a.activity_time }}</td>
        <td>{{ a.location }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}''',

    'add_activity.html': '''{% extends "base.html" %}
{% block title %}Add Activity{% endblock %}
{% block content %}
<h1>Add New Activity</h1>
<form method="post">
    <label>Club:</label>
    <select name="club_id" required>
        {% for club in clubs %}
        <option value="{{ club.club_id }}">{{ club.club_name }}</option>
        {% endfor %}
    </select><br><br>
    <label>Activity Type:</label> <input type="text" name="activity_type" required><br><br>
    <label>Date (YYYY-MM-DD):</label> <input type="text" name="activity_date" required><br><br>
    <label>Time (HH:MM:SS):</label> <input type="text" name="activity_time" required><br><br>
    <label>Location:</label> <input type="text" name="location"><br><br>
    <input type="submit" value="Add Activity">
</form>
{% endblock %}''',

    'memberships.html': '''{% extends "base.html" %}
{% block title %}Memberships{% endblock %}
{% block content %}
<h1>Club Memberships</h1>
<p><a href="{{ url_for('add_membership') }}"><button>Add New Membership</button></a></p>
<table>
    <tr><th>Student Name</th><th>Club</th><th>Joined Date</th><th>Role</th></tr>
    {% for m in members %}
    <tr>
        <td>{{ m.student_name }}</td>
        <td>{{ m.club_name }}</td>
        <td>{{ m.joined_id }}</td>
        <td>{{ m.role_in_club }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}''',

    'add_membership.html': '''{% extends "base.html" %}
{% block title %}Add Membership{% endblock %}
{% block content %}
<h1>Add a New Membership</h1>
<form method="post">
    <label>Student ID:</label> <input type="number" name="student_id" required><br><br>
    <label>Club ID:</label> <input type="number" name="club_id" required><br><br>
    <label>Role:</label> <input type="text" name="role" required><br><br>
    <input type="submit" value="Add Membership">
</form>
{% endblock %}''',

    'audit.html': '''{% extends "base.html" %}
{% block title %}Audit Log{% endblock %}
{% block content %}
<h1>Instructor Salary Audit Log</h1>
<table>
    <tr><th>Audit ID</th><th>Instructor ID</th><th>Old Salary</th><th>New Salary</th><th>Changed By</th><th>Change Time</th></tr>
    {% for log in logs %}
    <tr>
        <td>{{ log.audit_id }}</td>
        <td>{{ log.instructor_id }}</td>
        <td>{{ log.old_salary }}</td>
        <td>{{ log.new_salary }}</td>
        <td>{{ log.changed_by }}</td>
        <td>{{ log.change_time }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}''',

    'moderator_budget.html': '''{% extends "base.html" %}
{% block title %}Moderator Budget Summary{% endblock %}
{% block content %}
<h1>Total Budget per Moderator</h1>
<table>
    <tr><th>Instructor ID</th><th>Moderator Name</th><th>Total Budget of Clubs Moderated</th></tr>
    {% for m in summary %}
    <tr>
        <td>{{ m.instructor_id }}</td>
        <td>{{ m.fullname }}</td>
        <td>{{ m.total_budget }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}''',

    'add_club.html': '''{% extends "base.html" %}
{% block title %}Add Club{% endblock %}
{% block content %}
<h1>Add a New Club</h1>
<form method="post">
    <label>Club ID:</label> <input type="number" name="club_id" required><br><br>
    <label>Club Name:</label> <input type="text" name="club_name" required><br><br>
    <label>Budget:</label> <input type="number" step="0.01" name="budget" required><br><br>
    <label>Meeting Day:</label> <input type="text" name="meeting_day" required><br><br>
    <label>Meeting Time (HH:MM):</label> <input type="text" name="meeting_time" required><br><br>
    <label>Moderator ID:</label> <input type="number" name="moderator_id" required><br><br>
    <input type="submit" value="Add Club">
</form>
{% endblock %}''',

    'club_details_view.html': '''{% extends "base.html" %}
{% block title %}Club Details View{% endblock %}
{% block content %}
<h1>Club Details</h1>
<p><a href="{{ url_for('add_club') }}"><button>Add New Club</button></a></p>
<table>
    <tr><th>Club ID</th><th>Club Name</th><th>Budget</th><th>Meeting Day</th><th>Meeting Time</th><th>Moderator</th><th>Member Count</th></tr>
    {% for cd in details %}
    <tr>
        <td>{{ cd.club_id }}</td>
        <td>{{ cd.club_name }}</td>
        <td>{{ cd.budget }}</td>
        <td>{{ cd.meeting_day }}</td>
        <td>{{ cd.meeting_time }}</td>
        <td>{{ cd.moderator_name }}</td>
        <td>{{ cd.member_count }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}'''
}

# ------------------- Custom Jinja2 Loader -------------------
def loader_function(template_name):
    return TEMPLATES.get(template_name)

# ------------------- Flask Application -------------------
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'   # CHANGE TO A SECURE RANDOM KEY
app.jinja_loader = jinja2.FunctionLoader(loader_function)

# ------------------- Authentication Decorator -------------------
def login_required(f):
    """Decorator to require login for a route."""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ------------------- Database Helper Functions -------------------
def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Connection error: {e}")
        return None

# ----- Clubs -----
def get_all_clubs():
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Club")
    result = cursor.fetchall()
    cursor.close(); conn.close()
    return result

def get_club_details(club_id):
    conn = get_connection()
    if not conn: return None
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT c.*, u.fullname AS moderator_name
        FROM Club c
        JOIN Instructor i ON c.moderator_id = i.instructor_id
        JOIN users u ON i.instructor_id = u.user_id
        WHERE c.club_id = %s
    """
    cursor.execute(query, (club_id,))
    result = cursor.fetchone()
    cursor.close(); conn.close()
    return result

def update_club_budget(club_id, new_budget):
    conn = get_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Club SET budget = %s WHERE club_id = %s", (new_budget, club_id))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(e); conn.rollback(); return False
    finally:
        cursor.close(); conn.close()

def add_club(club_id, name, budget, day, time, mod_id):
    conn = get_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Club (club_id, club_name, budget, meeting_day, meeting_time, moderator_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (club_id, name, budget, day, time, mod_id))
        conn.commit()
        return True
    except Error as e:
        print(e); conn.rollback(); return False
    finally:
        cursor.close(); conn.close()

# ----- Memberships -----
def get_memberships():
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT s.student_id, u.fullname AS student_name,
               c.club_name, m.joined_id, m.role_in_club
        FROM Membership m
        JOIN Student s ON m.student_id = s.student_id
        JOIN users u ON s.student_id = u.user_id
        JOIN Club c ON m.club_id = c.club_id
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close(); conn.close()
    return result

def add_membership(student_id, club_id, role):
    conn = get_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Membership (student_id, club_id, joined_id, role_in_club)
            VALUES (%s, %s, CURDATE(), %s)
        """, (student_id, club_id, role))
        conn.commit()
        return True
    except Error as e:
        print(e); conn.rollback(); return False
    finally:
        cursor.close(); conn.close()

# ----- Students -----
def get_all_students():
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT s.student_id, u.fullname, u.email, s.reg_no, s.program, s.year_of_study, s.faculty
        FROM Student s
        JOIN users u ON s.student_id = u.user_id
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close(); conn.close()
    return result

# ----- Instructors -----
def get_all_instructors():
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT i.instructor_id, u.fullname, u.email, i.staff_no, i.department, i.position, i.salary
        FROM Instructor i
        JOIN users u ON i.instructor_id = u.user_id
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close(); conn.close()
    return result

# ----- Activities -----
def get_all_activities():
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT a.activity_id, a.activity_type, a.activity_date, a.activity_time, a.location,
               c.club_name, c.club_id
        FROM Activity a
        JOIN Club c ON a.club_id = c.club_id
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close(); conn.close()
    return result

def add_activity(club_id, activity_type, activity_date, activity_time, location):
    conn = get_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT MAX(activity_id) FROM Activity")
        max_id = cursor.fetchone()[0]
        new_id = (max_id + 1) if max_id else 1
        cursor.execute("""
            INSERT INTO Activity (activity_id, club_id, activity_type, activity_date, activity_time, location)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (new_id, club_id, activity_type, activity_date, activity_time, location))
        conn.commit()
        return True
    except Error as e:
        print(e); conn.rollback(); return False
    finally:
        cursor.close(); conn.close()

# ----- Audit Log -----
def get_audit_log():
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM InstructorAudit ORDER BY change_time DESC")
    result = cursor.fetchall()
    cursor.close(); conn.close()
    return result

# ----- Moderator Budget Summary -----
def get_moderator_budget_summary():
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT i.instructor_id, u.fullname, SUM(c.budget) AS total_budget
        FROM Instructor i
        JOIN users u ON i.instructor_id = u.user_id
        LEFT JOIN Club c ON i.instructor_id = c.moderator_id
        GROUP BY i.instructor_id
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close(); conn.close()
    return result

# ----- ClubDetails View -----
def get_club_details_view():
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ClubDetails")
    result = cursor.fetchall()
    cursor.close(); conn.close()
    return result

# ------------------- Routes -------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page – does not require authentication."""
    if request.method == 'POST':
        password = request.form.get('password')
        if password == APP_PASSWORD:
            session['logged_in'] = True
            flash('Login successful.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect password.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout – clears the session."""
    session.pop('logged_in', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html', clubs=get_all_clubs())

@app.route('/club/<int:club_id>')
@login_required
def club_detail(club_id):
    club = get_club_details(club_id)
    if club:
        return render_template('club_detail.html', club=club)
    flash('Club not found', 'error')
    return redirect(url_for('index'))

@app.route('/update_budget', methods=['POST'])
@login_required
def update_budget():
    try:
        club_id = int(request.form['club_id'])
        new_budget = float(request.form['new_budget'])
        if update_club_budget(club_id, new_budget):
            flash('Budget updated successfully', 'success')
        else:
            flash('Update failed (club not found or error)', 'error')
    except ValueError:
        flash('Invalid number format', 'error')
    return redirect(url_for('index'))

@app.route('/students')
@login_required
def students():
    return render_template('students.html', students=get_all_students())

@app.route('/instructors')
@login_required
def instructors():
    return render_template('instructors.html', instructors=get_all_instructors())

@app.route('/activities')
@login_required
def activities():
    return render_template('activities.html', activities=get_all_activities())

@app.route('/add_activity', methods=['GET', 'POST'])
@login_required
def add_activity():
    if request.method == 'POST':
        try:
            club_id = int(request.form['club_id'])
            act_type = request.form['activity_type']
            act_date = request.form['activity_date']
            act_time = request.form['activity_time']
            location = request.form['location']
            if add_activity(club_id, act_type, act_date, act_time, location):
                flash('Activity added successfully', 'success')
            else:
                flash('Error adding activity', 'error')
        except ValueError:
            flash('Invalid input', 'error')
        return redirect(url_for('activities'))
    return render_template('add_activity.html', clubs=get_all_clubs())

@app.route('/memberships')
@login_required
def memberships():
    return render_template('memberships.html', members=get_memberships())

@app.route('/add_membership', methods=['GET', 'POST'])
@login_required
def add_membership():
    if request.method == 'POST':
        try:
            student_id = int(request.form['student_id'])
            club_id = int(request.form['club_id'])
            role = request.form['role']
            if add_membership(student_id, club_id, role):
                flash('Membership added successfully', 'success')
            else:
                flash('Error adding membership', 'error')
        except ValueError:
            flash('Invalid input. Please enter numbers for IDs.', 'error')
        return redirect(url_for('memberships'))
    return render_template('add_membership.html')

@app.route('/audit')
@login_required
def audit():
    return render_template('audit.html', logs=get_audit_log())

@app.route('/moderator_budget')
@login_required
def moderator_budget():
    return render_template('moderator_budget.html', summary=get_moderator_budget_summary())

@app.route('/club_details_view')
@login_required
def club_details_view():
    return render_template('club_details_view.html', details=get_club_details_view())

@app.route('/add_club', methods=['GET', 'POST'])
@login_required
def add_club():
    if request.method == 'POST':
        try:
            club_id = int(request.form['club_id'])
            name = request.form['club_name']
            budget = float(request.form['budget'])
            day = request.form['meeting_day']
            time = request.form['meeting_time']
            mod_id = int(request.form['moderator_id'])
            if add_club(club_id, name, budget, day, time, mod_id):
                flash('Club added successfully', 'success')
            else:
                flash('Error adding club (possible duplicate ID or invalid moderator)', 'error')
        except ValueError:
            flash('Invalid input. Please check your numbers.', 'error')
        return redirect(url_for('club_details_view'))
    return render_template('add_club.html')

# ------------------- Run -------------------
if __name__ == '__main__':
    app.run(debug=True)