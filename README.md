
# QuizWorld - A Django-based Quiz Application

## Overview
QuizSite is a web-based quiz application built with Django. Users can register or log in to access a variety of quiz categories. Upon selecting a category, random questions are presented from the database. After completing the quiz, the user can view their score.

### Features:
1. **User Registration and Login:**
   - New users can register an account.
   - Registered users can log in to access the application.
     <img width="947" alt="1quizreg" src="https://github.com/user-attachments/assets/76f8f09e-385d-4f51-8335-2ed8ea7fa38a" />

2. **Quiz Categories:**
   - Users can choose from different categories of quizzes.
     <img width="947" alt="2quiz" src="https://github.com/user-attachments/assets/229d9b0c-3f2c-4d17-8f01-cf2656dd5a17" />

   - Random questions from the selected category are displayed.
     ![3 quiz](https://github.com/user-attachments/assets/6ee71f02-9845-4b2a-b8d7-994f924e2123)

3. **Score Display:**
   - At the end of the quiz, the user's score is displayed.
     <img width="932" alt="4 quiz" src="https://github.com/user-attachments/assets/f7b78ffb-51dd-420c-b86b-2d4296f55cb0" />


## How to Run the Project Locally

### Prerequisites
Ensure you have Python installed on your system.

### Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Meldindavidsabu/QuizSite-Django.git
   ```

2. **Set Up a Virtual Environment:**
   Navigate to the project directory and create a virtual environment:
   ```bash
   cd QuizSite-Django
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Requirements:**
   Install the dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Database:**
   - Ensure your database is set up and the connection details are correctly configured in `settings.py`.
   - Apply database migrations to set up the necessary tables:
     ```bash
     py manage.py migrate (incase you are using the old version it is - python manage.py migrate)
     ```

6. **Run the Application:**
   Start the development server:
   ```bash
   py manage.py runserver (incase you are using the old version it is - python manage.py runserver)
   ```

7. **Access the Site:**
   Follow the link that appeared on your terminal.


## Immediate Improvements

1. **Dashboard for Logged-in Users:**
   - Implement a dashboard where logged-in users can view their previous quiz details, including scores and categories attempted.

## Requirements
The application depends on the following packages:
- `asgiref==3.8.1`
- `Django==5.1.4`
- `django-widget-tweaks==1.5.0`
- `mysqlclient==2.2.6`
- `sqlparse==0.5.3`
- `tzdata==2024.2`

---

