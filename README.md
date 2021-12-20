# UFC Rankings Api

##### The app uses BeautifulSoup to extract the data from the official ufc website and saves it to a json file
 
## Steps:
#### 1) create a virtual environment inside your folder, and activate it
        run the command: python -m venv venv
        to activate, run: . venv/Scripts/activate
        
### 2) update pip version
        run the command: python -m pip install --upgrade pip==21.1.2    
### 3) cd into the main 'app' folder and install the packages
       run the command: python -m pip install -r requirements.txt

### 4) use docker compose to bring the containers up (in detached mode)
       run the command: docker compose up -d

#### The django web app will fail initially, since there is no DB connection. Proceed to step 5.

### 5) inside pgAdmin (in the browser) create a server
       for server name enter: ufc (or any) , for connection Host name' enter: pg , 
       for password - xxxxxx (your password in docker-compose.yml)

### 6) Restart ( or stop and start django web app container)
       run: docker restart <ContainerID>
       or run: docker stop <ContainerID>  and after run: docker start <ContainerID>

### 7) create migrations to load the tables, and apply migrations:
       run: docker compose exec web python manage.py makemigrations --noinput
       run: docker compose exec web python manage.py migrate --noinput



### Closing the app - Stop and remove the containers with the command:
    docker compose down --rmi all

## Endpoints:
            1) [GET, POST]    http://127.0.0.1:8000/api/weightclasses 
            2) [DELETE, GET]  http://127.0.0.1:8000/api/weightclasses/<int:pk> 
            3) [PUT]          http://127.0.0.1:8000/api/weightclasses/<int:pk>/ 
            ___________________________________________________________________
            4) ... not ready yet


#### Work in progress... 🐍🐍🐍        
