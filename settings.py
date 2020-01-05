import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
"""THIS FILE CONTAINS ALL SETTINGS AND CLASSES.
THERE IS AN ABSTRACT PARSING CLASS, BASED ON WHICH YOU CAN CREATE PARSING CLASSES FOR VARIOUS SITE"""
class Base_parser:
    def get_text_from_url(self, url):
        pass
    def url_parse(self, driver_path):
        pass
class Settings:
    """This class contains all settings.
    You need add vk settings there"""
    login = ""
    password = ""
    driver_path = ""
    http_vk = "https://api.vk.com/method/"
    api_key = ""
    group_id = ""
    group_name = ""

class Droideru_class(Base_parser):
    """THIS IS PARSING CLASS FOR DROIDER.RU SITE"""
    def get_text_from_url(self, url):
        """This function parses text from DROIDER.RU
        If you need to use another site you must create new class based on Base_parser class and add get_text_from_url function"""
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        spans = soup.select('p')
        output = " ".join([i.text for i in spans]).split(".")
        # Crop copyright
        print(" ".join(output[:-2]))
        return " ".join(output[:-2])
    def url_parse(self, driver_path, s=1, x=1, url = "http://droider.ru", a=open("urls.txt", "a")):
        """This function adds required quantity urls from given site to urls.txt file
            If you want to transform module to another site
            You must change this function"""
        s = int(input("Введите нужное кол-во статей:"))
        if s < 1 or s != int(s):
            print("Please input number more or equal 1")
            self.url_parse(driver_path=Settings.driver_path)
        while x <= s:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1920x935')
            browser = webdriver.Chrome(f"{driver_path}", chrome_options=options)
            browser.get(f"{url}")
            time.sleep(2)
            url1 = browser.find_element_by_xpath(f"/html/body/div/div[5]/div/div/div/div/a[{x}]")
            url1.click()
            print(browser.current_url)
            a.write(browser.current_url + " ")
            x += 1
        a.close()
Droider_ru = Droideru_class()





