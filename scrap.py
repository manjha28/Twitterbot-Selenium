from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import TwitterFollowBot
from selenium.webdriver.common.action_chains import ActionChains
bot = webdriver.Chrome(r"C:\Users\manis\driver\chromedriver.exe")

bot.get('https://www.youtube.com//')
time.sleep(3)

search = bot.find_element_by_id('search').send_keys('Bounties of Life poem by Manish JHa')
searchnutton = bot.find_element_by_id('search-icon-legacy').click()
time.sleep(5)
BOL = bot.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()