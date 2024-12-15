# Order_PRJ
**DRF + Swagger**

✅ JWT авторизация <br>
✅ Логирование действий <br>
❌ Обработка ошибок <br>
❌ Docker <br>

🏗️ Запуск

## Linux (Debian/Ubuntu)
Обновление системы и установка зависимостей:

```bash
sudo apt update -y && sudo apt upgrade -y && sudo apt install python3 python3-pip
sudo apt install python3-venv
sudo apt install postgresql postgresql-contrib
```
Вход в PostgreSQL:

```bash
sudo -u postgres psql
```
Создание базы данных:

```SQL
CREATE DATABASE orders_db;
```
Клонирование репозитория:

```bash
git clone https://github.com/ghost404-dev/Order_PRJ.git
```
Переход в директорию проекта:

```bash
cd /Order_PRJ
```
Создание виртуального окружения:

```bash
python3 -m venv venv
```
Активация виртуального окружения:

```bash
source venv/bin/activate
```
Установка зависимостей:
```bash
pip install -r requirements.txt
```
Применение миграций:

```bash
python manage.py migrate
```
Запуск проекта:

```bash
python manage.py runserver
```

## Windows (!!! НЕ ТЕСТИРОВАЛ !!!) 
Установка Python и pip:

Скачай и установи [Python](https://www.python.org/), убедившись, что выбрал опцию Add Python to PATH.
Установка Git (если не установлен):

Установка PostgreSQL:

Скачай и установи [PostgreSQL](https://www.postgresql.org/) для Windows.
Во время установки отметь опцию Install Stack Builder для дополнительной настройки.
Вход в PostgreSQL:

Открой командную строку PostgreSQL и выполни:
```CMD
psql -U postgres
```
Создание базы данных:

```CMD
CREATE DATABASE orders_db;
```
Клонирование репозитория:
Открой командную строку (CMD) или PowerShell и выполните:

```CMD
git clone https://github.com/ghost404-dev/Order_PRJ.git
```
Переход в директорию проекта:

```CMD
cd Order_PRJ
```
Создание виртуального окружения:

```CMD
python -m venv venv
```
Активация виртуального окружения: Для CMD:

```CMD
.\venv\Scripts\Activate
```
Установка зависимостей:

```CMD
pip install -r requirements.txt
```
Применение миграций:
```CMD
python manage.py migrate
```
Запуск проекта:
```CMD
python manage.py runserver
```
