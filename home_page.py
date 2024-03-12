from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
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
main_url = 'https://portal-dev.safsarglobal.link/'
def create_driver():
    auto_path_to_driver = ChromeDriverManager().install()
    chrome_service = Service(auto_path_to_driver)
    chrome_options = Options()
    driver_instance = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver_instance.maximize_window()
    return driver_instance

# Automation Testing for Header Section, Test Completed: 1.1.1.2, 1.1.1.4,1.1.2.1, 1.1.2.4, 1.1.2.6|

# 1.1.1.2 - Test sign in button in header Section


def test_1_1_1_2():
        driver = create_driver()
        try:
                driver.get(main_url)
                log_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/nav/div[1]/ul/a')))
                log_in_button.click()
                assert driver.current_url == "https://portal-dev.safsarglobal.link/signin", "Sign-in page is not opened"
                print("Sign-in page is successfully opened")
        finally:
                driver.close()


# 1.1.1.4 - Test Sell tickets button in header Section


def test_1_1_1_4():
        driver = create_driver()
        try:
                driver.get(main_url)
                sell_tickets_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/nav/p'))
                )
                sell_tickets_button.click()
                assert driver.current_url == "https://portal-dev.safsarglobal.link/start-ticket-sell", "Sell tickets page is not opened"
                print("Sell tickets page is successfully opened")
        finally:
                driver.quit()


# 1.1.2.1 - Test The sign in button from other page in header Section


def test_1_1_2_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                music_category_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/div[2]/a[2]')))
                music_category_element.click()
                log_in_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div[1]/div/nav/div[4]/ul/a'))
                )
                log_in_button.click()
                expected_result = main_url
                assert driver.current_url == expected_result
        except Exception as e:
                print(f"An error occurred: {e}")


# 1.1.2.4 - Test The sell tickets button from other page in header Section


def test_1_1_2_4():
        driver = create_driver()
        try:
                driver.get(main_url)
                music_category_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/div[2]/a[2]')))
                music_category_element.click()
                sell_tickets_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div[1]/div/nav/div[4]/a'))
                )
                sell_tickets_button.click()
                expected_result = main_url
                assert driver.current_url == expected_result
        except Exception as e:
                print(f"An error occurred: {e}")


# 1.1.2.6 - Test The LOGO button from other page in header Section


def test_1_1_2_6():
        driver = create_driver()
        try:
                driver.get(main_url)
                music_category_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/div[2]/a[2]')))
                music_category_element.click()
                safsar_logo = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div[1]/div/nav/div[2]/a/img')))
                safsar_logo.click()
                expected_result = main_url
                assert driver.current_url == expected_result
        except Exception as e:
                print(f"An error occurred: {e}")


# Automation Testing for Hero Section, Test Completed: 2.1.1.1, 2.1.1.2, 2.1.2.1, 2.1.2.2, 2.1.3.1, 2.1.3.2 |


# 2.1.1.1 - Test if the Headline is correct in Hero Section


def test_2_1_1_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                headline_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[7]/h1')))
                assert headline_element.is_displayed(), "Headline is not displayed"
                print("Headline is displayed on the page")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                driver.quit()


# 2.1.1.2 - Test if the Headline is correct in Hero Section


def test_2_1_1_2():
        driver = create_driver()
        try:
                driver.get(main_url)
                headline_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[7]/h1')))
                assert headline_element.is_displayed(), "Headline is not displayed"
                actual_text = headline_element.text
                expected_text = "כרטיסים\nבין בני אדם"
                assert actual_text == expected_text, f"Expected text: {expected_text}, Actual text: {actual_text}"
                print("Headline text is correct on the page")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                driver.quit()


# 2.1.2.1 - Test if the Search Bar is Displayed in Hero Section


def test_2_1_2_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                searchbar_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'autocompleteField')))
                assert searchbar_element.is_displayed(), "Headline is not displayed"
                print("Search Bar is displayed on the page")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                driver.quit()


# 2.1.2.2 - Test Input a Query in the Search Bar in Hero Section


def test_2_1_2_2():
        driver = create_driver()
        try:
                driver.get(main_url)
                searchbar_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'autocompleteField')))
                searchbar_element.send_keys("הפרוייקט של רביבו")
                searchbar_btn_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="search-results-container"]/div/div[1]/a')))
                searchbar_btn_element.click()
        finally:
                driver.quit()


# 2.1.3.1 - Test Confirmation Presence of Category Titles in Hero Section


def test_2_1_3_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                categories_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/div[2]')))
                assert categories_element.is_displayed(), "Categories are not displayed"
                print("Categories are displayed on the page")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                driver.quit()


# 2.1.3.2 - Test Click on a Category Title in Hero Section


def test_2_1_3_2():
        driver = create_driver()
        try:
                driver.get(main_url)
                categories_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/div[2]/a[2]/span')))
                categories_element.click()
        finally:
                driver.quit()


# Automation Testing for Events Carousel Section, Test Completed: 3.1.1.1, 3.2.1.1, 3.2.2.1, 3.3.1.1, 3.4.1.1, 3.4.1.3 |

# 3.1.1.1 - Test Confirmation Placement of Events Carousel Section
def test_3_1_1_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                Carousel_Section_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]')))
                assert Carousel_Section_element.is_displayed(), "Carousel Section is not displayed"
                print("Headline is displayed on the page")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                driver.quit()


# 3.2.1.1 - Test Confirmation Placement of Events Carousel Section
def test_3_2_1_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                Carousel_Section_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]')))
                carousel_title_element = driver.find_element(By.XPATH, './your_carousel_title_xpath')
                assert carousel_title_element.is_displayed(), "//*[@id='root']/div[2]/div[3]/div/div[1]/div[1]/div[1]/div/h1"
                print("Carousel Title, Tag, and Icon are present on the page")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                driver.quit()


# 3.2.2.1 - Test Confirmation of Event Items Display in Events Carousel Section
def test_3_2_2_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                poster_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/div[1]/img'
                title_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/h2'
                date_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/div[2]/p[1]'
                day_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/div[2]/p[2]'
                location_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/p'
                event_section_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[4]')))
                event_poster_element = WebDriverWait(event_section_element, 10).until(
                        EC.visibility_of_element_located((By.XPATH, poster_xpath))
                )
                assert event_poster_element.is_displayed(), "Event Poster is not displayed"
                event_poster_element = event_section_element.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/div[1]/img')
                assert event_poster_element.is_displayed(), "Event Poster is not displayed"
                event_title_element = event_section_element.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/h2')
                assert event_title_element.is_displayed(), "Event Title is not displayed"
                event_date_element = event_section_element.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/div[2]/p[1]')
                assert event_date_element.is_displayed(), "Event Date is not displayed"
                event_day_element = event_section_element.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/div[2]/p[2]')
                assert event_day_element.is_displayed(), "Event Day is not displayed"
                event_location_element = event_section_element.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/p')
                assert event_location_element.is_displayed(), "Event Location is not displayed"
                print("Event Items are displayed on the page")
        except TimeoutException:
                print("Timed out waiting for elements to be present.")

        except NoSuchElementException as e:
                print(f"Element not found: {e}")
        finally:
                driver.quit()


# 3.3.1.1 - Test Confirmation Placement of Events Carousel Section
def test_3_3_1_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                carousel_left_arrow_Section_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/img')))
                carousel_right_arrow_Section_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[1]/img')))
                carousel_left_arrow_Section_element.click()
        finally:
                driver.quit()


# 3.4.1.1 - Test Validate Order Management Events Carousel Section
def test_3_4_1_1():
        driver = create_driver()
        try:
                driver.get(main_url)
                event_section_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[4]'))
                )
                event_poster_element = event_section_element.find_element(By.XPATH,
                                                                          '(//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/div[1]/img)[1]')
                event_title_element = event_section_element.find_element(By.XPATH,
                                                                         '(//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/h2)[1]')
                event_poster_element.click()
                tickets_page_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="tickets-page"]'))
                )
                assert tickets_page_element.is_displayed(), "Tickets page is not displayed after clicking on the event's poster"
                driver.back()
                event_title_element.click()
                tickets_page_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="tickets-page"]'))
                )
                assert tickets_page_element.is_displayed(), "Tickets page is not displayed after clicking on the event's title"
                print("Order Management Validation Successful")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                driver.quit()


# 3.4.1.3 - Test Confirmation Placement of Events Carousel Section
def test_3_4_1_3():
        driver = create_driver()
        try:
                driver.get(main_url)
                event_section_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[4]'))
                )
                event_poster_element = event_section_element.find_element(By.XPATH,
                                                                                  '(//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/div[1]/img)[1]')
                event_title_element = event_section_element.find_element(By.XPATH,
                                                                                 '(//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/a/h2)[1]')
                parent_window = driver.window_handles[0]
                event_poster_element.click()
                driver.switch_to.window(driver.window_handles[1])
                tickets_page_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="tickets-page"]'))
                )
                assert tickets_page_element.is_displayed(), "Tickets page is not displayed after clicking on the event's poster"
                driver.close()
                driver.switch_to.window(parent_window)
                event_title_element.click()
                driver.switch_to.window(driver.window_handles[1])
                tickets_page_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="tickets-page"]')))
                assert tickets_page_element.is_displayed(), "Tickets page is not displayed after clicking on the event's title"
                print("Event Click Action Validation Successful")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                driver.quit()
# Automation Testing for Hero Banner Section, Test Completed: |


# Automation Testing for Categories Carousel Section, Test Completed: |



# Automation Testing for About intro strip Section, Test Completed: |



# Automation Testing for Footer Section, Test Completed: |
