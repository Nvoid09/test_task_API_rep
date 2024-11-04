## Указания для запуска проекта:

1. Установить poetry глобально (`python3 -m pip install poetry`), либо:

    а. Создать виртуальное окружение вручную: `python3 -m venv .venv`

    б. Активировать виртуальное окружение: `source .venv/bin/activate`

    в. Установить poetry: `pip install -r requirements.txt` или `pip install poetry`

2. Настроить poetry: `poetry config virtualenvs.create true` и `poetry config virtualenvs.in-project true` для корректной работы с виртуальным окружением проекта. При глобальной настройке, poetry будет создавать .venv автоматически в папке с проектом. При локальной настройке будет использоваться активированное окружение.

3. Установить пакет проекта с зависимостями: `poetry install`. Зависимости будут автоматически установлены в виртуальное окружение вне зависимости от того, активировано ли оно вручную или нет.

4. Запустить asgi сервер с помощью скрипта `src/test_task/scripts/run.py`. Скрипт использует ранее установленный на шаге 3 пакет `test_task` для подгрузки нужных определений и запуска uvicorn. Запуск может быть осуществлён с помощью poetry (`poetry run python src/test_task/scripts/run.py`), либо вручную с предварительной активацией виртуального окружения.

5. Запустить тест api с помощью pytest (был установлен на шаге 3). Запуск может быть осуществлён с помощью poetry (`poetry run pytest`), либо вручную, с предварительной активацией виртуального окружения.

## Рекомендации по оформлению кода python проектов.

1. Определять структуру проекта в виде python пакета вне зависимости от того, является ли проект приложением или набором функций-утилит. [https://packaging.python.org/en/latest/tutorials/packaging-projects/](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
2. Использовать файл pyproject.toml для описания проекта, его зависимостей (в т.ч. зависимостей для разработки), определения поддерживаемых версий python [https://packaging.python.org/en/latest/guides/writing-pyproject-toml/](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
3. Использовать продвинутые утилиты для отслеживания зависимостей проекта, с целью чёткого определения версий пакетов-зависимостей, их хэш сумм и т.п. (poetry, [https://python-poetry.org/](https://python-poetry.org/))
4. Использовать фрэймворки для тестирования (pytest, unittest, etc.), вместо отдельных скриптов.

## Использование poetry для создания новых проектов.

Для автосоздания структуры проекта можно использовать `poetry new project-name`, если пакет poetry установлен глобально.
