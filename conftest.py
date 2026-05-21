import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name"
    )


@pytest.fixture()
def browser_setup(request):

    browser = request.config.getoption("--browser")
    print("Selected Browser:", browser)

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser in ["chrome_headless", "headless"]:

        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Browser not supported: {browser}")

    driver.maximize_window()

    # Assign driver to class
    request.cls.driver = driver

    yield driver

    driver.quit()
    print("Browser Closed")