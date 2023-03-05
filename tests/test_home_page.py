import pytest
from pages.home_page import QASection
from locators.qa_locators import QuestionsLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("start_browser")
class TestHomePage:

    @pytest.mark.parametrize('question_input, answer_input',[(QuestionsLocators.question_1,QuestionsLocators.answer_1),(QuestionsLocators.question_2,QuestionsLocators.answer_2),(QuestionsLocators.question_3,QuestionsLocators.answer_3),(QuestionsLocators.question_4, QuestionsLocators.answer_4),(QuestionsLocators.question_5,QuestionsLocators.answer_5),(QuestionsLocators.question_6,QuestionsLocators.answer_6),(QuestionsLocators.question_7,QuestionsLocators.answer_7),(QuestionsLocators.question_8,QuestionsLocators.answer_8)])
    def test_QA_section_show_answer_for_question(self, question_input, answer_input):
        section = QASection(self.driver)
        section.go_to_QA_section()

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((question_input)))
        section.check_question_visible(question_input)

        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((answer_input)))

        assert self.driver.find_element(*answer_input).is_displayed()

        self.driver.quit()
