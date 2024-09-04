import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Task26 import SearchPage


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.imdb.com/search/name/")
    yield driver
    driver.quit()


def test_search(driver):
    search_page = SearchPage(driver)

    # Example data for searching
    name = "Tom Hanks"


    # Perform search actions
    search_page.enter_name(name)
    #search_page.enter_birth_year_range(birth_year_start, birth_year_end)
    search_page.click_search()

    # Optionally add assertions or further actions to verify the search results
    assert "Tom Hanks" in driver.page_source
