from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = "!")
client.remove_command("help")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.group(invoke_without_command=True)
async def help(ctx):
    if ctx.channel.name != 'krunker':
        return
    
    em = discord.Embed(title = "Krunker Bot Help", description="""*Krunker Bot* is the bot that help you create your krunker games.
    Use ```!help <command>``` to get the full description and settings of a special command, Enjoy !""")

    em.add_field(name="Create Krunker Game", value="```!help krunker```")
    em.add_field(name="Stop the current game", value="```!help stop```")

    await ctx.send(embed = em)

@help.command()
async def krunker(ctx):
    em = discord.Embed(title = "Krunker", description = "Create a default Gun Game")
    em.add_field(name = "**Syntax**", value="```!krunker```")
    await ctx.send(embed = em)

@help.command()
async def stop(ctx):
    em = discord.Embed(title = "Stop", description = "Stop the current Krunker Game")
    em.add_field(name = "**Syntax**", value="```!stop```")
    await ctx.send(embed = em) 

# chrome options
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
if (not os.getenv('Debug')):
    # Production Settings
    option.add_argument("--headless")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    option.binary_location = os.getenv("GOOGLE_CHROME_BIN")

PATH = os.getenv('CHROME_PATH')
# Starting Chrome Driver
driver = webdriver.Chrome(executable_path=PATH, options=option)
driver.implicitly_wait(20) # seconds


@client.command()
async def krunker(ctx):
    if ctx.channel.name != 'krunker':
        return

    # Starting Automation
    await ctx.channel.send('We are creating your game, please wait')
    driver.get("https://krunker.io/")
    try:
        print("Clicking Cookies Accept Button")
        cookieElement = driver.find_element_by_id('onetrust-accept-btn-handler')
        cookieElement.click()
    except:
        print("Already clicked on Cookies")
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
    driver.execute_script("arguments[0].setAttribute('value','5')", playersElement)
    minuteElement = driver.find_element_by_id('customSgameTime')
    driver.execute_script("arguments[0].setAttribute('value','15')", minuteElement)
    print("Starting Server")
    driver.find_element_by_id('passCode').send_keys('love')
    startServer = driver.find_element_by_xpath("//div[@id='hostActionH']/a")
    startServer.click()
    tmpElem = driver.find_element_by_xpath("//div[@id='hostGameMsg']/a")
    tmpElem.click()
    await ctx.channel.send('A new default gun game has been created : {}'.format(driver.current_url))
        
@client.command()
async def stop(ctx):
    if ctx.channel.name != 'krunker':
        return
    driver.get("https://www.google.com")
    await ctx.channel.send('Your game has been stopped')

client.run(os.getenv('TOKEN'))