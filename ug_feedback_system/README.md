# UG Feedback System

## ⚡ Quick Look
- Centralizes course feedback flows for administrators, faculty, and students.
- Automates test data bootstrapping via create_test_users.py for rapid onboarding.
- Ships with ready-to-use HTML templates and static assets for a responsive UI.

## 🧩 Features
- Role-aware dashboards for admins, faculty, and students.
- Feedback collection, audit logging, and reporting in one place.
- Modular routing and service layers built for maintainability.

## 🛠️ Tech Stack
| Layer | Stack |
| --- | --- |
| Backend | 🐍 Python · ⚙️ Flask |
| Database | 🗃️ SQLite (via db/connection.py) |
| Frontend | 🎨 Jinja2 templates · HTML · CSS · JavaScript |
| Tooling | 🧪 Virtualenv · 📦 Requirements from requirements.txt |

## 🚀 Getting Started
1. Clone this repository or download the source.
2. Install Python 3.10+ if you have not already.

### Step 1 · Create the virtual environment
- macOS or Linux:

        python3 -m venv .venv

- Windows (PowerShell):

        py -m venv .venv

### Step 2 · Activate the virtual environment
- macOS or Linux:

        source .venv/bin/activate

- Windows (PowerShell):

        .\.venv\Scripts\Activate.ps1

- Windows (Command Prompt):

        .\.venv\Scripts\activate.bat

### Step 3 · Enter the application directory

    cd ug_feedback_system

    ##step 3.1  create .env file and add paste following content

    DB_HOST=localhost
    DB_PORT=3306
    DB_USER=root
    DB_PASSWORD=your_password
    DB_NAME=ug_feedback_db
        

### Step 4 · Initialize the database and seed demo data

    python create_test_users.py

### Step 5 · Run the development server

    python app.py

The app listens on the host and port configured in config.py. Adjust settings such as database paths or secret keys there if needed.

## 📂 Project Layout Highlights
- Entry point: [app.py](app.py)
- Configuration: [config.py](config.py)
- Database layer: [db/connection.py](db/connection.py)
- Blueprints: [routes](routes) and [services](services)
- Static assets: [static](static)
- Templates: [templates](templates)

## ✅ Next Steps
- Review requirements.txt and install any missing system dependencies.
- Create real administrator accounts via the admin UI or custom scripts.
- Configure production-ready settings for secret management, logging, and deployment.
