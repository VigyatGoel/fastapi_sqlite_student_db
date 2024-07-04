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
## End Points

1. ### The API is available at: ###
  ```bash
  http://127.0.0.1:8000/
  ```
2. ### API docs are available at: ###
  ```bash
  http://127.0.0.1:8000/docs
  ```
3. ### Root ###
     GET `/status`
   
     Returns the homepage of the API

5. ### Help ###
     GET `/help`
   
     Returns the info about API

7. ### List of students ###
     GET `/get_all_students/`<br />

     Returns List all students

8. ### Get a Single Student ###
     GET `/get_student/{student_id}/`

     Returns a student with given student_id

10. ### Insert a new student in database ###
      POST `insert_student/?student_id={student_id}&branch={branch}&cgpa={cgpa}&status={status}`

      Returns status=ok if student is inserted successfully in the database

12. ### Update a existing student in database ###
      PUT `/update_student/?student_id={student_id}&branch={branch}&cgpa={cgpa}&status={status}`

      Returns status=ok if student is updated successfully in the database

14. ### Delete a existing student in database ###
      DELETE `/delete_student/?student_id={student_id}/`
    
      Returns status=ok if student is deleted successfully in the database
      


## Contributing

Contributions to Quick Note are welcome!
If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository or submit a pull request with your changes.

## License

Quick Note is released under the MIT License.
