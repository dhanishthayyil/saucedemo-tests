from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)

    def find(self, locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        self.logger.info(f"Typing '{text}' into: {locator}")
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        text = self.find(locator).text
        self.logger.info(f"Read text '{text}' from: {locator}")
        return text