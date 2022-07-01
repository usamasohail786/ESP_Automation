import unittest


from ddt import ddt, file_data
import pytest
from ESP_Test.src.pages.sign_in_email import SignByEmail


@pytest.mark.usefixtures("init_driver")
@ddt
class TestSignInEmail(unittest.TestCase):
    @file_data('../testdata/loginbyemail.json')
    def test_sign_in_email_func(self, email, password):
        sign_in_email_obj = SignByEmail(self.driver)
        sign_in_email_obj.url_call()
        sign_in_email_obj.sign_in_with_email_id(email)
        sign_in_email_obj.sign_in_with_password(password)
        sign_in_email_obj.click_sign_in_button()
        body_text = sign_in_email_obj.verify_by_text()
        assert 'Enterprise Submission Platform' in body_text
