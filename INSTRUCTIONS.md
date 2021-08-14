# Summit Inventory App

A Django backend app to be able to manage products inventory

## Task submission

To submit the assignment, please create a private GitHub repo and share the access with:

-   `GoelJatin`
-   `dennijo`

## Task description

There would be 2 different services:

### Products service

-   A web service to manage products inventory - all CRUD operations with both soft delete and hard delete operations
    -   A special endpoint to be able to list all products regardless of their status - `admin` permission only
-   The APIs should only be accessible if a valid JWT token (generated from `Token` service) is passed in the **Authorization** header in the format: `Authorization: Bearer {{TOKEN}}`
-   The API operations should be allowed basis on permissions:
    -   `read_product` - if a token has this permission only then the read operation should be allowed
    -   `manage_product` - all other CUD operations

### Token service

-   This service should have 4 endpoint(s) to generate a JWT token using a Secret Key
    -   Endpoint A - token with `read_product` permission
    -   Endpoint B - token with `manage_product` permission
    -   Endpoint C - token with `both` permission(s)
    -   Endpoint D - token with `admin` permission
    -   Token should be valid for 10 mins only
-   The token should be stored in the DB
-   Only one token should be valid at any point of time

### Database

Both services should connect to a single Postgres DB

### Tests

Unit tests for the above services with coverage >85%

## Add ons

### Docker

The services and database should be containerized

### Web server

The app should be accessible via a web server only, NGINX / Apache / any web server of your choice
