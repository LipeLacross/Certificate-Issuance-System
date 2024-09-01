# Certificate Issuance System

The Certificate Issuance System is a web application that allows for the creation, management, and viewing of certificates. It is designed to facilitate the issuance of certificates for course completions, training, and other events.

## 🔨 Project Features

- **List Certificates**: Retrieves a list of all certificates stored in the system.
- **Create Certificate**: Adds a new certificate based on provided information.
- **Certificate Details**: Displays details of a specific certificate.
- **Update Certificate**: Updates information of an existing certificate.
- **Delete Certificate**: Removes a specific certificate from the system.

### Visual Example of the Project

![Screenshot 2024-08-18 150159](https://github.com/user-attachments/assets/8083860d-a3c1-4ae3-a62b-3b0ee0d7829e)
![Screenshot 2024-08-18 145650](https://github.com/user-attachments/assets/d168fc0a-06a0-41f5-9ff3-fe5419e16b32)
![Screenshot 2024-08-18 150624](https://github.com/user-attachments/assets/8f8503ad-dafa-49d4-a4b6-5df94417383a)

## ✔️ Techniques and Technologies Used

- **Flask**: Web framework for creating the API server.
- **SQLAlchemy**: ORM for interacting with the MySQL database.
- **MySQL**: Relational database for storing certificates.
- **Python**: Primary programming language used in the development of the application.

## 📁 Project Structure

- **app/**: Contains the source code for the application, including database configuration, models, routes, and resources.
    - **`__init__.py`**: Initializes the Flask application and configures the database.
    - **`database.py`**: Database configuration and connection.
    - **`models.py`**: Data model definitions.
    - **`resources.py`**: API resources.
    - **`routes.py`**: API routes definition and control logic.
    - **templates/**: Contains the HTML files used by the application.
- **.venv/**: Virtual environment containing project dependencies.
- **.gitignore**: File to ignore files and directories in version control.
- **LICENSE**: Project license.
- **README.md**: Project documentation.
- **requirements.txt**: List of project dependencies.
- **run.py**: Script to start the Flask server.

## 🛠️ Running the Project

1. Clone the repository to your local environment.
2. Install the dependencies listed in the `requirements.txt` file.
3. Configure the MySQL database and adjust credentials in the `app/database.py` file.
4. Start the Flask server by running the `run.py` script.

   The server will be available at `http://127.0.0.1:5000`.

## 🌐 Deployment

For deployment in a production environment, consider using a WSGI server like Gunicorn and a web server like Nginx. Additionally, configure an accessible MySQL database for the application and adjust environment settings as necessary.
