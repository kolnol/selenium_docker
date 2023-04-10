from Scrapper import Scrapper
import os

# import chromedriver_autoinstaller
# chromedriver_autoinstaller.install()

def scrap_internal():
    router_url = os.getenv('ROUTER_URL')
    if router_url is None:
        raise AttributeError('ROUTER_URL is not set in an environment.')

    router_password = os.getenv('ROUTER_PASSWORD')
    if router_password is None:
        raise AttributeError('ROUTER_PASSWORD is not set in an environment.')
    
    print('=' * 10)
    scrapper = Scrapper(router_url, router_password)
    print('Running scraping ...')
    scrapper.run()
    print('=' * 10)

if __name__ == "__main__":
    scrap_internal()