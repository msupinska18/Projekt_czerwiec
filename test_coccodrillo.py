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



