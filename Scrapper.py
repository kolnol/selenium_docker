from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from RouterClient import RouterClient

class Scrapper:
    def __init__(self, router_url, router_password) -> None:
        self.router_url = router_url
        self.router_password = router_password

    def set_chrome_options(self) -> Options:
        """Sets chrome options for Selenium.
        Chrome options for headless browser is enabled.
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return chrome_options

    def setup_driver(self):
        chrome_options = self.set_chrome_options()
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(800, 600)
        return driver

    # TODO adjust to own router
    def scrap_out_of_it(self, driver):
        client = RouterClient(driver, self.router_url)
        title = client \
                    .login(self.router_password) \
                    .get_page_title()
        print(title)

    def run(self):
        try:
            driver = self.setup_driver()
            print(f'Driver is ready. Starting scraping {self.router_url}...')
            self.scrap_out_of_it(driver)
        except Exception as shit:
            print('Failed scrapping! The following exception occured:')
            print(shit)
            return None
        finally:
            driver.close()