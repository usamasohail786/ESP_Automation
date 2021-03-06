from ESP_Test.src.pages.locators.sign_in_idendi_locators import SignByIDENEDILocators
from ESP_Test.src.extended.extended import Extended
from ESP_Test.src.helpers.config_helpers import get_base_url

import time

class SignByIDendi(SignByIDENEDILocators):

    def __init__(self, driver):
        self.driver = driver
        self.ex = Extended(self.driver)
        self.elem_bool = False

    def url_call(self):
        base_url = get_base_url()
        self.driver.maximize_window()
        self.driver.get(base_url)

    def click_on_idendi_button(self):
        self.ex.wait_and_click(self.idendi_btn)

    def sign_in_with_phone_number(self, phone_number):
        self.ex.wait_and_input_text(self.idendi_phone_number, phone_number)

    def sign_in_with_password(self, password_idendi):
        self.ex.wait_and_input_text(self.idendi_password, password_idendi)

    def click_log_in_button(self):
        self.ex.wait_and_click(self.idendi_log_btn)

    def element_exist(self):
        self.ex.wait_until_element_is_visible(self.profile_img)
        time.sleep(10)
        if self.profile_img:
            print("test........................")
            import pbd; pbd.set_trace()