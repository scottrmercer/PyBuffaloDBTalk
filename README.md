This project was created to accompany a talk I gave to the Python Buffalo meetup on 2019-03-14. The slides are included in HTML and PDF format in the master branch. The subject of the talk is "how to manage your RDBMS schema using python", and it covers SQLAlchemy, SQLAlchemy-continuum, and Alembic. 

# Running this project

This talk (see index.html for slides) contains 3 exercises. 
Each exercise has a corresponding branch in the repository.
* excercise-1
* excercise-2
* excercise-3

To run the example code for each segment of the talk, checkout the exercise branch, and use docker-compose to start the containers (postgres and python3.6). 
These containers have all dependencies installed. You will need to have the docker daemon running locally, and docker-compose installed. 

# Helpful Commands
Docker Compose (run within docker directory)
* Start and build containers: `docker-compose up --build -d` 
* Stop containers: `docker-compose down`
* Open shell within container: `docker-compose run python sh` 

Alembic (be sure to set the PYTHONPATH to `.` when running in container shell)
* Initialize: `alembic init alembic` 
* Autogenerate revision: `alembic revision --autogenerate -m 'some comments here'`
* Upgrade to head: `alembic upgrade head`
* Downgrade 1 revision: `alembic downgrade -1` 
