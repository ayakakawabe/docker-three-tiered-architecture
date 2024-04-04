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