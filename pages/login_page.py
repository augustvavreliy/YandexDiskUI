from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    dzen_login_button = (By.CSS_SELECTOR, 'button[class=" base-button__rootElement-12  base-button__m-2y  base-button__regular--M"]')
    yandex_login_button = (By.CSS_SELECTOR, 'div[class=login-content__yaButtonWrapper-15]')
    login_input = (By.CSS_SELECTOR, 'input[class=Textinput-Control]')
    login_button = (By.ID, 'passp:sign-in')
    dzen = (By.CSS_SELECTOR, 'a[rel="dofollow"]')

class LoginPage(BasePage):
    def click_dzen_login_button(self):
        self._find_element_clickable(LoginPageLocators.dzen_login_button)
        self._click(LoginPageLocators.dzen_login_button)

    def click_yandex_login_button(self):
        self._find_element_clickable(LoginPageLocators.yandex_login_button)
        self._click(LoginPageLocators.yandex_login_button)

    def type_login_or_pass(self, value):
        self._type(LoginPageLocators.login_input, value)
    
    def click_login_button(self):
        self._find_element_clickable(LoginPageLocators.login_button).click()

    def dzen_loaded(self):
        self._find_element_visible(LoginPageLocators.dzen)