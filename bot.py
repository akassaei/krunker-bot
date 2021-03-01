from selenium import webdriver
# chrome options
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')

# Starting Chrome Driver
PATH = "/Users/ariak/projects/krunker_bot/python/chromedriver"
driver = webdriver.Chrome(executable_path=PATH, options=option)
driver.implicitly_wait(10) # seconds

# Starting Automation
driver.get("https://krunker.io/")
cookieElement = driver.find_element_by_id('onetrust-accept-btn-handler')
cookieElement.click()
hostElement = driver.find_element_by_id('menuBtnHost')
hostElement.click()