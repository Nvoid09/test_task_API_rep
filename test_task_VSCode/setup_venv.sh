#!/bin/bash

# Проверка, что Python 3.8 установлен
if ! command -v python3.8 &> /dev/null
then
    echo "Python 3.8 не установлен. Пожалуйста, установите его перед запуском скрипта."
    exit 1
fi

# Создание виртуального окружения в папке .venv
echo "Создание виртуального окружения..."
python3.8 -m venv .venv

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source .venv/bin/activate

# Обновление pip до последней версии
echo "Обновление pip..."
pip install --upgrade pip

# Установка зависимостей из requirements.txt, если файл существует
if [ -f "requirements.txt" ]; then
    echo "Установка зависимостей из requirements.txt..."
    pip install -r requirements.txt
else
    echo "Файл requirements.txt не найден. Убедитесь, что он находится в текущей директории."
    deactivate
    exit 1
fi

echo "Виртуальное окружение настроено, активировано и зависимости установлены."
