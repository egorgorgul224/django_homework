# Проект "Знакомство с Django"

---

## Оглавление
<a id="content"></a>
1. [Описание](#description)
2. [Установка и настройка проекта](#instruction)
3. [Структура проекта](#structure)
4. [Запуск и тестирование проекта](#launch)
5. [Лицензия](#license)

---

## Описание<a id="description"></a>
Проект направлен на знакомство с Django. В проекте подключен Django, создано приложение contact, созданы шаблоны
главной страницы и контактов и стилизованы. Созданы котроллеры для рендеринга шаблонов страниц. URL-файлы подключены
к главному URL-файлу проекта.

---

## Установка и настройка проекта<a id="instruction"></a>

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```
2. Перейдите в директорию проекта:
```
cd ваш_проект
```
3. Установите зависимости проекта:
```
poetry install
```
или
```
pip install -r requirements.txt
```
4. Зайдите в файл .env.example и следуйте инструкциям из него.

---

## Структура проекта<a id="structure"></a>
```
.
├── catalog - приложение на django
│ ├── migrations
│ ├── templates - папка с шаблонами страниц
│     ├── catalog
│         ├── contacts.html
│         ├── home.html
│     ├── admin.py, apps.py, models.py, tests.py, urls.py, views.py - необходимые модули для работы приложения
├── config
│     ├── asgi.py, settings.py, urls.py, wsgi.py необходимые модули для работы приложения
├── static - папка со стилями и фото
│ ├── css
│     ├── bootstrap.min.css
│ ├── js
│     ├── bootstrap.bundle.min.js
├── .env.example - env экземпляр для доступа к закрытым данным
├── .flake8
├── .gitignore
├── manage.py
├── pyproject.toml
├── poetry.lock
├── requirements.text - файл с зависимостями
└── README.md
```

---

## Запуск и тестирование проекта<a id="launch"></a>
1. После установки и настройки проекта в консоль введите python/python3 manage.py runserver для запуска сервера
2. Откройте сервер (ссылка в консоли: http://127.0.0.1:8000)

---

## Лицензия<a id="license"></a>

Этот проект лицензирован по [лицензии MIT](LICENSE).

##### [Оглавление](#content)