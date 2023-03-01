from pages.home_page import OrderSection
from pages.order_page import OrderPageUserData, OrderPageOrderData
from selenium import webdriver
from locators.order_locators import MakeOrderLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

class TestOrderPage:


    @classmethod
    def setup_class(cls):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        cls.driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)

    def test_making_order_first_data(self, user_data, order_data):
        section = OrderSection(self.driver)
        user_order_page = OrderPageUserData(self.driver)
        order_page = OrderPageOrderData (self.driver)


        section.click_on_first_make_order_button()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((MakeOrderLocators.firstname)))
        user_order_page.send_text_to_firstname_input(user_data['name'])
        user_order_page.send_text_to_secondname_input(user_data['surname'])
        user_order_page.send_text_to_adress_input(user_data['adress'])
        user_order_page.send_text_to_phone_number_input(user_data['phone number'])
        user_order_page.choose_station_in_metro_selector()

        user_order_page.click_on_next_button()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((MakeOrderLocators.order_data)))
        order_page.send_text_to_data_input(order_data['time'])
        order_page.choose_order_duration()
        order_page.choose_black_color()
        order_page.send_text_to_comment_input(order_data['comment'])
        order_page.click_on_send_order_button()

        order_page.confirm_order()
        assert self.driver.find_element(*MakeOrderLocators.completed_order).is_displayed()


    def test_making_order_second_data(self, user_data, order_data):
        section = OrderSection(self.driver)
        user_order_page = OrderPageUserData(self.driver)
        order_page = OrderPageOrderData(self.driver)

        section.go_to_make_order_section()
        section.click_on_second_order_button()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((MakeOrderLocators.firstname)))
        user_order_page.send_text_to_firstname_input(user_data['name'])
        user_order_page.send_text_to_secondname_input(user_data['surname'])
        user_order_page.send_text_to_adress_input(user_data['adress'])
        user_order_page.send_text_to_phone_number_input(user_data['phone number'])
        user_order_page.choose_station_in_metro_selector()

        user_order_page.click_on_next_button()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((MakeOrderLocators.order_data)))
        order_page.send_text_to_data_input(order_data['time'])
        order_page.choose_order_duration()
        order_page.choose_grey_color()
        order_page.send_text_to_comment_input(order_data['comment'])
        order_page.click_on_send_order_button()

        order_page.confirm_order()
        assert self.driver.find_element(*MakeOrderLocators.completed_order).is_displayed()


    def test_go_back_by_logo(self):
        order_page = OrderPageOrderData(self.driver)

        order_page.see_your_order()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((MakeOrderLocators.samocat_logo)))
        order_page.go_back_by_samocat_logo_clicking()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_go_to_yandex_main_page(self):
        order_page = OrderPageOrderData(self.driver)

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((MakeOrderLocators.yandex_logo)))
        order_page.go_to_yandex_main_page_by_clicking_yandex_logo()

        assert WebDriverWait(self.driver,3).until(expected_conditions.url_changes('https://dzen.ru/?yredirect=true'))



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()