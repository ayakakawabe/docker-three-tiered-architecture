# docker-three-tiered-architecture

## Quick Start
1. Create container
    ```
    docker compose up -d
    ```
2. Create a React project, a Vue project, or an other project after entering a web container.
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
### Database Container
#### **How to initialize the database**
* Change SQL in `./docker/db_context/init/init.sql`.

#### **How to manipulate the database**
1. Enter a database container.
    ```
    docker exec -it db bash
    ```
2. Connect to MySQL after entering a database container.
    
    if you want to use another user, change `sample_user` to 
    a user name that you want to use.
    ```
    mysql -u sample_user -p 
    ```