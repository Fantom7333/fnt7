from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import json
from settings import Settings

def parse(func, driver_path = Settings.driver_path):
    """This function is decorator for parse2 function"""
    with open("urls.txt",'w') as w:
            func(driver_path)
    print("Завершено")

def textfile(func, driver_path = Settings.driver_path, group_name = Settings.group_name, group_id = Settings.group_id, api_key = Settings.api_key, http_vk = Settings.http_vk,login = Settings.login, password = Settings.password):
    """This function keep the numbering in the files name"""
    group_pub = 0
    #Get list of urls
    with open("urls.txt", "r") as f:
        urls = f.read().split()
    #Test existance of "title.txt" file
    try:
        with open("title.txt", 'r', encoding='utf-8') as f:
            t = f.read()
    #If "title.txt" not exists
    except FileNotFoundError:
            with open("title.txt", 'w', encoding='utf-8') as f:
                x = "0"
                f.write(x)
    finally:
        for i in urls:
        #This 3 open-constructions is necessary to keep numbering in the file name
            with open("title.txt", 'r', encoding='utf-8') as f:
                x = f.read()
                x = int(x)
                x += 1
                x = str(x)
            with open(f"tech{x}.txt", 'w', encoding='utf-8') as f:
                f.write(func(i))
                a = f"tech{x}.txt"
            with open("title.txt", 'w', encoding='utf-8') as f:
                f.write(x)
                files = {"file": open(a,'r')}
            #This open-construction upload text info from url in VK as post
            with open(a, 'r') as f:
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                options.add_argument('window-size=1920x935')
                driver = webdriver.Chrome(f"{driver_path}", options = options)
                driver.get("https://vk.com")
                login_box = driver.find_element_by_xpath(
                    "/html/body/div[9]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/form/input[7]")
                password_box = driver.find_element_by_xpath(
                    "/html/body/div[9]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/form/input[8]")
                login_box.send_keys(f"{login}")
                password_box.send_keys(f"{password}")
                button_login = driver.find_element_by_xpath(
                    "/html/body/div[9]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/form/button")
                button_login.click()
                driver.implicitly_wait(5)
                community = driver.find_element_by_xpath(
                    "/html/body/div[11]/div/div/div[2]/div[1]/div/nav/ol/li[5]/a/span/span[3]")
                community.click()
                admine1 = driver.find_element_by_xpath(
                    "/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/h2/ul/li[2]/a")
                admine1.click()
                #Search line
                search_box = driver.find_element_by_xpath("/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div/input")
                #Search group
                search_box.send_keys(f"{group_name}")
                time.sleep(10)
                search = driver.find_element_by_xpath(
                    "/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/button")
                driver.implicitly_wait(10)
                search.click()
                time.sleep(5)
                tech_news = driver.find_element_by_xpath(
                    "/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[1]/a")
                driver.implicitly_wait(10)
                tech_news.click()
                write_box = driver.find_element_by_xpath(
                    "/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div")
                write_box.click()
                write_box1 = driver.find_element_by_id("post_field")
                time.sleep(5)
                try:
                    write_box1.send_keys("\n".join(f.readlines()))
                except:
                    continue
                settings = driver.find_element_by_xpath(
                    "/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[6]/div[2]")
                actions = ActionChains(driver)
                time.sleep(5)
                if group_pub != 1:
                    actions.move_to_element(settings).perform()
                    time.sleep(5)
                    from_community = driver.find_element_by_xpath(
                        "/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[6]/div[2]/div/div[2]/div[1]")
                    from_community.click()
                #This block of code upload text file as document in VK group
                publish = driver.find_element_by_xpath(
                    "/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[6]/div[1]/button")
                publish.click()
                vk_adress = requests.get(
                    f"{http_vk}/docs.getWallUploadServer?group_id={group_id}&fields=bdate&access_token={api_key}&v=5.103")
                content = vk_adress.text
                upload_url = json.loads(content)["response"]["upload_url"]
                vk_file = \
                json.loads(requests.post(f"{upload_url}", files=files, params={"format": "multipart/form-data"}).text)[
                    "file"]
                print(vk_file)
                finish = requests.get(
                    f"{http_vk}docs.save?group_id={group_id}&file={vk_file}&fields=bdate&access_token={api_key}&v=5.103")
                print(finish.text)
                group_pub = 1
                time.sleep(5)
        driver.quit()




