from data import users
from modules.registration_page import RegistrationPage


def test_practice_form(browser_conf):
    registration_page = RegistrationPage()
    student = users.student

    registration_page.open()
    registration_page.register(student)
    registration_page.should_title_form()
    registration_page.should_registred_user_with(student)
