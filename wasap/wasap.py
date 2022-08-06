
from os import path
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Wasap():
    DEFAULT_USER_DATA_DIR = path.expanduser("~/.wasap/data")

    def __init__(self, user_data_dir=None):
        chrome_options = ChromeOptions()
        chrome_options.add_argument(
            f"--user-data-dir={user_data_dir or self.DEFAULT_USER_DATA_DIR}")
        self.driver = Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 600)

    def __enter__(self):
        self.driver.get("https://web.whatsapp.com")
        self.is_ready = self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#side [role=textbox]")))
        return self

    def __exit__(self, *args, **kwargs):
        self.driver.quit()

    def select_chat(self, contact_name):
        search_button = self.wait.until(
            lambda x: x.find_element_by_css_selector("#side button"))
        search_button.click()
        search_textbox = self.wait.until(
            lambda x: x.find_element_by_css_selector("#side [role=textbox]"))
        search_textbox.send_keys(contact_name)
        chat = self.wait.until(
            lambda x: x.find_element_by_css_selector("#side [role=row]"))
        chat.click()

    def send_message(self, message):
        input_textbox = self.wait.until(
            lambda x: x.find_element_by_css_selector("#main [role=textbox]"))
        for line in message.split("\n"):
            input_textbox.send_keys(line)
            input_textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        input_textbox.send_keys(Keys.ENTER)
