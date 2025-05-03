from modules.registration_page import RegistrationPage


def test_practice_form(browser_conf):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Oksana')
    registration_page.fill_last_name('Ivanova')
    registration_page.fill_email('ivanova_oksana@mail.ru')
    registration_page.fill_gender()
    registration_page.fill_phone('8987456327')
    registration_page.fill_date_of_birth('1999','February','15')
    registration_page.fill_subjects('Physics')
    registration_page.fill_hobbies()
    registration_page.upload_picture('../resources/test_image.jpg')
    registration_page.fill_address('ul. Pobednaya, d.7, kv.55')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Panipat')
    registration_page.submit()

    # THEN
    registration_page.should_title_form('Thanks for submitting the form')
    registration_page.should_registred_user_with(
        'Label Values',
        'Student Name Oksana Ivanova',
        'Student Email ivanova_oksana@mail.ru',
        'Gender Female',
        'Mobile 8987456327',
        'Date of Birth 15 February,1999',
        'Subjects Physics',
        'Hobbies Reading',
        'Picture test_image.jpg',
        'Address ul. Pobednaya, d.7, kv.55',
        'State and City Haryana Panipat'
    )

