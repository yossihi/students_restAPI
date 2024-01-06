# Students Management System

This application is a simple CRUD (Create, Read, Update, Delete) system for managing student records. It uses Flask, SQLAlchemy for database management, and Flask-CORS for enabling Cross-Origin Resource Sharing. The system allows users to perform basic operations on student data, including adding, deleting, and updating records.

## Setup

### Prerequisites

- Python 3.x
- Flask
- Flask-CORS
- Flask-SQLAlchemy

### Installation

1. Clone the repository:
 "git clone https://github.com/your-username/students-management.git"

 
2. Install dependencies:
"pip install -r requirements.txt"


### Configuration

- Database configuration:
- By default, the application uses SQLite. To switch to MySQL, modify the `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py`.
- Make sure to create the necessary tables by running `db.create_all()` within the app context.

### Usage

1. Run the application:
    "python app.py"


2. Access the application in your web browser at `http://localhost:5000`.

### API Endpoints

- `GET /` - Retrieve all student records.
- `POST /add` - Add a new student record.
- `DELETE /delete/<int:studID>` - Delete a student record by ID.
- `POST /update/<int:studID>` - Update a student record by ID.

### Schema

- `Students` Table:
- `id` - Primary key (autoincrement)
- `name` - Student name (String, 100 characters)
- `city` - City (String, 50 characters)
- `addres` - Address (String, 200 characters)
- `photo` - Photo file name (String, 500 characters)

### Additional Notes

- Uploaded images are stored in the `/static/images` directory.

### Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request.


