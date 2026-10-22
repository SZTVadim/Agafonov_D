from playwright.sync_api import Page, expect

url = "https://www.qa-practice.com/forms/practice-form"


def test_open_form(page: Page):
    page.goto(url)
    expect(page).to_have_url(url)

    first_name = page.locator("#firstName")
    first_name.fill("Danil")

    last_name = page.locator("#lastName")
    last_name.fill("Agafonov")

    user_email = page.locator("#userEmail")
    user_email.fill("danyaagaffonov04@gmail.com")

    gender_radio_button = page.locator("#gender_0")
    gender_radio_button.check()

    number_of_telephone = page.locator("#userNumber")
    number_of_telephone.fill("8950568062")

    date_of_birth = page.locator("#dateOfBirthInput")
    date_of_birth.fill("13 June 2004")

    subject = page.locator("#subjectsAutocomplete")
    subject.fill("Engl")
    subject_list = page.locator("#subjectsSuggestions")
    subject_list.get_by_text("English").click()

    checkbox_sports = page.locator("#hobbies_0")
    checkbox_sports.check()

    checkbox_music = page.locator("#hobbies_2")
    checkbox_music.check()

    current_address = page.locator("#currentAddress")
    current_address.fill("Kaliningrad")

    state = page.locator("#div_id_state .custom-dropdown-control")
    state.click()
    state_option = page.locator(".custom-dropdown-option[data-value='Uttar Pradesh']")
    state_option.click()
    expect(state).to_contain_text("Uttar Pradesh")

    city = page.locator("#div_id_city .custom-dropdown-control")
    city.click()
    city_option = page.locator("#div_id_city .custom-dropdown-option[data-value='Agra']")
    city_option.click()
    expect(city).to_contain_text("Agra")

    button_submit = page.locator("#submit-id-submit")
    button_submit.click()

    result_title_locator = page.locator("#resultsModalLabel")

    student_name_locator = page.locator("//tr[td[1][text()='Student Name']]/td[2]")
    student_email_locator = page.locator("//tr[td[1][text()='Student Email']]/td[2]")
    gender_locator = page.locator("//tr[td[1][text()='Gender']]/td[2]")
    mob_locator = page.locator("//tr[td[1][text()='Mobile']]/td[2]")
    date_of_birth_locator = page.locator("//tr[td[1][text()='Date of Birth']]/td[2]")
    sub_locator = page.locator("//tr[td[1][text()='Subjects']]/td[2]")
    hobbies_locator = page.locator("//tr[td[1][text()='Hobbies']]/td[2]")
    picture_locator = page.locator("//tr[td[1][text()='Picture']]/td[2]")
    addr_locator = page.locator("//tr[td[1][text()='Address']]/td[2]")
    state_city_locator = page.locator("//tr[td[1][text()='State and City']]/td[2]")

    expect(result_title_locator).to_have_text("Thanks for submitting the form")
    expect(student_name_locator).to_have_text("Danil Agafonov")
    expect(student_email_locator).to_have_text("danyaagaffonov04@gmail.com")
    expect(gender_locator).to_have_text("Male")
    expect(mob_locator).to_have_text("8950568062")
    expect(date_of_birth_locator).to_have_text("2004-06-13")
    expect(sub_locator).to_have_text("English")
    expect(hobbies_locator).to_have_text("Sports, Music")
    expect(picture_locator).to_have_text("Not provided")
    expect(addr_locator).to_have_text("Kaliningrad")
    expect(state_city_locator).to_have_text("Uttar Pradesh")