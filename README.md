# Food Search Application

This is a Django-based web application that allows users to search for dishes from various restaurants. Users can sign up, log in, and search for dishes based on their names.

## Features

- User authentication (sign up, log in, log out)
- Search for dishes
- Display search results with pagination
- Containerized setup using Docker

## Requirements

- Python 3.10+
- Django 4.2+
- Docker (for containerized setup)

## Running the Project Locally

### 1. Using Virtual Environment (venv)

#### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/NikhilSingh2004/SearchAdminPanel.git
    cd SearchAdminPanel
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables:**

    Create a `.env` file in the `search` directory and add the following variables:

    ```plaintext
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

6. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

### 2. Using Docker

#### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/NikhilSingh2004/SearchAdminPanel.git
    cd SearchAdminPanel
    ```

2. **Build the Docker image:**

    ```bash
    docker-compose build
    ```

3. **Run the Docker containers:**

    ```bash
    docker-compose up
    ```

    The application will be available at `http://127.0.0.1:8000/`.

4. **Apply database migrations:**

    In a new terminal, run:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

## Project Structure

- `search/`: Contains the Django project settings and URLs.
- `core/`: Contains the main application views, models, and templates.
- `api/`: Contains the API views and serializers for user registration.
- `templates/`: Contains the HTML templates.

## Docker Configuration

- `Dockerfile`: Defines the Docker image.
- `docker-compose.yml`: Defines the Docker services.

## Environment Variables

Make sure to set the following environment variables in your `.env` file:

- `SECRET_KEY`: Your Django secret key.
- `DEBUG`: Set to `True` for development, `False` for production.
