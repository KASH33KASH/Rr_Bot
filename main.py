import threading
import Bot
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

def init_webdriver():
    user_agent = UserAgent().chrome
    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--headless")

    return Bot.Bot(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options))

def main():
    controller()

def work():
    bot = init_webdriver()

    bot.login("mail", "login") #Bot login and mail
    bot.select_factory()
    bot.select_energy()

    while True:
        bot.work()

def train_perk():
    bot = init_webdriver()

    bot.login("mail", "login") #Bot login and mail
    while True:
        bot.training()
    
def war_train():
    bot = init_webdriver()
    
    bot.login("mail", "login") #Bot login and mail
    while True:
        bot.war_training()

def controller():
    threading.Thread(target=work, args=()).start()
    time.sleep(30)
    threading.Thread(target=train_perk, args=()).start()
    time.sleep(30)
    threading.Thread(target=war_train, args=()).start()


if __name__ == "__main__":
    main()
