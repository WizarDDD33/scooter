# Павел Данилов, 46-я когорта — Финальный проект. Инженер по тестированию плюс
import pytest

from api_client import create_order
from data import ORDER_PAYLOAD


@pytest.fixture(scope="module")
def created_order_track() -> int:
    response = create_order(ORDER_PAYLOAD)
    assert response.status_code == 201, (
        f"Не удалось создать заказ: {response.status_code} {response.text}"
    )
    return response.json()["track"]