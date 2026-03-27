# Rare Server (API for Rare: The Publishing Platform for the Discerning Writer)

## About
The Rare API is a vanilla Python server using SQLite as its database. It handles all data management for the Rare publishing platform.

---

## Features
- User registration and authentication
- Full CRUD for posts
- Full CRUD for categories
- Full CRUD for tags
- Full CRUD for comments

---

## Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

---

## Getting Started

1. Clone the [repository](https://github.com/NSS-Day-Cohort-79/Rare-for-Python-api-mldbax) 

1. Run `pipenv shell` to start the virtual environment
1. Run `pipenv install` to install the dependencies
1. Run `sqlite3 db.sqlite3 < loaddata.sql` to create and seed the database
1. Open the project in VS Code
1. Open `json-server.py` in VS Code
1. Open the Run and Debug panel (Cmd+Shift+D on Mac / Ctrl+Shift+D on Windows)
1. Click the green play button to start the debugger
1. Make sure the [Rare Client](https://github.com/NSS-Day-Cohort-79/Rare-for-Python-client-mldbax) is also running
    1. The API will be available at http://localhost:8088

---
## Contributors
- [Dakota Seagraves](https://github.com/TheDakotaSeagraves)
- [Larissa Ferreira](https://github.com/larisssssa)
- [Cory Drumright](https://github.com/cmdrumright)
- [Maggie Flatt](https://github.com/MaggieFlatt-Dev)