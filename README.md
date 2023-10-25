# How to setup?

## 0. Set environment variable

Rename `.env.example` as `.env`. And set variables.  
e.g. `SECRET_KEY=[This is a string]`

## 1. Initialize database

`docker exec [CONTAINER ID] bash -c 'python /workspace/app/manage.py makemigrations && python /workspace/app/manage.py migrate'`

## 2. Create admin user

`docker exec -it [CONTAINER ID] bash -c 'python /workspace/app/manage.py createsuperuser'`

## 3. Push initial data

`docker exec [CONTAINER ID] bash -c 'python /workspace/app/manage.py seed --mode=refresh'`

## 4. Tests

`docker exec -it [CONTAINER ID] bash -c 'python /workspace/app/manage.py test'`

## 5. API & Endpoints

You can browse to :

```
admin/
api-auth/ (swagger)
/         (app)
```