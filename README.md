Техзадание - Поднять сервис на Docker, используя FastAPI, который будет получать с ресурса вопросы с ответами и сохранять их в базе данных.

Название - Tehzadan

## Инструменты

- Python 3.11
- FastAPI
- Docker


------------------------------------------------

## Старт
- скачать проект с репозитория
- Внести в файл .env свои данные бд: postgresql://user_name:password@host/database_name 
- В файле docker-compose.yml внести данные бд

#### Запустить сервер

- используя команду - docker-compose up --build в папке проекта запустить проект 
- на странице http://localhost:8000/docs в свагере сделать запрос на количество вопросов 
