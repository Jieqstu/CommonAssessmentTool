Team TicTech

Project -- Feature Development Backend: Create CRUD API's for Client

User Story

As a user of the backend API's, I want to call API's that can retrieve, update, and delete information of clients who have already registered with the CaseManagment service so that I more efficiently help previous clients make better decisions on how to be gainfully employed.

Acceptance Criteria
- Provide REST API endpoints so that the Frontend can use them to get information on an existing client.
- Document how to use the REST API
- Choose and create a database to hold client information
- Add tests


This will contain the model used for the project that based on the input information will give the social workers the clients baseline level of success and what their success will be after certain interventions.

The model works off of dummy data of several combinations of clients alongside the interventions chosen for them as well as their success rate at finding a job afterward. The model will be updated by the case workers by inputing new data for clients with their updated outcome information, and it can be updated on a daily, weekly, or monthly basis.

This also has an API file to interact with the front end, and logic in order to process the interventions coming from the front end. This includes functions to clean data, create a matrix of all possible combinations in order to get the ones with the highest increase of success, and output the results in a way the front end can interact with.

-------------------------How to Use-------------------------
1. In the virtual environment you've created for this project, install all dependencies in requirements.txt (pip install -r requirements.txt)

2. Run the app (uvicorn app.main:app --reload)

3. Load data into database (python initialize_data.py)

4. Go to SwaggerUI (http://127.0.0.1:8000/docs)

4. Log in as admin (username: admin password: admin123)

5. Click on each endpoint to use
-Create User (Only users in admin role can create new users. The role field needs to be either "admin" or "case_worker")

-Get clients (Display all the clients that are in the database)

-Get client (Allow authorized users to search for a client by id. If the id is not in database, an error message will show.)

-Update client (Allow authorized users to update a client's basic info by inputting in client_id and providing updated values.)

-Delete client (Allow authorized users to delete a client by id. If an id is no longer in the database, an error message will show.)

-Get clients by criteria (Allow authorized users to get a list of clients who meet a certain combination of criteria.)

-Get Clients by services (Allow authorized users to get a list of clients who meet a certain combination of service statuses.)

-Get clients services (Allow authorized users to view a client's services' status.)

-Get clients by success rate (Allow authorized users to search for clients whose cases have a success rate beyond a certain number.)

-Get clients by case worker (Allow users to view which clients are assigned to a specific case worker.)

-Update client services (Allow users to update the service status of a case.)

-Create case assignment (Allow authorized users to create a new case assignment.)


## Running with Docker

### Prerequisites
Before running the backend with Docker, ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Option 1: Run using Docker Commands

#### Step 1: Build the Docker Image
```bash
docker build -t case-management-backend .
```
This command reads Dockerfile, installs the necessary dependencies and sets up the container environment.

Step 2: Run the Docker Container
```bash
docker run -p 8000:8000 case-management-backend
```
This command starts the container and maps port 8000 of your container to port 8000 on your host machine.

### Option 2: Run using Docker Compose

#### Step 1: Start the Container using Docker Compose
```bash
docker-compose up --build
```
This command builds the image and starts the containers defined in the docker-compose.yml.

#### Step 2: Stopping the Container
```bash
docker-compose down
```
This command stops and removes the containers.

---
# Sprint3 - Story 1

## Public Swagger URL
http://ec2-18-212-56-36.compute-1.amazonaws.com:8000/docs

## Deployment Instructions

1. SSH into EC2
```bash
ssh -i ~/.ssh/casemanagement.pem ubuntu@18.212.56.36
```

Make sure the key file has proper permissions:
```bash
chmod 400 ~/.ssh/casemanagement.pem
```

2. Clone the repo and set up the environment

```bash
sudo apt update
sudo apt install git python3-pip python3-venv -y

git clone https://github.com/Jieqstu/CommonAssessmentTool.git
cd CommonAssessmentTool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the backend server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

4. Load initial data
```bash
source venv/bin/activate
python initialize_data.py
```
This will insert default users including an admin and case worker.

5. Log in via Swagger
Admin Username: admin

Admin Password: admin123

Get the token from /token, click "Authorize", then access protected endpoints like /clients.


## Developer Setup / SSH Access Instructions (for teammates)

### SSH Access to EC2

You can SSH into the EC2 instance using the following credentials:

```bash
ssh -i ~/.ssh/casemanagement.pem ubuntu@18.212.56.36
```

Username: ubuntu

Make sure you have the casemanagement.pem key file
Move the key to ~/.ssh/ for convenience
If needed, run chmod 400 casemanagement.pem to restrict permissions

Once logged in:
```bash
cd ~/CommonAssessmentTool
```

Manually Running the Backend (for testing)
```bash
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Testing the Server
After running the server, Swagger docs will be available at:
```bash
http://ec2-18-212-56-36.compute-1.amazonaws.com:8000/docs
```