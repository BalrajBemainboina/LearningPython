from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from threading import Thread
import time
# This array 'capabilities' defines the capabilities browser, device and OS combinations where the test will run
load_dotenv()
BUILD_NAME = "browserstack-mypkfitTest"
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "ChromeBrowser",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "firefox",
        "browserVersion": "102.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "FirefoxBrowser",
        "buildName": BUILD_NAME,
    },
]
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())
# run_session function searches for 'BrowserStack' on duckduckgo.com
def run_session(cap):
    cap["userName"] = os.environ.get("BROWSERSTACK_USERNAME") or "balrajbemainboin_ZgOJfw"
    cap["accessKey"] = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "dPV5U2AqsKuLbBpvwqfT"
    options = get_browser_option(cap["browserName"].lower())
    options.set_capability("browserName", cap["browserName"].lower())
    options.set_capability("bstack:options", cap)
    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub", options=options
    )
    driver.get("https://sg-prd-hema.mypkfit.com")
    if not "myPKFiT" in driver.title:
        raise Exception("Unable to load myPKFiT page!")
    driver.maximize_window()
    elem = driver.find_element(By.LINK_TEXT, "India (English)")
    elem.click()
    driver.find_element_by_css_selector("button[ng-click='vm.confirm(vm.selectedCountry)']").click()
    time.sleep(20)
    driver.find_element_by_css_selector("button[ng-click='vm.close()']").click()
    try:
        WebDriverWait(driver, 5).until(EC.title_contains("myPKFiT"))
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}'
        )
    except TimeoutException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}'
        )
    print(driver.title)
    driver.quit()
# The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
