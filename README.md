<h1 align="center">Hi there, I'm <a href="https://t.me/anastaaaaaass" target="_blank">Anastasiya</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">This is a django-project with PostgreSQl and few models </h3>

### Install

    git clone https://github.com/nannnnna/fl_django.git
    cd fl_django

### Setup

    you must create .env file with these parametrs or use .env_example:
    KEY=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=postgres
    DB_PORT=5432
    POSTGRES_PASSWORD=

    in DB_HOST write the name of the service from the docker 
    docker-compose  run --rm web  python gen_key.py
    write to env your secret key 
    
### Run

    docker-compose up -d --build

### Check

    listening on http://localhost:8000/
    

### Stop and delete web and postgres containers

    docker-compose down




