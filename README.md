# Fatmug Assignment

Note: My sytem is not supporting docker, I know how to dockerize but, i think system is not comptible with docker version, I tried in many ways.

This is a simple Python project that demonstrates Video Upload and Processing, Search Functionality, List View for Uploaded Videos

## Features
- Developed a website that allows users to upload videos, which will be processed in the background. After processing and extracting subtitles from the video
- Added search feature on the website that enables users to search for a phrase within the video and retrieve the timestamp of its occurrence
- Implement a list view for uploaded video files. When a video file is selected, it should retrieve the corresponding video and subtitles

## Installation

To get started with this project:

1. Clone the repository:
   ```bash
   git clone https://github.com/Narcy-github/Fatmug
   cd Fatmug
2. Create a virtual environment and activate it
    ```
    python -m venv venv
    venv\Scripts\activate
3. Install the dependencies
   ```
   pip install -r requirements.txt
4. Configure the database in settings.py
   ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
5. Run Migrations
   ```
   python manage.py migrate

6. Create a Superuser
   ```
   python manage.py createsuperuser

7. Run the Server
   ```
   python manage.py runserver

Contact
GitHub: (https://github.com/Narcy-github) Email: narsimha.parswapu@gmail.com



