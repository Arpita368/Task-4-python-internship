# User Management App 📋

## Overview
This is a simple Flask-based web application for managing user data.  
It provides a browser-based interface to:
- View all users
- Add new users
- Edit existing users
- Delete users

The data is stored in memory (dictionary/list) — no database required.

---

## Features
✅ View users in a table format  
✅ Add users via a form  
✅ Update user details using an edit form  
✅ Remove users with one click  
✅ Simple and lightweight — no external database needed  

---

## Requirements
- Python 3.x  
- Flask library  

---

## Installation
1. Clone or download the project files to your computer.  
2. Install Flask:  
   ```bash
   pip install flask

## Running the App
1. Open a terminal in the project folder.
2. Run: python app.py
3. Open your browser and go to: http://127.0.0.1:5000/

## How to Use
**1. View Users**
A table shows all current users with ID, Name, Email, and Actions.

**2. Add User**
Fill out the "Add User" form and click Add.

**3. Edit User**
Click Edit next to a user, update the details, and click Update.

**4. Delete User**
Click Delete next to a user to remove them.

## Notes
Since data is stored in memory, all changes are lost when the server restarts.
Can be extended to use SQLite, MySQL, or PostgreSQL for persistence.

## Author
Created by Arpita Jitendra Sonparote

## License
This script is for educational purposes. You can use it or modify it as per your requirement.
