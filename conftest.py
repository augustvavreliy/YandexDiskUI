import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime

@pytest.fixture(scope='function', autouse=True)
def test_log(request):
    os.system('echo - - -')
    os.system('echo TEST: ' + request.node.name + ', STARTED AT: ' + datetime.now().strftime("%H:%M:%S"))
    
    def fin():
        test_result = ""
        if request.node.rep_call.failed:
            test_result = "Failure"
        if request.node.rep_call.passed:
            test_result = "Success"    
        os.system('echo - - -')
        os.system('echo TEST: ' + request.node.name + ', COMPLETED AT: ' + datetime.now().strftime("%H:%M:%S"))
        os.system('echo TEST RESULT IS: ' + test_result)

    request.addfinalizer(fin)         

@pytest.fixture(scope='module', autouse='True')
def new_browser_window(setup):
    setup.switch_to.new_window()
    yield setup

@pytest.fixture(scope="session")
def setup(request):
    browser = request.config.getoption("--browser")
    #выбор браузера
    driver = None
        
    if browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--disable-dev-shm-usage')
        firefox_options.page_load_strategy = 'normal'        
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--allow-running-insecure-content')
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)            
    os.system('echo - - -')
    os.system('echo Driver was created: ' + datetime.now().strftime("%H:%M:%S"))
    yield driver
    driver.close()
    driver.quit()
