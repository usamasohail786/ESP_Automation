import unittest

from ddt import ddt, file_data
import pytest
from ESP_Test.src.pages.sign_in_idenendi import SignByIDendi
from ESP_Test.src.dictionary import dictionary

@pytest.mark.usefixtures("init_driver")
@ddt
class TestSignByIDENEDI(unittest.TestCase):
    @file_data('../testdata/loginbyidenedi.json')
    def test_sign_in_idenedi_func(self, phone_number, password_idenedi):
        sign_in_idenedi_obj = SignByIDendi(self.driver)
        sign_in_idenedi_obj.url_call()
        sign_in_idenedi_obj.click_on_idendi_button()
        sign_in_idenedi_obj.sign_in_with_phone_number(phone_number)
        sign_in_idenedi_obj.sign_in_with_password(password_idenedi)
        sign_in_idenedi_obj.click_log_in_button()
        value = sign_in_idenedi_obj.element_exist()
        self.assertTrue(value, "Profile image exist so login successfully")



