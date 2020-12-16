import os
import time
from datetime import datetime
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Instantiate Chromedriver object

class chrome_bot():
    def __init__(self, download_dir):
        self.download_dir = download_dir
        self.executable_path = os.path.join(os.path.join(os.getcwd(), "webdriver"), 'chromedriver.exe')
        self.driver = None

    def initiate_driver(self):
        now = datetime.now()
        date = now.strftime("%d %b %Y")
        currenttime = now.strftime("%H-%M-%S")

        chromeoptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory': self.download_dir,
                 "plugins.always_open_pdf_externally": True}

        chromeoptions.add_experimental_option("prefs", prefs)
        chromeoptions.add_argument('--kiosk-printing')

        driver = webdriver.Chrome(options=chromeoptions,
                                  executable_path=self.executable_path)

        driver.get("https://www.bestbuy.com/")
        print("Bot initiated")

        self.driver = driver

        return driver


    def handle_cart(self):
        driver = self.driver
        driver.get('https://www.bestbuy.com/cart')
        beeps = 5
        for x in range(beeps):
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)

    def loop_wait_and_add_to_cart(self, url):
        driver = self.driver
        # element = driver.find_element_by_partial_link_text("Add to Cart")
        index = 0
        not_available = True
        while not_available:
            try:
                driver.get(url)
                # driver.get("https://www.bestbuy.com/site/cyberpunk-2077-standard-edition-xbox-one-xbox-series-x/6255136.p?skuId=6255136")
                element = driver.find_element_by_xpath("//button[contains(text(), 'Add to Cart')]")
                element.click()
                time.sleep(2)
                not_available = False
                self.handle_cart(driver)
            except BaseException as e:
                # print("Exception fired")
                # print(str(e))

                time.sleep(2)
                pass
            index += 1






