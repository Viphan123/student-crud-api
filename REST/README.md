## Student CRUD API
This project is a simple RESTful API for managing student records, supporting Create, Read, Update, and Delete (CRUD) operations. The API is built using Flask and is deployed on Azure Web App Service. This README will guide you through setting up, running, and deploying the API.


### Features
Create a new student record
Read all students or a specific student by ID
Update a student's information by ID
Delete a student by ID
### Endpoints
GET /students - Retrieve a list of all students.
GET /students/{id} - Retrieve details of a student by ID.
POST /students - Add a new student.
PUT /students/{id} - Update an existing student by ID.
DELETE /students/{id} - Delete a student by ID.
### Getting Started
Prerequisites
Python 3.8 or above
Flask and Flask-RESTful for the API framework
Git for version control
### Installation
Clone the repository:
```
git clone https://github.com/viphan123/student-crud-api.git
cd student-crud-api 
```
### Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### Install dependencies:

```python 
pip install flask
```
### Environment Configuration
Configure any environment variables needed for the project. Update the .env file with required variables or set them directly in the deployment environment:

FLASK_APP: Set to REST.py
FLASK_ENV: Set to development for local testing
### Running the API Locally
After configuring the environment, start the API locally with:
```
flask run
```
The API will be available at http://127.0.0.1:5000.

### Deployment

1. Set up an Azure Web App Service through the Azure Portal.
2. Create a publish profile for deployment.
3. Push code changes to GitHub: The CI/CD pipeline will automatically deploy the latest code to Azure Web App (refer to .github/workflows/ci-cd.yml).
### CI/CD Pipeline
This project uses GitHub Actions for CI/CD. The workflow file (.github/workflows/ci-cd.yml) configures automatic deployment to Azure Web App Service upon each push to the main branch.

### Important Notes
Delete Azure Resources: After confirming the API deployment, delete the Azure resources to minimize costs.
### License
This project is licensed under the MIT License. See the LICENSE file for more details.
