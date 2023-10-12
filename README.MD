# Тестовое задание Junior (bewise.ai)
>Docker Version: 20.10.23 <br>
>Docker-Compose version: v2.15.1

## Запуск в dev-mode
1. Добавить в .gitignore .env.dev и .env.prod
2. Изменить переменные .env на необходимые
3. Выполнить
```
$ docker-compose -f docker-compose.yml build
$ docker-compose -f docker-compose.yml up -d
```

## Запуск в product-mode
1. Добавить в .gitignore .env.dev и .env.prod
2. Изменить переменные .env на необходимые
3. Выполнить
```
$ docker-compose -f docker-compose.prod.yml build
$ docker-compose -f docker-compose.prod.yml up -d
```

## Подключение к PostgreSQL
1. Через psql
```
$ psql -h <HOST> -p <POSTGRES_PORT> -U <POSTGRES_USER> -d <POSTGRES_TABLE>
<enter password>
```

2. По DATABASE-URI (Через PGAdmin или подобное ПО)
```
postgresql://<USER>:<PASSWORD>@<HOST>:<PORT>/<DB>
```

## Пример POST запроса
<img src="https://i.imgur.com/X0vLMhE.png">