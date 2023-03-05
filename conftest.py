import pytest
from random import randint
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


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
@pytest.fixture
def start_browser(request):
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    request.instance.driver = driver
