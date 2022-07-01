from selenium.webdriver.common.by import By


class SignByEmailLocators:
    log_in_username = (By.NAME, "email")
    log_in_password = (By.NAME, "password")
    sign_in_button = (By.XPATH, "//button//span[text()=' Sign In ']")
    esp_text = (By.XPATH, "//div[text()='Enterprise Submission Platform']")
