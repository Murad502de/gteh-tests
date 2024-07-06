import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from base.base_core import BaseCore

# Specify the path to the ChromeDriver and Chrome binary
chrome_driver_path = "/home/alice/chromedriver-linux64/chromedriver"
chrome_binary_path = "/home/alice/chrome-linux64/chrome"


# Set up Chrome options for mobile emulation
def get_mobile_emulation_options(device_name):
    mobile_emulation = {
        "deviceName": device_name
    }
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.binary_location = chrome_binary_path
    return options


# Define the list of devices to test
devices = [
    "iPhone SE",
    "iPhone XR",
    "iPhone 12 Pro",
    "iPhone 14 Pro Max",
    "Pixel 7",
    "Samsung Galaxy S8+",
    "Samsung Galaxy S20 Ultra",
    "iPad Mini",
    "iPad Air",
    "iPad Pro",
    "Samsung Galaxy A51/71",
    "Nest Hub",
    "Nest Hub Max"
]

# Define the URL of the website to test
url_to_test = "https://gteh.pro/"


@pytest.mark.parametrize("device", devices)
def test_no_horizontal_scroll(device):
    # Set up Chrome options with mobile emulation
    device_options = get_mobile_emulation_options(device)

    # Create a Chrome WebDriver session with the specified Chrome binary
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=device_options)

    # Use the BaseCore class for structured operations
    core = BaseCore(driver)

    try:
        # Navigate to the website
        core.route_by_link(url_to_test)

        # Check for horizontal scrolling
        width = driver.execute_script("return document.body.scrollWidth")
        viewport_width = driver.execute_script("return window.innerWidth")
        assert width <= viewport_width, f"Horizontal scroll detected on {device} for URL: {url_to_test}"
    finally:
        # Close the driver
        driver.quit()


if __name__ == "__main__":
    pytest.main()
