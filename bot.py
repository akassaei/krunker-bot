from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import discord
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# chrome options
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
"""
Production Settings
option.add_argument("--headless")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--no-sandbox")
"""
PATH = os.getenv('CHROME_PATH')
print(PATH)
# Starting Chrome Driver
driver = webdriver.Chrome(executable_path=PATH, options=option)
driver.implicitly_wait(20) # seconds


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!krunker') and message.channel.name == 'krunker':
        # Starting Automation
        await message.channel.send('We are creating your game, please wait')
        driver.get("https://krunker.io/")
        print("Clicking Cookies Accept Button")
        cookieElement = driver.find_element_by_id('onetrust-accept-btn-handler')
        cookieElement.click()
        print("Clicking Host Game Button")
        hostElement = driver.find_element_by_id('menuBtnHost')
        hostElement.click()
        print("Clicking Custom Mode Button")
        customElement = driver.find_element_by_xpath("//div[@id='menuWindow']/div[3]")
        customElement.click()
        print("Changing Settings for the Game")
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
        print("Starting Server")
        driver.find_element_by_id('passCode').send_keys('love')
        startServer = driver.find_element_by_xpath("//div[@id='hostActionH']/a")
        startServer.click()
        tmpElem = driver.find_element_by_xpath("//div[@id='hostGameMsg']/a")
        tmpElem.click()
        await message.channel.send('A new default gun game has been created : {}'.format(driver.current_url))
    
    if message.content.startswith('!stop') and message.channel.name == 'krunker':
        driver.get("https://www.google.com")
        await message.channel.send('Your game has been stopped')


client.run(os.getenv('TOKEN'))