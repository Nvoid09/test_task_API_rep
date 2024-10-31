#!/bin/bash
echo "Запуск сервера FastAPI..."
./.venv/bin/uvicorn api:app --reload
