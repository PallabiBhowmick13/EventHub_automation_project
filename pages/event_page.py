from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventPage:


    def __init__(self, driver):
        self.driver = driver


    event_tab = (
        By.XPATH,
        "//a[@id='nav-events']"
    )


    body = (
        By.XPATH,
        "//body"
    )


    def click_event_tab(self):

        WebDriverWait(
            self.driver,10
        ).until(
            EC.element_to_be_clickable(self.event_tab)
        )

        self.driver.find_element(
            *self.event_tab
        ).click()



    def get_event_page_text(self):

        WebDriverWait(
            self.driver,10
        ).until(
            EC.visibility_of_element_located(self.body)
        )


        return self.driver.find_element(
            *self.body
        ).text