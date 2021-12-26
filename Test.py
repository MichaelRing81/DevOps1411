from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

my_driver = webdriver.Chrome(executable_path="c:/Users/Michael/Desktop/chromedriver/chromedriver.exe")
my_driver.get("https://translate.google.com/")

a = driver.find_element_by_id("gt-submit")
b = driver.find_element_by_class_name("jfk-button")
c = driver.find_element_by_xpath("//input[@type=‘submit']")
print(a)
