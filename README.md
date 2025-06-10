Flask API Final Test
REST API-приложение на Flask с PostgreSQL, Docker и CI/CD через Jenkins.
________________________________________
?? Как запустить проект локально
1.	Клонируй репозиторий:
 	git clone https://github.com/KapitanTito/flask-api-finaltest.git
cd flask-api-finaltest
2.	Создай файл .env:
 	cp .env.example .env
# Заполни переменные в .env при необходимости
3.	Запусти через Docker Compose:
 	docker-compose up -d --build
4.	Применить миграции (если нужно):
 	docker-compose exec web flask db upgrade
5.	Приложение будет доступно по адресу:
 	http://localhost:5050
________________________________________
??? Как настроить Jenkins
1.	Установить Jenkins (например, через Docker или на сервере).
2.	Установить плагины:
o	Git
o	Docker
o	SSH Agent
3.	Создать Credentials:
o	SSH-ключ для доступа на сервер (kind: SSH Username with private key)
o	credentialsId добавить в Jenkinsfile
4.	Создать новую pipeline job
o	Ввести ссылку на репозиторий:
https://github.com/KapitanTito/flask-api-finaltest.git
o	Указать путь до Jenkinsfile (по умолчанию корень)
5.	В Jenkinsfile прописать свои credentialsId и путь до сервера
________________________________________
?? Как работает CI/CD
1.	Push в GitHub > Jenkins запускает pipeline:
o	Клонирует репозиторий
o	Собирает Docker-образ
o	Запускает линтер flake8
o	Деплоит на сервер через SSH (git pull + docker-compose up -d)
o	Применяет миграции БД через Flask-Migrate
2.	Всё разворачивается автоматически!
________________________________________
?? Примеры API-запросов
Получить все результаты
GET /results
Пример ответа:
[
  {
    "id": 1,
    "name": "Kirill",
    "score": 88,
    "timestamp": "2025-06-10T12:34:56"
  }
]
________________________________________
Добавить новый результат
POST /submit
Content-Type: application/json

{
  "name": "Kirill",
  "score": 88
}
Пример успешного ответа:
{"message": "Result added"}
________________________________________
?? Тестовая HTML-форма
Файл static/test.html позволяет быстро протестировать POST-запросы через браузер.
________________________________________
?? Полезные команды
•	Остановить сервисы:
 	docker-compose down
•	Посмотреть логи:
 	docker-compose logs web
docker-compose logs db
•	Миграции вручную:
 	docker-compose exec web flask db migrate
docker-compose exec web flask db upgrade
________________________________________
?? Контакты
Если есть вопросы — @KapitanTito
________________________________________
