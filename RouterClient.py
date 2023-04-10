from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

class RouterClient:
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.url = url
        self.waiting_for_element_timeout = 5 # seconds. Thank me later cowboy
    
    def login(self, router_password, password_element_id='id_login_password'):
        print ('trying to log in')

        self.driver.get(self.url)
        password_input_element = self.get_element(password_element_id)

        password_input_element.send_keys(router_password)
        password_input_element.send_keys(Keys.ENTER)

        time.sleep(5)
        return self

    def get_element(self, elementid):
        print ('getting element: ' + elementid)
        element = None
        time.sleep(5)
        try:
            element_present = EC.presence_of_element_located((By.ID, elementid))
            element = WebDriverWait(self.driver, self.waiting_for_element_timeout).until(element_present)
        except TimeoutException:
            print ("Timed out waiting for page to load")
        
        if (element is None):
            raise AttributeError(f'No element with id {elementid} found on page {self.url}')
        return element

    def open_private_network(self, private_network_element_id = 'routerText'):
        
        private_network_button_element = self.get_element(private_network_element_id)

        # https://stackoverflow.com/questions/56119289/element-not-interactable-selenium/56119786#56119786       
        self.driver.execute_script("arguments[0].click();", private_network_button_element)
        return self 
    
    def open_management_submenu(self, management_submenu_element_id = 'idmenufoldermanagement'):
        management_menu_element = self.get_element(management_submenu_element_id)

        self.driver.execute_script("arguments[0].click();", management_menu_element)
        return self 

    def open_factory_reset(self, reset_menu_element_id = 'idmenunodereset'):
        reset_menu_element = self.get_element(reset_menu_element_id)

        self.driver.execute_script("arguments[0].click();", reset_menu_element)
        return self 

    def click_reboot(self, restart_button_id = 'id_common_restart'):
        restart_button = self.get_element(restart_button_id)

        # restart_button.click()
        # self.driver.execute_script("arguments[0].click();", restart_button)
        
        print(restart_button.text)
        
        return self

    def get_page_title(self, title_element_id = 'uiPageTitle'):
        title_element = self.driver.find_element_by_id(title_element_id)
        title = title_element.find_element_by_class_name('arrow_box')
        return title.text

