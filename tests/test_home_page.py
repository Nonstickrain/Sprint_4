from pages.home_page import QASection
from selenium import webdriver
from locators.qa_locators import QuestionsLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options


class TestHomePage:


    @classmethod
    def setup_class(cls):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        cls.driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)

    def test_QA_section_show_answer_for_question_1(self):
        section = QASection(self.driver)

        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.question_1)))
        section.check_question_1_visible()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.answer_1)))

        assert self.driver.find_element(*QuestionsLocators.answer_1).is_displayed()

    def test_QA_section_show_answer_for_question_2(self):
        section = QASection(self.driver)
        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.question_2)))
        section.check_question_2_visible()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.answer_2)))

        assert self.driver.find_element(*QuestionsLocators.answer_2).is_displayed()

    def test_QA_section_show_answer_for_question_3(self):
        section = QASection(self.driver)
        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.question_3)))
        section.check_question_3_visible()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.answer_3)))

        assert self.driver.find_element(*QuestionsLocators.answer_3).is_displayed()

    def test_QA_section_show_answer_for_question_4(self):
        section = QASection(self.driver)
        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.question_4)))
        section.check_question_4_visible()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.answer_4)))

        assert self.driver.find_element(*QuestionsLocators.answer_4).is_displayed()

    def test_QA_section_show_answer_for_question_5(self):
        section = QASection(self.driver)
        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.question_5)))
        section.check_question_5_visible()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.answer_5)))

        assert self.driver.find_element(*QuestionsLocators.answer_5).is_displayed()

    def test_QA_section_show_answer_for_question_6(self):
        section = QASection(self.driver)
        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.question_6)))
        section.check_question_6_visible()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.answer_6)))

        assert self.driver.find_element(*QuestionsLocators.answer_6).is_displayed()

    def test_QA_section_show_answer_for_question_7(self):
        section = QASection(self.driver)
        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.question_7)))
        section.check_question_7_visible()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.answer_7)))

        assert self.driver.find_element(*QuestionsLocators.answer_7).is_displayed()

    def test_QA_section_show_answer_for_question_8(self):
        section = QASection(self.driver)
        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.question_8)))
        section.check_question_8_visible()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((QuestionsLocators.answer_8)))

        assert self.driver.find_element(*QuestionsLocators.answer_8).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()