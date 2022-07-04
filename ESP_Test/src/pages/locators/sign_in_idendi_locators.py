from selenium.webdriver.common.by import By


class SignByIDENEDILocators:
    idendi_phone_number = (By.XPATH, "//input[@placeholder='Mobile Number']")
    idendi_password = (By.XPATH, "//input[@placeholder='Password']")
    idendi_btn = (By.XPATH, "//span[@class='mat-button-wrapper']//div[text()=' Sign in with IDENEDI ']")
    idendi_log_btn = (By.XPATH, "//span[@class='ng-scope']")
    esp_text = (By.XPATH, "//div[text()='ESP']")
    profile_img = (By.XPATH, "//img[@class='profile-img']")
