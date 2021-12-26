# UFC Rankings Api

About:
UFC rankings api server using django and postgres on the backend and React on the frontend
The app uses BeautifulSoup to extract the data from the official ufc website and loads the data initially into the tables.

ufc_rankings_client 👉 https://github.com/Azamat-Shogen/ufc_rankings_client
 
## Steps:
#### 1. Create a virtual environment inside your folder, and activate it
        run the command: python -m venv venv
        to activate, run: . venv/Scripts/activate
        
#### 2. Update pip version
python -m pip install --upgrade pip==21.1.2    

#### 3. cd into the main 'app' folder and install the packages
python -m pip install -r requirements.txt

#### 4. use docker compose to bring the containers up (in detached mode)
docker compose up -d

#### The django web app will fail initially, since there is no DB connection. Proceed to step 5.

#### 5. Inside pgAdmin (in the browser) create a server
        for server name enter: ufc (or any) , for connection Host name' enter: pg , 
        for password - xxxxxx (your password in docker-compose.yml)

#### 6. Restart ( or stop and start django web app container)
        run: docker restart <ContainerID>
        or run: docker stop <ContainerID>  
        and after run: docker start <ContainerID>

#### 7. Create migrations to load the tables, and apply migrations: 
docker compose exec web python manage.py makemigrations --noinput
       
#### 8. Run migrations:
docker compose exec web python manage.py migrate --noinput

#### 9. Load the data from json file into the tables:
docker compose exec web python manage.py runscript seed



### Closing the app - Stop and remove the containers with the command:
docker compose down --rmi all

## Endpoints:
            1) [GET, POST]         http://127.0.0.1:8000/api/weightclasses 
            2) [DELETE, GET, PUT]  http://127.0.0.1:8000/api/weightclasses/<int:pk> 
            ___________________________________________________________________
            3) [GET, POST]         http://127.0.0.1:8000/api/athletes
            4) [DELETE, GET, PUT]  http://127.0.0.1:8000/api/athletes/<int:pk> 
            


#### Work in progress... 🐍🐍🐍        
