# 1

from selenium import webdriver
my_driver = webdriver.Chrome(executable_path="c:/Users/Michael/Desktop/chromedriver/chromedriver.exe")
my_driver.get("http://www.walla.co.il")

from selenium import webdriver
my_driver = webdriver.Firefox(executable_path="c:/Users/Michael/Desktop/geckodriver/geckodriver.exe")
my_driver.get("http://www.ynet.co.il")


# 2

title = my_driver.title
my_driver.refresh()
if title == my_driver.title:
    print("the title is the same")
else:
    print("the title is different")


# 3

# Yes, the elements have same locators in any browser used, as they are the output of the web page code


# 4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

my_driver = webdriver.Chrome(executable_path="c:/Users/Michael/Desktop/chromedriver/chromedriver.exe")
my_driver.get("https://translate.google.com/")
my_driver.find_element_by_id("source").send_keys("test")
my_driver.find_element_by_id("gt-submit").click()


# 5

my_driver.get("https://www.youtube.com/")
my_driver.find_element_by_id("search").send_keys("guns and roses")
my_driver.find_element_by_id("search-icon-legacy").click()


# 6

a = driver.find_element_by_id("gt-submit")
b = driver.find_element_by_class_name("jfk-button")
c = driver.find_element_by_xpath("//input[@type=‘submit']")
print(a)
