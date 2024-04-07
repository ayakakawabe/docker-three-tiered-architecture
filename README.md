# docker-three-tiered-architecture

## Quick Start
1. Create container
    ```
    docker compose up -d
    ```
2. Create a React project, a Vue project, or an other project after entering the web container.
    ```
    docker compose exec web bash
    ```
    If you create a React project, run the following command.
    ```
    npx create-react .
    ```
    If you create a Vue project, run the following command
    ```
    npm create vue@latest .
    ```

## Usage

### Web Container
#### **How to fetch data from Fast API in the app container**
1. Enter the web container.
    ```
    docker compose exec web bash
    ```
2. Run the following command
    ```
    node app.js
    ```

### App Container
#### **How to connect MySQL in the database container**
1. Enter the app container.
    ```
    docker compose aexec app bash
    ```
2. Run the following command.
    ```
    python3 con_db
    ```

### Database Container
#### **How to initialize the database**
* Change SQL in `./docker/db_context/init/init.sql`.

#### **How to manipulate the database**
1. Enter the database container.
    ```
    docker exec -it db bash
    ```
2. Connect to MySQL after entering the database container.
    
    if you want to use another user, change `sample_user` to 
    a user name that you want to use.
    ```
    mysql -u sample_user -p 
    ```