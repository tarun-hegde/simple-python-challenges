Python Challenges Setup Guide
---


## Prerequisites

Make sure you have the following installed on your machine:
- Python (>= 3.6)
- pip (Python package installer)

## Project Setup

Follow these steps to set up and run the tasks:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Set Up Virtual Environment

It is recommended to use a virtual environment to keep your dependencies isolated. If you don’t have `virtualenv` installed, you can install it with:

```bash
pip install virtualenv
```

Create and activate a virtual environment:

- For macOS/Linux:
    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

- For Windows:
    ```bash
    virtualenv venv
    venv\Scripts\activate
    ```

### 3. Install Dependencies

After activating the virtual environment, install all necessary dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Running Tasks

If you want to run task1, task2 or task3

```bash
cd <tasknumber>
```

This applies for all tasks except task3
```bash
python <filename>.py
```

For task3 follow the steps below

#### Apply Migrations

To apply the database migrations, run the following command:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Create a Superuser (Optional)

To create a superuser for accessing the Django Admin interface:

```bash
python manage.py createsuperuser
```

#### Run the Development Server

To start the development server, use:

```bash
python manage.py runserver
```

You can now visit `http://127.0.0.1:8000/` in your browser to view the application.

### 5. Deactivate the Virtual Environment

When you're done, you can deactivate the virtual environment by running:

```bash
deactivate
```
