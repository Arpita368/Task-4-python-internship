from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# In-memory user list
users = [
    {"id": 1, "name": "Arjun", "email": "arjun@gmail.com"},
    {"id": 2, "name": "Priya", "email": "priya@gmail.com"}
]

# HTML template
template = """
<!DOCTYPE html>
<html>
<head>
    <title>User Management</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 50%; margin-bottom: 20px; }
        table, th, td { border: 1px solid #ccc; padding: 8px; }
        th { background: #f2f2f2; }
        input { padding: 5px; margin: 5px; }
        button { padding: 5px 10px; }
    </style>
</head>
<body>
    <h2>User List</h2>
    <table>
        <tr>
            <th>ID</th><th>Name</th><th>Email</th><th>Actions</th>
        </tr>
        {% for user in users %}
        <tr>
            <td>{{ user.id }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>
                <form action="/delete/{{ user.id }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
                <form action="/edit/{{ user.id }}" method="GET" style="display:inline;">
                    <button type="submit">Edit</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>

    <h2>Add User</h2>
    <form action="/add" method="POST">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit">Add</button>
    </form>

    {% if edit_user %}
    <h2>Edit User</h2>
    <form action="/update/{{ edit_user.id }}" method="POST">
        <input type="text" name="name" value="{{ edit_user.name }}" required>
        <input type="email" name="email" value="{{ edit_user.email }}" required>
        <button type="submit">Update</button>
    </form>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(template, users=users, edit_user=None)

@app.route("/add", methods=["POST"])
def add_user():
    new_id = users[-1]["id"] + 1 if users else 1
    users.append({"id": new_id, "name": request.form["name"], "email": request.form["email"]})
    return redirect("/")

@app.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return redirect("/")

@app.route("/edit/<int:user_id>")
def edit_user(user_id):
    user_to_edit = next((u for u in users if u["id"] == user_id), None)
    return render_template_string(template, users=users, edit_user=user_to_edit)

@app.route("/update/<int:user_id>", methods=["POST"])
def update_user(user_id):
    for user in users:
        if user["id"] == user_id:
            user["name"] = request.form["name"]
            user["email"] = request.form["email"]
            break
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
