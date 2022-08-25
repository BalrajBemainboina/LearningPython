from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
desired_cap = {
    # Set your access credentials
    "browserstack.user" : "balrajbemainboin_ZgOJfw",
    "browserstack.key" : "dPV5U2AqsKuLbBpvwqfT",
  
    # Set URL of the application under test
    "app" : "bs://8fbaceffe5698a25811544ebfc3c14f9d12d4743",
  
    # Specify device and os_version for testing
    "device" : "Samsung Galaxy S22",
    "os_version" : "12.0",
      
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "myPKFitAppTest"
}
  
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)
time.sleep(4)
elements_list = driver.find_elements_by_class_name("android.widget.TextView")
for element in elements_list:
    if 'Contact Us' in element.text: 
        element.click()
        print(element.text + ' Selected')
        break
time.sleep(3)
elements_listCancel = driver.find_elements_by_class_name("android.widget.TextView")
for element in elements_listCancel:
    if 'Cancel' in element.text: 
        element.click()
        print('Cancel' + ' Selected')
        break
time.sleep(3)
elements_listsign = driver.find_elements_by_class_name("android.widget.TextView")
for element1 in elements_listsign:
    if 'Sign Up' in element1.text: 
        element1.click()
        print('Sign Up' + ' Selected')
        break
elements_listhome = driver.find_elements_by_class_name("android.widget.TextView")
for element2 in elements_listhome:
    if 'Cancel' in element2.text: 
        element2.click()
        print('backtoLogin' + ' Selected')
        break
# If you have uploaded your app, write your test case here. 
time.sleep(2) 
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
