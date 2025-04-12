# Notes App

A Django‑based web application for managing personal notes.  
Built with a clean MVC structure, it supports user authentication, note tagging, live AJAX search, and is ready for caching and test coverage.

---

## Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Getting Started](#getting-started)  
4. [Project Structure](#project-structure)  
5. [Usage](#usage)  
6. [Future Improvements](#future-improvements)  

---

## Features

- **User Authentication**:  
  - Registration, login, logout  
  - Email and password change  
- **Notes Management**:  
  - Create, edit, delete, view notes  
  - Add and manage tags per note  
- **Live Search**:  
  - AJAX‑powered instant search by note title  
  - Keyword filtering via tags  
- **Responsive UI**:  
  - Mobile‑first design  
- **Ready for Enhancement**:  
  - Core MVC in place  
  - Upcoming: caching layer & full test suite  

---

## Tech Stack

- **Backend**:  
  - Django  
  - Django REST Framework  
- **Frontend**:  
  - HTML5, CSS3, JavaScript (vanilla AJAX)  
- **Database**:  
  - SQLite (easily swap to PostgreSQL or MySQL)  
- **Dependencies**:  
  - See [requirements.txt](requirements.txt)  

---

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/g3rberr/notes.git
   cd notes

    Create & activate a virtual environment

    python3 -m venv venv
    source venv/bin/activate

Install dependencies

    pip install -r requirements.txt

Apply migrations

    python manage.py migrate

Create a superuser (optional)

    python manage.py createsuperuser

Run the development server

    python manage.py runserver

    Open http://127.0.0.1:8000/ in your browser.

## Project Structure

    notes/
    ├── core/           # Project settings & URL routing
    ├── note/           # Notes app (models, views, templates)
    ├── users/          # Custom user app (auth, profile, email/password change)
    ├── static/         # Static files (CSS, JS)
    ├── templates/      # Global templates
    ├── manage.py
    └── requirements.txt

## Usage

    Register a new account or login with existing credentials.

    Change email/password from your profile settings.

    Create notes, assign tags, and search instantly by title via the search box.

    Filter by tag by clicking on a tag label.

## Future Improvements

    Integrate a caching layer (Redis) for faster note listing.

    Add unit & integration tests (Pytest / Unittest).

    Enhance UI with a modern frontend framework (e.g., React or Vue).

    Deploy to Docker and CI/CD pipeline.
