import stand_request


def status_test():
    response = stand_request.Create_new_order()
    get_response = stand_request.get_order(f"{response.json()["track"]}")
    assert get_response.status_code == 200


def test_status_order():
    status_test()

#Карачев Макисм Николаевич, 10-я когорта — Финальный проект. Инженер по тестированию плюс