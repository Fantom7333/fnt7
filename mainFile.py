from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import json
import functions as fp
import settings as s
fp.parse(s.Droider_ru.url_parse)
fp.textfile(s.Droider_ru.get_text_from_url)
