# Павел Данилов, 46-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

from config import (
    BASE_URL,
    CREATE_ORDER_ENDPOINT,
    GET_ORDER_BY_TRACK_ENDPOINT,
)


def create_order(payload: dict) -> requests.Response:
    return requests.post(
        f"{BASE_URL}{CREATE_ORDER_ENDPOINT}",
        json=payload,
        timeout=10,
    )


def get_order_by_track(track: int) -> requests.Response:
    return requests.get(
        f"{BASE_URL}{GET_ORDER_BY_TRACK_ENDPOINT}",
        params={"t": track},
        timeout=10,
    )