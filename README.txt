README.txt for Outfit Recommender System Based on Machine Learning

Overview

-This Django project provides a personalized outfit recommendation system, allowing users to explore and select outfits based on their preferences. Features include user profiles, outfit liking functionality, and a dynamic recommendation engine that leverages advanced text analysis techniques.

Requirements

-To run this project, ensure you have the following installed:

    Python 3.x
    Django 4.x
    Additional dependencies listed in *requirements.txt*

Getting Started

1. Copy the Project
Begin by copying the entire project folder from the CD to your local machine.
2. Set Up a Virtual Environment
It's recommended to create a virtual environment to manage project dependencies:

Setting up Virtual Environment

    # For Windows
    In Terminal : python -m venv virtual 
    
    # For macOS/Linux
    In Terminal : python3 -m venv virtual

#tip: you can name your virtual environment as you preferred as sample name is "virtual"


3. Activate the Virtual Environment

    Windows:
    In Terminal : venv\Scripts\activate

    macOS/Linux:
    In Terminal : source venv/bin/activate

4. Install Dependencies
    Install the required dependencies from *requirements.txt*:
    In Terminal : pip install -r requirements.txt

5. Database Setup
    If you are using SQLite (the default), the db.sqlite3 file is included, so you can skip this step. If using a different database, ensure your settings in settings.py are correctly configured.

6. Run Migrations
    To apply any pending migrations, execute:
    In Terminal : python manage.py migrate

7. Collect Statics
    To access to static files (e.g css files, images), you need to execute this command in terminal.
    In Terminal : python manage.py collectstatic

8. Run the Development Server
    Start the Django development server with:
    In Terminal : python manage.py runserver

    You can then access the application in your web browser at http://127.0.0.1:8000/.

Additional Notes
    To create a superuser account for accessing the admin interface, run:
    In Terminal : python manage.py createsuperuser

    You can access the admin dashboard in your web browser at http://127.0.0.1:8000/admin

Ensure that static files are properly configured to be served.