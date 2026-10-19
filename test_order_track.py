# Павел Данилов, 46-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

BASE_URL = "https://13403dcb-d419-400c-a853-c54c6f224c6b.serverhub.praktikum-services.ru"


def test_get_order_by_track():
    # 1. Создаём заказ
    order_body = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

    create_response = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=order_body,
        timeout=10
    )

    assert create_response.status_code == 201, (
        f"Ожидался 201 при создании заказа, получен "
        f"{create_response.status_code}: {create_response.text}"
    )

    # 2. Сохраняем трек заказа
    track = create_response.json()["track"]
    assert track is not None

    # 3. Получаем заказ по треку
    get_response = requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track},
        timeout=10
    )

    # 4. Проверяем код ответа
    assert get_response.status_code == 200, (
        f"Ожидался 200 при получении заказа по треку, получен "
        f"{get_response.status_code}: {get_response.text}"
    )

    # Дополнительная проверка, что вернулся тот же заказ
    order = get_response.json()["order"]
    assert order["track"] == track