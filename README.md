Flask API Final Test
REST API-���������� �� Flask � PostgreSQL, Docker � CI/CD ����� Jenkins.
________________________________________
?? ��� ��������� ������ ��������
1.	�������� �����������:
 	git clone https://github.com/KapitanTito/flask-api-finaltest.git
cd flask-api-finaltest
2.	������ ���� .env:
 	cp .env.example .env
# ������� ���������� � .env ��� �������������
3.	������� ����� Docker Compose:
 	docker-compose up -d --build
4.	��������� �������� (���� �����):
 	docker-compose exec web flask db upgrade
5.	���������� ����� �������� �� ������:
 	http://localhost:5050
________________________________________
??? ��� ��������� Jenkins
1.	���������� Jenkins (��������, ����� Docker ��� �� �������).
2.	���������� �������:
o	Git
o	Docker
o	SSH Agent
3.	������� Credentials:
o	SSH-���� ��� ������� �� ������ (kind: SSH Username with private key)
o	credentialsId �������� � Jenkinsfile
4.	������� ����� pipeline job
o	������ ������ �� �����������:
https://github.com/KapitanTito/flask-api-finaltest.git
o	������� ���� �� Jenkinsfile (�� ��������� ������)
5.	� Jenkinsfile ��������� ���� credentialsId � ���� �� �������
________________________________________
?? ��� �������� CI/CD
1.	Push � GitHub > Jenkins ��������� pipeline:
o	��������� �����������
o	�������� Docker-�����
o	��������� ������ flake8
o	������� �� ������ ����� SSH (git pull + docker-compose up -d)
o	��������� �������� �� ����� Flask-Migrate
2.	�� ��������������� �������������!
________________________________________
?? ������� API-��������
�������� ��� ����������
GET /results
������ ������:
[
  {
    "id": 1,
    "name": "Kirill",
    "score": 88,
    "timestamp": "2025-06-10T12:34:56"
  }
]
________________________________________
�������� ����� ���������
POST /submit
Content-Type: application/json

{
  "name": "Kirill",
  "score": 88
}
������ ��������� ������:
{"message": "Result added"}
________________________________________
?? �������� HTML-�����
���� static/test.html ��������� ������ �������������� POST-������� ����� �������.
________________________________________
?? �������� �������
�	���������� �������:
 	docker-compose down
�	���������� ����:
 	docker-compose logs web
docker-compose logs db
�	�������� �������:
 	docker-compose exec web flask db migrate
docker-compose exec web flask db upgrade
________________________________________
?? ��������
���� ���� ������� � @KapitanTito
________________________________________
