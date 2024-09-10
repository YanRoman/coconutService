# Coconut service

сервис, который прогнозирует действия <br>
пользователей интернет магазина

# Требования
- Python 3
# Точки доступа
- http://localhost:8000/api/base [get]
# Запуск:
### 1. Dockerfile
``` shell
docker build -t coconut_image . ; docker run --name coconut -p 8000:8000 coconut_image
```

### 2. Powershell скрипт
```shell
    .\setup-and-run.ps1
```

### 3. Терминал (команды по очереди)
``` shell
python -m venv venv
```
``` shell
venv\Scripts\activate
```
```shell
pip install --no-cache-dir -r requirements.txt
```
```shell
python manage.py runserver 0.0.0.0:8000
```
