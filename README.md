# Установка и запуск

- Склонировать репозиторий
```
git clone https://github.com/jancoksys/webapp
```
- Установить python 3.13
- В папке webapp выполнить:
```
py -3 -m venv .venv
```
- Далее выполнить:
```
.venv\Scripts\activate
```
- Установить Flask
```
pip install Flask
```
- Установить SwaggerUI
```
pip install flask-swagger-ui
```
- Запустить приложение 
```
flask --app webapp run
```
По умолчанию оно будет запущено по адресу: 
```
http://127.0.0.1:5000/
```
