# Запуск:
##1) Создание окружения
```
pip unstall virtualenv
python -m venv venv (Если Mac или linux python3 -m venv venv)
.\venv\Scripts\activate
```
##2) Установка нужных пакетов
```
pip install -r requirements.txt
```
##3) Запуск программы
```
python main.py (Если Mac или linux python3 main.py)
```

# Endpoints:

GET```/city/``` - Получение всех городов из БД;

GET````/city/street/?city=1```` - Получение всех улиц города по id города;

GET ```/shop/``` - Получение всех магазинов;

GET ```/shop/?city=1``` - Получение всех магазинов в конкретном городе;

GET ```/shop/?street=1``` - Получение всех магазинов на конкретной улице;

GET ```/shop/?street=1&city=1``` - Получение всех магазинов на конкретной улице в конкретном городе;

POST ```/shop/``` - Создание магазина
