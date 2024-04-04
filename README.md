# docker-three-tiered-architecture

## Quick Start
1. Create container
    ```
    docker compose up -d
    ```
2. Create a React project, a Vue project, or an other project after entering a web container
    ```
    docker compose exec web bash
    ```
    if you create a React project,
    ```
    npx create-react .
    ```
    if you create a Vue project,
    ```
    npm create vue@latest .
    ```