# Описание
Микро-сервис для парсинга XmlFile сервиса zakupki.gov.ru, работающий на связке flask+uWSGI+NGINX.
1. Api для получения информации id информации из локальных файлов;
2. Api для получение полной информации по аукциону по юрл ссылке.

# Структура
* app/ - директория с flask приложением
* congigs/ - директория с настройками пакетов, приложения, api. Все настройки можно получить от ConfigDealer
* packages/ - директория со специальными пакетами необдодимые для работы контроллеров flask. Получить необходимый объект можно от PackageDealer
* wsgi.py - файл точки входа
* xmlparser.ini - файл настройками uWSGI сервиса
* parserxml.sock - файл сокет для соеденения сервера NGINX  с сервисом uWSGI
* setup.py - файл установки. Временно не работает
* .env - файл с переменными окружения, необходимые для работы сериса

# Предустановки
1. sudo apt update
2. sudo apt install nginx python3
3. sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv

# Установка
1. Скачать с репозитория
2. Создать venv python3 -m venv venv
3. Войти в venv source venv/bin/activate
2. Установить требуемые пакеты из requirements.txt pip install -r requirements.txt
3. Настроить файл .env
4. Настроить файл xmlparser.ini
5. Создать uWSGI сервис в ОС.
6. Создать связть uWSGI и NGINX через файл xmlparser.sock

# Настройка Configs(.env) - файл переменных виртуального окружения
Зайти в файл .env и задать необходимые переменные:
* UNPACK_PATH - путь до директории разархивированных файлов
* DEFAULT_LOCAL_PARSE_PATH - стандартный путь до директории с файлами
* APP_MODE - режим в котором включить приложение
