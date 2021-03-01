from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
customElement = driver.find_element_by_xpath("//div[@id='menuWindow']/div[3]")
customElement.click()
mapElement = driver.find_element_by_xpath("//div[@id='menuWindow']/div[3]/label[2]")
mapElement.click()
ffaElement = driver.find_element_by_xpath("//div[@id='forcedSettings']/div[2]/label[1]")
ggElement = driver.find_element_by_xpath("//div[@id='forcedSettings']/div[2]/label[11]")
ffaElement.click()
ggElement.click()
playersElement = driver.find_element_by_id('customSmaxPlayers')
driver.execute_script("arguments[0].setAttribute('value','4')", playersElement)
minuteElement = driver.find_element_by_id('customSgameTime')
driver.execute_script("arguments[0].setAttribute('value','15')", minuteElement)
driver.find_element_by_id('passCode').send_keys('love')
startServer = driver.find_element_by_xpath("//div[@id='hostActionH']/a")
startServer.click()