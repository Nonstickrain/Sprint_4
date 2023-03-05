from selenium.webdriver.common.by import By

class MakeOrderLocators:

    make_order_section = [By.XPATH, ".//div[text() = 'Как это работает']"]
    make_order_button_1 = [By.XPATH, ".//div[@class= 'Header_Nav__AGCXC']/button[text()='Заказать']"]
    make_order_button_2 = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button"]

    firstname = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    secondname = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    adress = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    metro_selector = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    metro_station = [By.XPATH, ".//li[@data-index = '0']/button"]
    phone_number = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]

    next_button = [By.XPATH, ".//button[text() = 'Далее']"]

    order_data = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    order_duration_selector = [By.XPATH, ".//span[@class = 'Dropdown-arrow']"]
    order_duration = [By.XPATH, ".//div[text() = 'сутки']"]
    black_color = [By.ID, "black"]
    grey_color = [By.ID, "grey"]
    order_comment = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"]

    send_order_button = [By.XPATH, ".//div[@class= 'Order_Buttons__1xGrp']/button[text()='Заказать']"]
    yes_button = [By.XPATH, ".//button[text() = 'Да']"]
    completed_order = [By.XPATH, ".//div[text() = 'Заказ оформлен']"]

    samocat_logo = [By.XPATH, ".//img[@alt = 'Scooter']"]
    yandex_logo = [By.XPATH, ".//img[@alt = 'Yandex']"]
