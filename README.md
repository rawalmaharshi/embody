#Embody - Software Engineer Intern Assignment

The project is a REST API based on Flask Microframework in Python. The main function of the API is to return the user_key associated with a particular user, when user_id is passed in a GET request as a query string. 

The **logistics** of the projects is as follows:
1) Language and Framework - Python, Flask
2) Database - Redis
3) Load Balancing - Nginx
4) Build Tool - Docker

*app1, app2, app3* represent the Flask API that is run on 3 separate instances of Docker on ports *5001, 5002, 5003* respectively.

##Working
Intially, the API was developed without having the reverse proxy server nginx setup. After that, nginx load balancing along with Docker.
There are 3 **endpoints** in the REST API
1) **/ [GET]** - Returns Hello World! (for testing purpose)
2) **/ping [GET]** - Returns PONG (for testing purpose)
3) **/getuserkey [GET]** - Expects a query param: user_id=someRandomId 
    e.g. `/getuserkey?user_id=maharshi`

The working of project is such that it looks in the database for the existence of the particular user_id, if the user_id is found in the database, the respective user_key(length=32) is returned. Otherwise, a new user_key is generated for the user and returned in the JSON response along with the port number serving that request.

##How to Run
To run the project, go to the project directory and run the command:
1) `sudo docker-compose up --build`
  This will run the project in the *localhost:5000*.
  Go to `http://localhost:5000/getuserkey?user_id={random_user_id}` to test the project.
  In the `docker-compose.yml` file, nginx listens to all requests coming to the port 5000 and maps them to port 80 (the port it listens to in the nginx.conf file)
  
2) To run the project again, first use `sudo docker compose down --remove-orphans` and then follow the first step again.