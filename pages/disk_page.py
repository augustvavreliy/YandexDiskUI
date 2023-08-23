from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 

class DiskLocators:
    create_button = (By.CSS_SELECTOR, "button[class='Button2 Button2_view_raised Button2_size_m Button2_width_max']")
    create_folder_button = (By.CSS_SELECTOR, "div[class='create-resource-popup-with-anchor__create-items'] button:nth-child(1)")
    create_file_button = (By.CSS_SELECTOR, "div[class='create-resource-popup-with-anchor__create-items'] button:nth-child(2)")
    name_input = (By.CSS_SELECTOR, "form[class='rename-dialog__rename-form'] input")
    save_button = (By.CSS_SELECTOR, "div[class='confirmation-dialog__footer'] button")
    folder_name = (By.XPATH, "//div[@class='listing-item__info']//span[text()='test_folder']")
    files = (By.CSS_SELECTOR, "div[class='listing__items'] div span")

class DiskPage(BasePage):
    def click_create_button(self):
        self._click(DiskLocators.create_button)
    
    def click_create_folder_button(self):
        self._click(DiskLocators.create_folder_button)

    def type_name(self, name):
        self._type(DiskLocators.name_input, name)
    
    def click_save_button(self):
        self._click(DiskLocators.save_button)
    
    def click_folder_name(self):
        self.doubleclick(DiskLocators.folder_name)
        
    
    def click_create_file_button(self):
        self._click(DiskLocators.create_file_button)

    def get_files(self):
        return self._find_elements(DiskLocators.files)