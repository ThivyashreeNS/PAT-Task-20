# Import necessary libraries for web automation using Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import requests

# Data class contains URL
class Data:
   url = "https://labour.gov.in/"

# Class for web-elements locator
class Locators:
    close_button = "open_button"
    documents = "Documents"
    Report = "Monthly Progress Report"
    pdf = "//*[@id='fontSize']/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a"
    media = "Media"
    gallery = "Photo Gallery"
    photos_table = "//table[@class='views-view-grid cols-3']"

# Class for webpage automation with constructor
class WindowsAutomation(Data,Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)
        # Set an explicit wait to wait for elements to become interactable (up to 10 seconds)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def downloadFiles(self):
        try:
            # Close the Ad Banner
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.close_button))).click()

            # Download monthly progress report, select and click
            hover_over_document = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, self.documents)))
            self.action.move_to_element(hover_over_document).perform()
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.Report))).click()
            # Click somewhere outside the dropdown to close it
            self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/th[1]'))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pdf))).click()
            print("clicked")
            alert_window = self.driver.switch_to.alert
            alert_window.accept()

            # Get handles of all open windows
            window_handles = self.driver.window_handles
            # Display window/frame IDs in the console
            for handle in window_handles:
                self.driver.switch_to.window(handle)
            # Close the two new windows and switch back to original window
            for handle in window_handles[1:]:
                self.driver.switch_to.window(handle)
                self.driver.close()
            # Switch back to original window
            self.driver.switch_to.window(window_handles[0])

            hover_over_media = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, self.media)))
            self.action.move_to_element(hover_over_media).perform()
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.gallery))).click()

            self.wait.until(EC.presence_of_element_located((By.XPATH, self.photos_table)))
            # Locate the table element (use the specific XPath to target the table)
            table = self.driver.find_element(By.XPATH, self.photos_table)
            # Now find all the <img> tags within the table
            photos = table.find_elements(By.TAG_NAME, 'img')

            # Create a folder to store the downloaded photos
            folder_path = 'downloaded_photos'
            os.makedirs(folder_path, exist_ok=True)

            # Download the first 10 images
            downloaded_photos_count = 0
            for i, photo in enumerate(photos[:10]):  # Limiting to the first 10 images
                try:
                    photo_url = photo.get_attribute('src')  # Get the 'src' attribute of the image
                    if photo_url:  # Check if the image URL is valid
                        response = requests.get(photo_url)  # Make a GET request to download the image
                        # Save the image in the folder with a proper name
                        with open(os.path.join(folder_path, f'photo_{i + 1}.jpg'), 'wb') as f:
                            f.write(response.content)  # Write the content of the image
                        print(f"Downloaded photo_{i + 1}.jpg")  # Print a message for each successful download
                        downloaded_photos_count += 1
                    else:
                        print(f"Image {i + 1} does not have a valid 'src' URL.")
                except Exception as e:
                    print(f"Error downloading photo {i + 1}: {e}")  # Print an error message if something goes wrong
            return downloaded_photos_count

        # If an exception occurs during execution, print the error message
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.driver.close()