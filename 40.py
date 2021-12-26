from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome(executable_path="c:/Users/Michael/Desktop/chromedriver/chromedriver.exe")
#my_driver.get("https://github.com")
#sleep(3)
#my_driver.close()
my_driver.get("c:/Users/Michael/Desktop/chromedriver/index.html")
#my_driver.back()
#my_driver.refresh()
billamt = my_driver.find_element_by_id("billamt")
billamt.send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element_by_id("peopleamt").send_keys("4")
my_driver.find_element_by_id("calculate").click()
expected = "3.75"
actual = my_driver.find_element_by_id("tip").text

#if expected == actual:
#    print("tip is ok")
#else:
#    print("tip is not ok")

assert expected == actual
sleep(3)
my_driver.close()

