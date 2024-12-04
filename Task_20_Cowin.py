# Import necessary libraries for web automation using Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Data class contains URL
class Data:
   url = "https://www.cowin.gov.in/"

# Class for web-elements locator
class Locators:
   faq = "FAQ"
   partners = "PARTNERS"

# Class for webpage automation with constructor
class WindowsAutomation(Data,Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Set an explicit wait to wait for elements to become interactable (up to 10 seconds)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get(self.url)


    def browserWindows(self):
        try:
            # Wait until the FAQ link is clickable and click it
            faq_element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.faq)))
            faq_element.click()

            # Wait until the Partners link is clickable and click it
            partner_element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.partners)))
            partner_element.click()

            # Get handles of all open windows
            windowsID = self.driver.window_handles

            # Switch to the new windows and print their IDs
            for id in windowsID:
                self.driver.switch_to.window(id)
                print("Browser Window ID:", id)

            # Close two new windows and come back to Home page
            for id in windowsID[1:]:
                self.driver.switch_to.window(id)
                self.driver.close()

            # Switch back to main window
            self.driver.switch_to.window(windowsID[0])
            return windowsID

        # If an exception occurs during execution, print the error message
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.driver.close()