from playwright.sync_api import Page, expect

url = "https://www.qa-practice.com/forms/practice-form"


def test_open_form(page: Page):
    page.goto(url)
    expect(page).to_have_url(url)

    first_name = page.locator("#firstName")
    first_name.fill("Danil")

    last_name = page.locator("#lastName")
    last_name.fill("Agafonov")

    userEmail = page.locator("#userEmail")
    userEmail.fill("danyaagaffonov04@gmail.com")

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

    expect(first_name).to_have_value("Danil")
    expect(last_name).to_have_value("Agafonov")
    expect(userEmail).to_have_value("danyaagaffonov04@gmail.com")
    expect(gender_radio_button).to_be_checked()
    expect(number_of_telephone).to_have_value("8950568062")
    expect(current_address).to_have_value("Kaliningrad")
    expect(checkbox_sports).to_be_checked()
    expect(checkbox_music).to_be_checked()

    header_of_table = page.locator("#resultsModalLabel")
    expect(header_of_table).to_have_text("Thanks for submitting the form")

    expect(page.locator("#resultsModal")).to_contain_text("Danil")
    expect(page.locator("#resultsModal")).to_contain_text("Agafonov")
    expect(page.locator("#resultsModal")).to_contain_text("danyaagaffonov04@gmail.com")
    expect(page.locator("#resultsModal")).to_contain_text("8950568062")
    expect(page.locator("#resultsModal")).to_contain_text("Kaliningrad")
    expect(page.locator("#resultsModal")).to_contain_text("Uttar Pradesh")
