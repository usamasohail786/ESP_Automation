from ESP_Test.src.pages.locators.sign_in_email_locators import SignByEmailLocators
from ESP_Test.src.extended.extended import Extended
from ESP_Test.src.helpers.config_helpers import get_base_url


class SignByEmail(SignByEmailLocators):

    def __init__(self, driver):
        self.driver = driver
        self.ex = Extended(self.driver)

    def url_call(self):
        self.driver.maximize_window()
        base_url = get_base_url()
        self.driver.get(base_url)

    def sign_in_with_email_id(self, username):
        self.ex.wait_and_input_text(self.log_in_username, username)

    def sign_in_with_password(self, password):
        self.ex.wait_and_input_text(self.log_in_password, password)

    def click_sign_in_button(self):
        self.ex.wait_and_click(self.sign_in_button)

    def verify_by_text(self):
        return self.ex.wait_and_get_text(self.esp_text)
