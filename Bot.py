import random
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Bot():
    trup_use = 0 
    en_use = 0

    brovse = None


    def __init__(self, brovse):
        self.brovse = brovse 
        self.brovse.set_window_size(1920, 1080) 

    def login(self, email, password):
        try:
            time.sleep(3)
            self.brovse.get("https://rivalregions.com/")
            time.sleep(5)

            input_email = self.brovse.find_element(By.NAME, "mail") 
            input_email.clear() 
            input_email.send_keys(email)
            time.sleep(2)

            input_password = self.brovse.find_element(By.NAME, "p")
            input_password.clear() 
            input_password.send_keys(password)
            time.sleep(3)
            input_password.send_keys(Keys.ENTER)
            
            print("Sucsefull login")
            time.sleep(2)
        except:
            return
        
    def select_factory(self):
        try:
            self.get_menu_button("https://rivalregions.com/#work") 

            find_factory = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[5]/div[2]") 
            time.sleep(1)
            find_factory.click() 
            time.sleep(3)

            factory_list = self.brovse.find_element(By.ID, "list_tbody") 
            time.sleep(1)
            factorys = factory_list.find_elements(By.TAG_NAME, "tr")
            
            for factory in factorys: 
                time.sleep(1)
                salary = int(factory.text.split("%")[0].split(" ")[-1]) 
                if salary == 100: 
                    factory.find_elements(By.TAG_NAME, "td")[-1].click()
                    break
            time.sleep(2)
            print("Sucsefull selected factory")
        except:
            return
        
    def work(self):
        try:
            time.sleep(5)

            if self.en_use == 10: 
               self.buy_energy()

            work_on_factory = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[6]/div[2]/div[2]/div[3]/div[1]") 
            time.sleep(1)
            work_on_factory.click() 
            time.sleep(1.5)

            pyautogui.press('enter')
            time.sleep(4)

            close_work_panel = self.brovse.find_element(By.XPATH, "/html/body/div[3]/div/div[1]") 
            time.sleep(1)
            close_work_panel.click() 

            self.en_use += 1 
            print("Worked")

            self.check_energy_hub()

            time.sleep(600)
            return 
        except:
            time.sleep(600)
            return 

    def check_energy_hub(self):
        energy_hub = "/html/body/div[5]/div[1]/div[1]/div[5]"
        if self.xpath_exith(energy_hub):
            energy = self.brovse.find_element(By.XPATH, energy_hub)
            try:
                energy.click()
            except:
                if "block" in energy.get_attribute("style"):
                    energy.click()
                    time.sleep(1)
                    self.work()
    
    def buy_energy(self):
        try:
            self.en_use = 0 

            self.get_menu_button("https://rivalregions.com/#storage") 

            buy_enegry = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[11]/div[3]") 
            time.sleep(1)
            buy_enegry.click() 
            time.sleep(3)

            input_energy_value = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[3]/input") 
            input_energy_value.clear() 
            input_energy_value.send_keys(2000) 
            time.sleep(2)

            produce = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[4]/div") 
            time.sleep(1)
            produce.click() 
            time.sleep(2)
            return
        except:
            time.sleep(3600)
            return

    def select_energy(self):
        try:
            sel_ener = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[6]/div[2]/div[2]/div[2]/div[2]/div/div/div") 
            time.sleep(1)
            sel_ener.click() 
            time.sleep(3)

            energy_list = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul") 
            time.sleep(1)

            full_energy = energy_list.find_elements(By.TAG_NAME, "li")[-1] 
            time.sleep(1)
            full_energy.click() 

            print("Sucsefull selected energy")
            time.sleep(2)
            return
        except:
            time.sleep(3600)
            return 
        
    def xpath_exith(self, xpath):
        try:
            self.brovse.find_element(By.XPATH, xpath) 
            exist = True
        except: 
            exist = False 
        return exist
    
    def get_menu_button(self, url):
        time.sleep(3)
        self.brovse.get(url.replace("#", "")) 
        time.sleep(5) 
        self.brovse.get(url) 
        time.sleep(3)

    def war_training(self):
        try:
            if self.trup_use == 10: 
                self.buy_army()
            
            self.get_menu_button("https://rivalregions.com/#war") 
            time.sleep(5)
    
            war_train_button = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[4]/div[2]/div") 
            time.sleep(1)
            war_train_button.click() 
            time.sleep(3)
 
            beat = self.brovse.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div[2]/div[4]/div[1]") 
            time.sleep(1)
            beat.click() 
            time.sleep(2)

            close_war_train_panel = self.brovse.find_element(By.XPATH, "/html/body/div[3]/div/div[1]") 
            time.sleep(1)
            close_war_train_panel.click() 
            time.sleep(2)

            self.trup_use += 1 

            time.sleep(3600)

            return 
        except:
            print("error")
            time.sleep(3600)
            return 
        
    def buy_army(self):
        try:
            self.trup_use = 0 

            self.get_menu_button("https://rivalregions.com/#storage")

            buy_plane_button = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[15]") 
            time.sleep(1)
            buy_plane_button.click()
            time.sleep(1)

            input_buy_plane_value = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[5]/input") 
            input_buy_plane_value.clear()  
            input_buy_plane_value.send_keys(20000) 
            time.sleep(2)

            buy_plane = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[6]/div[1]") 
            time.sleep(1)
            buy_plane.click() 
            time.sleep(2)

            return
        except:
            time.sleep(600)
            return

    def training(self):
        try:
            self.get_menu_button("https://rivalregions.com/#overview") 

            ran_perk = random.randint(1, 3) 

            if ran_perk == 1: 
                second = self.click_train_button("/html/body/div[6]/div[1]/div[9]/div[2]/div[4]") 
            elif ran_perk == 2: 
                second = self.click_train_button("/html/body/div[6]/div[1]/div[9]/div[2]/div[5]") 
            elif ran_perk == 3: 
                second = self.click_train_button("/html/body/div[6]/div[1]/div[9]/div[2]/div[6]") 
            
            time.sleep(second)
            return 
        except:
            time.sleep(3600)
            return 
        
    def click_train_button(self, perk_xpath):
        try:
            perk = self.brovse.find_element(By.XPATH, perk_xpath)
            time.sleep(0.3)
            perk.click()
            time.sleep(3)

            train = self.brovse.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div[1]")
            time.sleep(0.3)
            trainning_time = train.find_element(By.CLASS_NAME, "perk_4").text.split(",")[-1]
            
            hour_min_second = trainning_time.split(":")
            second = 0
            if len(hour_min_second) == 3:
                second += hour_min_second[0] * 3600
                second += hour_min_second[1] * 60
                second += hour_min_second[2]
            else:
                second += hour_min_second[0] * 60
                second += hour_min_second[1]
            
            time.sleep(1)
            train.click()
        

            return second
        except Exception as ex:
            return 3600
            return 