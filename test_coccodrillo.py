import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Możesz zmienić na Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_open_coccodrillo(driver):
    driver.get("https://pl.coccodrillo.eu/")
    time.sleep(5)
    assert "Coccodrillo" in driver.title, "Strona nie otworzyła się poprawnie"

#def test_go_to_niemowlak(driver):
 #   driver.get("https://pl.coccodrillo.eu/")
    
    # Znalezienie zakładki "Niemowlak 0-2 lat" i kliknięcie
  #  niemowlak_tab = driver.find_element(By.LINK_TEXT, "Niemowlak 0-2 lat")
   # niemowlak_tab.click()

    # Sprawdzenie, czy strona została poprawnie otwarta
    #assert "Niemowlak" in driver.page_source, "Zakładka Niemowlak się nie otworzyła"

