from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

from RouterClient import RouterClient

def set_chrome_options() -> Options:
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

def setup_driver():
    chrome_options = set_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(800, 600)
    return driver

# TODO adjust to own router
def scrap_out_of_it(driver):
    router_url = '<>'
    router_password = '<>'
    client = RouterClient(driver, router_url)
    title = client \
                .login(router_password) \
                .open_private_network() \
                .get_page_title()
    print(title)

def main():
    try:
        driver = setup_driver()
        print('setup driver')
        scrap_out_of_it(driver)
    except Exception as shit:
        print(f"{shit} happened.")
        return None
    finally:
        driver.close()

if __name__ == "__main__":
    main()