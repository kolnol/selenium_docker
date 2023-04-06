from selenium.webdriver.common.keys import Keys

class RouterClient:
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.url = url
    
    def login(self, router_password, password_element_id='uiPass'):
        self.driver.get(self.url)
        password_input_element = self.driver.find_element_by_id(password_element_id)
        if (password_input_element is None):
            raise AttributeError(f'No element with id {password_element_id} found on page {self.url}')
        password_input_element.send_keys(router_password)
        password_input_element.send_keys(Keys.ENTER)
        return self

    def open_private_network(self, private_network_element_id = 'lan'):
        private_network_button_element = self.driver.find_element_by_id(private_network_element_id)
        
        if (private_network_button_element is None):
            raise AttributeError(f'No element with id {private_network_element_id} found on page {self.url}')

        private_network_button_element.click()
        network_button_element = self.driver.find_element_by_id('net')
        network_button_element.click()
        return self

    def get_page_title(self, title_element_id = 'uiPageTitle'):
        title_element = self.driver.find_element_by_id(title_element_id)
        title = title_element.find_element_by_class_name('arrow_box')
        return title.text

