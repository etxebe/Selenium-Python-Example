from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def navigate(self):
        self.driver.get(self.url)

    def is_page_loaded(self, elem):
        delay = 10  # seconds
        try:
            WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(elem))
        except TimeoutError:
            print('Page is not ready!!')

    def get_text_from_element(self, *elem):
        return self.driver.find_element(*elem).text