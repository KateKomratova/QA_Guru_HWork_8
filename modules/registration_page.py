import os
from selene import browser, have
from data.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name="gender"]')
        self.phone = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('.custom-checkbox')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.upload_picture = browser.element('#uploadPicture')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')

    def _fill_first_name(self, value):
        self.first_name.type(value)

    def _fill_last_name(self, value):
        self.last_name.type(value)

    def _fill_email(self, value):
        self.email.type(value)

    def _fill_gender(self,value):
        self.gender.element_by(have.value(value)).element('..').click()

    def _fill_phone(self, number):
        self.phone.type(number)

    def _fill_date_of_birth(self, year, month, day):
        # Выбираем дату рождения в календаре
        self.date_of_birth.click()
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option').element_by(have.exact_text(month)).click()
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option').element_by(have.value(year)).click()
        browser.all('.react-datepicker__day').element_by(have.exact_text(day)).click()

    def _fill_subjects(self, subjects):
        self.subjects.type(subjects).press_enter()

    def _fill_hobbies(self,value):
        self.hobbies.element_by(have.text(value)).click()

    def _fill_address(self, value):
        self.address.type(value)

    def _fill_state(self, value):
        self.state.click()
        browser.element('#react-select-3-input').set_value(value).press_tab()

    def _fill_city(self, value):
        self.city.click()
        browser.element('#react-select-4-input').set_value(value).press_tab()

    def _upload_picture(self, file_name):
        absolute_path = os.path.abspath(os.path.join('..', 'resources', file_name))
        self.upload_picture.send_keys(absolute_path)

    def _submit(self):
        self.submit_button.click()

    def should_title_form(self):
        title_registered_form = 'Thanks for submitting the form'
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text(title_registered_form))

    def should_registred_user_with(self, student: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
            f'{student.first_name} {student.last_name}',
            student.email,
            student.gender,
            student.phone,
            f'{student.date_of_birth[2]} {student.date_of_birth[1]},{student.date_of_birth[0]}',
            student.subjects,
            student.hobbies,
            student.image_name,
            student.address,
            f'{student.state} {student.city}',
        )
    )


    def register(self, student: User):
        self._fill_first_name(student.first_name)
        self._fill_last_name(student.last_name)
        self._fill_email(student.email)
        self._fill_gender(student.gender)
        self._fill_phone(student.phone)
        self._fill_date_of_birth(*student.date_of_birth)
        self._fill_subjects(student.subjects)
        self._fill_hobbies(student.hobbies)
        self._upload_picture(student.image_name)
        self._fill_address(student.address)
        self._fill_state(student.state)
        self._fill_city(student.city)
        self._submit()