from locators.qa_locators import QuestionsLocators
from locators.order_locators import MakeOrderLocators

class QASection:


    def __init__(self, driver):
        self.driver = driver

    def go_to_QA_section(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        section = self.driver.find_element(*QuestionsLocators.section)
        self.driver.execute_script('arguments[0].scrollIntoView();', section)


    def check_question_1_visible(self):
        question_locator = QuestionsLocators.question_1
        self.driver.find_element(*question_locator).click()

    def check_question_2_visible(self):
        question_locator = QuestionsLocators.question_2
        self.driver.find_element(*question_locator).click()

    def check_question_3_visible(self):
        question_locator = QuestionsLocators.question_3
        self.driver.find_element(*question_locator).click()

    def check_question_4_visible(self):
        question_locator = QuestionsLocators.question_4
        self.driver.find_element(*question_locator).click()

    def check_question_5_visible(self):
        question_locator = QuestionsLocators.question_5
        self.driver.find_element(*question_locator).click()

    def check_question_6_visible(self):
        question_locator = QuestionsLocators.question_6
        self.driver.find_element(*question_locator).click()

    def check_question_7_visible(self):
        question_locator = QuestionsLocators.question_7
        self.driver.find_element(*question_locator).click()

    def check_question_8_visible(self):
        question_locator = QuestionsLocators.question_8
        self.driver.find_element(*question_locator).click()

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