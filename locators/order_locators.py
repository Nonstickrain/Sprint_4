from selenium.webdriver.common.by import By

class MakeOrderLocators:

    make_order_section = [By.XPATH, ".//div[text() = 'Как это работает']"]
    make_order_button_1 = [By.XPATH, ".//button[@class = 'Button_Button__ra12g']"]
    make_order_button_2 = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]

    firstname = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    secondname = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    adress = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    metro_selector = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    metro_station = [By.XPATH, ".//li[@data-index = '0']/button"]
    phone_number = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]

    next_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]

    order_data = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    order_duration_selector = [By.XPATH, ".//span[@class = 'Dropdown-arrow']"]
    order_duration = [By.XPATH, ".//div[text() = 'сутки']"]
    black_color = [By.ID, "black"]
    grey_color = [By.ID, "grey"]
    order_comment = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"]

    send_order_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]
    yes_button = [By.XPATH, ".//button[text() = 'Да']"]
    completed_order = [By.XPATH, ".//div[text() = 'Заказ оформлен']"]
    see_your_order_button = [By.XPATH, ".//button[text() = 'Посмотреть статус']"]

    samocat_logo = [By.XPATH, ".//img[@alt = 'Scooter']"]
    yandex_logo = [By.XPATH, ".//img[@alt = 'Yandex']"]
