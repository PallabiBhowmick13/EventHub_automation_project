from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.event_page import EventPage

import os
from utilities.logger import get_logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

logger = get_logger()
logger.info("Starting Test Execution")

try:

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()


    # Login Page

    driver.get(
        "https://eventhub.rahulshettyacademy.com/login"
    )


    login_page = LoginPage(driver)


    login_page.login(
        "student@example.com",
        "secret123"
    )


    # Wait for Event Tab to Appear After Login
    # WebDriverWait(driver, 15).until(
    # EC.visibility_of_element_located(
    #     (By.XPATH, "//a[@id='nav-events']")
    # )
    # )


    logger.info("Login successful and Home page loaded")

    logger.info("Login Test Passed")

# Capture Screenshot After Login
    os.makedirs("screenshots", exist_ok=True)
      # Wait for Event Tab to Appear After Login
    WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//a[@id='nav-events']")
    )
    )
    driver.save_screenshot(
    "screenshots/login_success.png"
    )

    logger.info("Screenshot Captured")


    # Event Page

    event = EventPage(driver)
  
    # Click Events

    event.click_event_tab()


    # Verify URL

    assert driver.current_url == \
    "https://eventhub.rahulshettyacademy.com/events"


    logger.info("Event URL Verified")


    # Verify Page Text

    e_page_text = event.get_event_page_text()



    expected_text = (
         "Upcoming Events\nFind your next unforgettable experience"
       
    )
   
    assert expected_text in e_page_text


    logger.info("Event Page Text Verified")

    logger.info("EVENT TEST PASSED")

    time.sleep(10)  # Wait for 20 seconds to observe the event page before capturing screenshot
    # Capture Event Page Screenshot
    driver.save_screenshot(
    "screenshots/event_page.png"
    )

    logger.info("Event Page Screenshot Captured")

# Capture Screenshot Only When Test Fails
# Log Exceptions
except Exception as e:

    # logger.error("EVENT TEST FAILED")
    # logger.error(e)
    logger.error(
        f"Test Failed: {str(e)}"
    )

    driver.save_screenshot(
        "screenshots/test_failure.png"
    )

    logger.info("Screenshot saved")
    logger.error(e)


    logger.debug(
    f"Current URL: {driver.current_url}"
    )

    logger.debug(
    f"Page Title: {driver.title}"
    )


finally:

    input("\nPress ENTER to close browser")

    driver.quit()
