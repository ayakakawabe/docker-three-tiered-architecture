# docker-three-tiered-architecture

## 🚀 Quick Start
1. Create container.
    ```
    docker compose up -d --build
    ```
2. Check the connection.
    * Connect on a client network ( web - app ).
    1. Enter the web container.
        ```
        docker compose exec web bash
        ```
    2. Run the following command.
        ```
        node sample.js
        ```
    * Connect on a server network ( app - db ).
    1. Enter the app container.
        ```
        docker compose aexec app bash
        ```
    2. Run the following command.
        ```
        python3 con_db
        ```


## 📚 Usage

### Web Container
* Create a React project, a Vue project, or an other project after entering the web container.
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

### App Container
#### **How to install the Python packages with build the app container.**
* Write the packages that you want to install in `./docker/app_context/requirements.txt`.

### Database Container
#### **How to initialize the database**
* Change SQL in `./docker/db_context/init/init.sql`.

#### **How to manipulate the database**
1. Enter the database container.
    ```
    docker exec -it db bash
    ```
2. Connect to MySQL after entering the database container.
    ```
    mysql -u sample_user -p 
    ```
    A password is `sample_user`.
    
    if you want to use another user, change `sample_user` to 
    a user name that you want to use in `./docker-compose.yml`.

    Then, run the following command.
    ```
    mysql -u username -p 
    ```
    