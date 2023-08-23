import pytest
from pages.login_page import LoginPage
from pages.disk_page import DiskPage
import time



def test_login(setup):
    login_page = LoginPage(setup)
    login_page._visit('https://yandex.ru')

    login_page.click_dzen_login_button()
    login_page.click_yandex_login_button()
    login_page.type_login_or_pass('ap1.d')
    login_page.click_login_button()
    time.sleep(1)
    login_page.type_login_or_pass('123wAs123')
    login_page.click_login_button()
    login_page.dzen_loaded()

def test_create_folder(setup):
    disk_page = DiskPage(setup)
    disk_page._visit('https://disk.yandex.ru/client/disk')

    disk_page.click_create_button()
    disk_page.click_create_folder_button()
    time.sleep(1)
    disk_page.type_name('test_folder')
    disk_page.click_save_button()
    time.sleep(2)
    disk_page.click_folder_name()
    time.sleep(2)

def test_create_file(setup):
    disk_page = DiskPage(setup)
    disk_page.click_create_button()
    time.sleep(1)
    disk_page.click_create_file_button()
    time.sleep(2)
    disk_page.type_name('test_file')
    disk_page.click_save_button()
    time.sleep(2)
    setup.switch_to.window(setup.window_handles[-1])
    setup.close()
    setup.switch_to.window(setup.window_handles[1])  
    files = disk_page.get_files()
    for i in range(len(files)):
        if files[i].text == 'test_file.docx':
            assert True
            print('files available')
        else:
            assert False
    