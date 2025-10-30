from selenium import webdriver


def test_open_github():
    driver = webdriver.Chrome()

    url = "https://github.com/"
    driver.get(url)

    assert driver.title == "Github"
    assert driver.current_url == url
