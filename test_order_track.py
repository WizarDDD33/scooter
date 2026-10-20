# Павел Данилов, 46-я когорта — Финальный проект. Инженер по тестированию плюс
from api_client import create_order, get_order_by_track
from data import ORDER_PAYLOAD


def test_create_order_returns_201_and_track():
    """Проверяет только создание заказа."""
    response = create_order(ORDER_PAYLOAD)

    assert response.status_code == 201, (
        f"Ожидался 201, получен {response.status_code}: {response.text}"
    )
    assert "track" in response.json(), "В ответе отсутствует поле track"


def test_get_order_by_track_returns_200(created_order_track):
    """Проверяет только получение заказа по треку."""
    response = get_order_by_track(created_order_track)

    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}: {response.text}"
    )
    assert response.json()["order"]["track"] == created_order_track