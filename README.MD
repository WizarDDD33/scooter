# Scooter Rent — автотесты API

Автотест сценария «создание заказа → получение заказа по треку»
для сервиса аренды самокатов.

## Сценарий
1. `POST /api/v1/orders` — создать заказ.
2. Сохранить `track` из ответа.
3. `GET /api/v1/orders/track?t=<track>` — получить заказ по треку.
4. Проверить, что код ответа `200`.

## Стек
- Python 3.8+
- pytest
- requests

## Установка и запуск

```bash
# 1. Клонировать репозиторий
git clone <repo-url>
cd scooter-api-tests

# 2. Создать и активировать виртуальное окружение
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Запустить тест
pytest test_create_order.py -v