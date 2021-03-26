from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(r"C:\Users\manis\driver\chromedriver.exe")

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        clicklogin = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
        time.sleep(5)
        enteremail = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(self.username)
        time.sleep(5)
        enterpass = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(self.password)
        time.sleep(3)
        clicklgin = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()

    def tweet(self,tweetstuff):
        bot = self.bot
        self.login()
        time.sleep(3)
        writebox = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        time.sleep(15)
        writebox.send_keys(tweetstuff)
        time.sleep(2)
        tweetbutton = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span').click()

    def favourite(self):
        bot = self.bot
        self.login()
        time.sleep(3)
        like = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div/div[1]/svg')
        time.sleep(2)
        like.click()
        # SCROLL_PAUSE_TIME = 0.5
        #
        # # Get scroll height
        # last_height = bot.execute_script("return document.body.scrollHeight")
        #
        # while True:
        #     # Scroll down to bottom
        #     bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #     # Wait to load page
        #     time.sleep(SCROLL_PAUSE_TIME)
        #
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = bot.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

    def like_retweet(self, hashtag):


        """
        This function automatically retrieves
        the tweets and then likes and retweets them

        Arguments:
            hashtag {string} -- twitter hashtag
        """

        bot = self.bot


        # fetches the latest tweets with the provided hashtag
        bot.get('https://twitter.com / search?q =% 23' + \
hashtag + '&src = typed_query&f = live'
        )

        time.sleep(3)

        # using set so that only unique links
        # are present and to avoid unnecessary repetition
        links = set()

        # obtaining the links of the tweets
        for _ in range(100):
            # executing javascript code
            # to scroll the webpage
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)'
            )

            time.sleep(4)

            # using list comprehension
            # for adding all the tweets link to the set
            # this particular piece of code might
            # look very complicated but the only reason
            # I opted for list comprehension because is
            # lot faster than traditional loops
            [
                links.add(elem.get_attribute('href')) \
                for elem in bot.find_elements_by_xpath("//a[@dir ='auto']")
            ]

        # traversing through the generated links
        for link in links:
            # opens individual links
            bot.get(link)
            time.sleep(4)

            try:
                # retweet button selector
                bot.find_element_by_css_selector(
                    '.css-18t94o4[data-testid ="retweet"]'
                ).click()
                # initializes action chain
                actions = ActionChains(bot)
                # sends RETURN key to retweet without comment
                actions.send_keys(Keys.RETURN).perform()

                # like button selector
                bot.find_element_by_css_selector(
                    '.css-18t94o4[data-testid ="like"]'
                ).click()
                # adding higher sleep time to avoid
                # getting detected as bot by twitter
                time.sleep(10)
            except:
                time.sleep(2)

        # fetches the main homepage
        bot.get('https://twitter.com/')

manjha = TwitterBot('Man_jha28','noki@C300')
manjha.like_retweet('politics')
# manjha.tweet('Twitter Bot Going Live, This is the first tweet by tweebot')