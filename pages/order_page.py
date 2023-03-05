from locators.order_locators import MakeOrderLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class OrderPageUserData:

    def __init__(self, driver):
        self.driver = driver

    def send_text_to_firstname_input(self, str):
        input = MakeOrderLocators.firstname
        self.driver.find_element(*input).send_keys(str)

    def send_text_to_secondname_input(self,str):
        input = MakeOrderLocators.secondname
        self.driver.find_element(*input).send_keys(str)

    def send_text_to_adress_input(self, str):
        input = MakeOrderLocators.adress
        self.driver.find_element(*input).send_keys(str)

    def choose_station_in_metro_selector(self):
        selector = MakeOrderLocators.metro_selector
        metro = MakeOrderLocators.metro_station

        self.driver.find_element(*selector).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((metro)))
        self.driver.find_element(*metro).click()

    def send_text_to_phone_number_input(self,str):
        input = MakeOrderLocators.phone_number
        self.driver.find_element(*input).send_keys(str)

    def click_on_next_button(self):
        button = MakeOrderLocators.next_button
        self.driver.find_element(*button).click()

class OrderPageOrderData:

    def __init__(self, driver):
            self.driver = driver

    def send_text_to_data_input(self, str):
        input = MakeOrderLocators.order_data
        self.driver.find_element(*input).send_keys(str)

    def choose_order_duration(self):
        selector = MakeOrderLocators.order_duration_selector
        duration = MakeOrderLocators.order_duration

        self.driver.find_element(*selector).click()
        self.driver.find_element(*duration).click()

    def choose_black_color(self):
        color = MakeOrderLocators.black_color
        self.driver.find_element(*color).click()

    def choose_grey_color(self):
        color = MakeOrderLocators.grey_color
        self.driver.find_element(*color).click()

    def send_text_to_comment_input(self, str):
        input = MakeOrderLocators.order_comment
        self.driver.find_element(*input).send_keys(str)

    def click_on_send_order_button(self):
        button = MakeOrderLocators.send_order_button
        self.driver.find_element(*button).click()

    def confirm_order(self):
        button = MakeOrderLocators.yes_button
        self.driver.find_element(*button).click()

    def go_back_by_samocat_logo_clicking(self):
        button = MakeOrderLocators.samocat_logo
        self.driver.find_element(*button).click()

    def go_to_yandex_main_page_by_clicking_yandex_logo(self):
        button = MakeOrderLocators.yandex_logo
        self.driver.find_element(*button).click()