from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.event_page import EventPage


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

    print("Login Test Passed")


    # Event Page

    event = EventPage(driver)


    # Click Events

    event.click_event_tab()


    # Verify URL

    assert driver.current_url == \
    "https://eventhub.rahulshettyacademy.com/events"


    print("Event URL Verified")



    # Verify Page Text

    e_page_text = event.get_event_page_text()



    expected_text = (
         "Upcoming Events\nFind your next unforgettable experience"
       
    )
   


    assert expected_text in e_page_text



    print("Event Page Text Verified")

    print("\nEVENT TEST PASSED")



except Exception as e:

    print("\nEVENT TEST FAILED")
    print(e)



finally:

    input("\nPress ENTER to close browser")

    driver.quit()