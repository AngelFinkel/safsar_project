from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import pytest


auto_path_to_driver = ChromeDriverManager().install()
chrome_service = Service(auto_path_to_driver)
chrome_options = Options()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)



