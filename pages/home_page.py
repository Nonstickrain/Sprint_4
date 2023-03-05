from locators.qa_locators import QuestionsLocators
from locators.order_locators import MakeOrderLocators

class QASection:


    def __init__(self, driver):
        self.driver = driver

    def go_to_QA_section(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        section = self.driver.find_element(*QuestionsLocators.section)
        self.driver.execute_script('arguments[0].scrollIntoView();', section)

    def check_question_visible(self, question):
        self.driver.find_element(*question).click()

class OrderSection:

    def __init__(self, driver):
        self.driver = driver

    def click_on_first_make_order_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        button = MakeOrderLocators.make_order_button_1
        self.driver.find_element(*button).click()

    def go_to_make_order_section(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        section = self.driver.find_element(*MakeOrderLocators.make_order_section)
        self.driver.execute_script('arguments[0].scrollIntoView();', section)

    def click_on_second_order_button(self):
        button = MakeOrderLocators.make_order_button_2
        self.driver.find_element(*button).click()