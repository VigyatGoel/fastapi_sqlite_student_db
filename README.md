# FastAPI with Database

This is API made using FastAPI in python. It can be used to connect to a local sqlite database runninng on your computer.

## Features

- Async await support for fast response time and query performance.
- uses sqlite3 database with databases library for storing and retrieving data asynchronously.
- CRUD operations on student database.
- uses all latest available fastapi features and practices. 

## Requirements

- python 3.11 or above

## Installation

1. Clone the repository:

  ```bash
  https://github.com/VigyatGoel/fastapi_sqlite_student_db.git
  ```
## Running the API

1. Navigate to the root directory of the project:
  ```bash
   cd fastapi_sqlite_student_db
   ```
2. Install all required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigation to my_app package:
   ```bash
   cd my_app
   ```
4. Setup the Database:
   ```bash
   python3 setup.py
   ```
5. Navigate back to root directory of the project:
   ```bash
   cd ..
   ```
7. Run the API:
   ```bash
   fastapi dev my_app
   ```
8. You can access the api at the following url:
   ```bash
   http://127.0.0.1:8000
   ```
9. Docs will be available at:
   ```bash
   http://127.0.0.1:8000/docs
   ```

## Contributing

Contributions to Quick Note are welcome!
If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository or submit a pull request with your changes.

## License

Quick Note is released under the MIT License.
