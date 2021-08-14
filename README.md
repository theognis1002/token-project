# Instructions

1. `chmod +x token_app/entrypoint.sh && chmod +x product-app/entrypoint.sh`
1. `docker compose up --build`

### Create Admin User

1. `docker compose run token_app python manage.py createsuperuser`
    - follow prompt and enter in credentials

### Testing

1. Run tests only:
    - `docker compose run token_app python manage.py test`
    - `docker compose run product_app python manage.py test`
1. Run tests + coverage report
    - `docker compose run token_app sh -c "coverage run --source tokens manage.py test -v 2 && coverage report"`
    - `docker compose run product_app sh -c "coverage run --source products manage.py test -v 2 && coverage report"`
