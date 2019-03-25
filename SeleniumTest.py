from selenium import webdriver

dir_loc =r'F:\Python-Projects\Learning-Project\Webdrivers\geckodriver.exe'
print(dir_loc)
driver = webdriver.Firefox(dir_loc)


driver.quit()
