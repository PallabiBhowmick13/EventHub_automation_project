import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.event_page import EventPage
from utilities.logger import get_logger

logger = get_logger()


@pytest.fixture
def driver():
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    drv.maximize_window()
    yield drv
    drv.quit()


def test_login_and_event_page(driver):
    logger.info("Starting Test Execution")

    try:
        # Login Page
        driver.get("https://eventhub.rahulshettyacademy.com/login")

        login_page = LoginPage(driver)
        login_page.login("student@example.com", "secret123")

        logger.info("Login successful and Home page loaded")

        os.makedirs("screenshots", exist_ok=True)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@id='nav-events']"))
        )
        driver.save_screenshot("screenshots/login_success.png")
        logger.info("Screenshot Captured")

        # Event Page
        event = EventPage(driver)
        event.click_event_tab()

        assert driver.current_url == "https://eventhub.rahulshettyacademy.com/events"
        logger.info("Event URL Verified")

        e_page_text = event.get_event_page_text()
        expected_text = "Upcoming Events\nFind your next unforgettable experience"
        assert expected_text in e_page_text
        logger.info("Event Page Text Verified")

        logger.info("EVENT TEST PASSED")

        time.sleep(2)
        driver.save_screenshot("screenshots/event_page.png")
        logger.info("Event Page Screenshot Captured")

    except Exception as e:
        logger.error(f"Test Failed: {str(e)}")
        driver.save_screenshot("screenshots/test_failure.png")
        logger.debug(f"Current URL: {driver.current_url}")
        logger.debug(f"Page Title: {driver.title}")
        raise   # <-- IMPORTANT: re-raise so pytest marks it as FAILED