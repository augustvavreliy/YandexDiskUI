from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 

TIMEOUT = 300


class BasePage():

    def __init__(self, driver):
        self.driver = driver
    
        # self.base_url = url

    def _visit(self, url):
        return self.driver.get(url)

    def _go_back(self):
        return self.driver.back()
    
    def close_tab(self):
        self.driver.browser.close()

    def _find_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def _find_element_visible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def _find_element_clickable(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}")

    def _find_elements(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def _find_elements_visible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def _wait_for_element_text_load(self, locator, text, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text),
                                                         message=f"Can't find element by locator {locator} with text {text}")

    def _wait_for_class_attribute_load(self, locator, attribute_text, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(
                locator, 'class', attribute_text),
            message=f"Can't find element by locator {locator} with attribute text {attribute_text}")

    def _wait_for_invisibility_of_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator),
                                                         message=f"The element with locator {locator} is visible")

    def _refresh(self):
        return self.driver.refresh()

    def _type(self, locator, input_text):
        return self._find_element(locator).send_keys(input_text)

    def _click(self, locator):
        return self._find_element(locator).click()

    def _is_not_displayed(self, locator, timeout=TIMEOUT):
        timeout = 2
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    EC.invisibility_of_element_located(
                        (locator)))
            except TimeoutException:
                return False
            except NoSuchElementException:
                return False
            except TimeoutError:
                return False
            return True
        # else:
        #    try:
        #        return self._find_element(locator)
        #    except NoSuchElementException:
        #        return False

    def _is_displayed(self, locator, timeout=TIMEOUT):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    EC.visibility_of_element_located(
                        (locator)))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find_element(locator).is_displayed()
            except NoSuchElementException:
                return False

    def _frame_to_be_available_and_switch_to_it(self, locator, timeout=TIMEOUT):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    EC.frame_to_be_available_and_switch_to_it(
                        (locator)))
            except TimeoutException:
                return False
            return True

    def doubleclick(self, locator):
        element = self._find_element(locator)
        actionChains = ActionChains(self.driver)
        actionChains.double_click(element).perform()