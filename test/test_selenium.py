import pytest
from selenium import webdriver
# from test_selenium.webdriver.chrome.options import Options

def test_selenium():
    driver = webdriver.Chrome()

    url = 'https://www.google.com/'
    driver.get(url)

    assert driver.title == 'Google'
    assert driver.current_url == url

