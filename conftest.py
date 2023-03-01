import pytest
from random import randint


@pytest.fixture
def user_data():
    data = {
        'name': 'Артём',
        'surname': 'Тимонин',
        'adress': 'Строителей д.' + str(randint(0, 100)),
        'phone number': '8' + str(randint(900, 999)) + str(randint(1000000, 9999999))
    }
    return data

@pytest.fixture
def order_data():
    data = {
        'time': str(randint(1, 28)) + '.' + str(randint(1, 12)) + '.23',
        'comment': 'Тестовый комментарий'
    }
    return data