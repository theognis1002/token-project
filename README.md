# Token Project

### Setup

1.  `chmod +x token_app/entrypoint.prod.sh product_app/entrypoint.prod.sh`
1.  `docker compose -f docker-compose.prod.yml up --build`
1.  `docker compose run token_app python manage.py createsuperuser`
    -   follow prompt and enter in credentials
1.  Post the credentials made in the previous step to any of the `Token Service` endpoints to get your JWT token
    -   Example cURL:
        ```
        curl --request POST \ --url http://0.0.0.0:3333/tokens/admin/ \ --header 'Content-Type: application/json' \ --data '{ "username": "admin", "password": "admin" }'
        ```
1.  Use the JWT token to query the `Product Service` endpoints
    -   Example cURL:
         ```
         curl --request GET \
         --url http://0.0.0.0:8000/products/ \
         --header 'Authorization: Bearer <JWT_TOKEN>' \
         --header 'Content-Type: application/json' \
         --data '{
         "name": "My Product",
         "price": 10.0,
         "qty": 500
         }'
         ```

### Product Endpoints

1. `http://0.0.0.0:8000/products/`
    - List all active products
1. `http://0.0.0.0:8000/products/<id>/`
    - Perform CRUD operations on specific product
1. `http://0.0.0.0:8000/products-admin/`
    - List all products (both active and soft deleted)

### Token Endpoints

1. `http://0.0.0.0:3333/tokens/read/`
    - Create read-only token
1. `http://0.0.0.0:3333/tokens/manage/`
    - Create manage-only token
1. `http://0.0.0.0:3333/tokens/both/`
    - Create read and manage token
1. `http://0.0.0.0:3333/tokens/admin/`
    - Create admin token

### Testing

1. Run tests only:
    - `docker compose run token_app python manage.py test`
    - `docker compose run product_app python manage.py test`
1. Run tests + coverage report
    - `docker compose run token_app sh -c "coverage run --source tokens manage.py test -v 2 && coverage report"`
    - `docker compose run product_app sh -c "coverage run --source products manage.py test -v 2 && coverage report"`
