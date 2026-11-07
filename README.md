# CampusConnect

**Full name:** Precious Ann S. Tolentino  
**Section:** G1  
**Course:** CSIT327

A Django application with sign-up, login, a dashboard, and a profile page.
Authenticated users can edit their own username, first name, last name, and email through
a class-based `UpdateView`. Pages share a Bootstrap 5 base template and navbar.
Successful sign-up and profile updates display Bootstrap alerts.

## Run locally

Use Python 3.12 or newer. The following commands are for Windows PowerShell.

1. Clone the repository and enter its folder:

   ```powershell
   git clone https://github.com/dellisyoss/CSIT327-G1-Tolentino-Precious-FirstDjango.git
   cd CSIT327-G1-Tolentino-Precious-FirstDjango
   ```

2. Create a virtual environment and install dependencies:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Generate a local secret key file (do this once for a new checkout):

   ```powershell
   .\.venv\Scripts\python.exe -c "from pathlib import Path; from django.core.management.utils import get_random_secret_key; Path('.env').write_text('DJANGO_SECRET_KEY=' + get_random_secret_key() + '\n', encoding='utf-8')"
   ```

   `.env` is ignored by Git. You may instead set the `DJANGO_SECRET_KEY`
   environment variable; it takes priority over the value in `.env`.
   `.env.example` documents the required variable without including a secret.

4. Create the database tables and start the development server:

   ```powershell
   .\.venv\Scripts\python.exe manage.py migrate
   .\.venv\Scripts\python.exe manage.py runserver
   ```

5. Open http://127.0.0.1:8000/accounts/signup/ and create an account.
   Log in, then select **Edit Profile** on the dashboard.

The database is created locally by migrations. Virtual environments, Python
cache files, local databases, and secret files should remain outside Git.
These settings are for local development (`DEBUG = True`).
