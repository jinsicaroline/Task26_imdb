from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Define locators for the search fields and buttons
        self.name_input = (By.NAME, "name-text-input")  # Example locator, adjust as needed
        self.birth_year_start_input = (By.NAME, "birth-date-start-input")  # Example locator, adjust as needed
        self.birth_year_end_input = (By.NAME, "birth-date-end-input")  # Example locator, adjust as needed
        self.search_button = (By.XPATH, "//button[@type='submit']")  # Example locator, adjust as needed

    def enter_name(self, name: str):
        try:
            name_field = self.wait.until(EC.visibility_of_element_located(self.name_input))
            name_field.clear()
            name_field.send_keys(name)
        except TimeoutException:
            print("Failed to find the name input field.")

    def select_gender(self, gender: str):
        try:
            gender_dropdown = self.wait.until(EC.element_to_be_clickable(self.gender_select))
            gender_dropdown.click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//option[text()='{gender}']"))).click()
        except TimeoutException:
            print(f"Failed to select the gender option: {gender}")

    def enter_birth_year_range(self, start_year: str, end_year: str):
        try:
            start_year_field = self.wait.until(EC.visibility_of_element_located(self.birth_year_start_input))
            start_year_field.clear()
            start_year_field.send_keys(start_year)

            end_year_field = self.wait.until(EC.visibility_of_element_located(self.birth_year_end_input))
            end_year_field.clear()
            end_year_field.send_keys(end_year)
        except TimeoutException:
            print("Failed to enter birth year range.")

    def click_search(self):
        try:
            search_button = self.wait.until(EC.element_to_be_clickable(self.search_button))

            # Scroll the element into view if necessary
            self.driver.execute_script("arguments[0].scrollIntoView(true);", search_button)

            # Wait until the element is clickable
            self.wait.until(EC.element_to_be_clickable(self.search_button))

            # Try clicking the search button
            search_button.click()
        except TimeoutException:
            print("Failed to click the search button.")
        except ElementClickInterceptedException:
            # Additional handling if the click is intercepted
            print("Click was intercepted; attempting to handle the issue.")
            # Optionally, add additional steps here to handle the issue
