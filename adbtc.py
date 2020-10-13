from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')
driver = webdriver.Chrome(options=chrome_options)

#driver = webdriver.Chrome()
email='your_email'
senha='your_password'

driver.get("https://adbtc.top/index/enter/")
time.sleep(40) #60s for you solve hCaptcha
driver.find_element_by_id('logpochta').send_keys(email)
driver.find_element_by_id('logpa5sword').send_keys(senha)
driver.find_element_by_css_selector('.btn.light-blue.darken-4').click()
time.sleep(10)
driver.get("https://adbtc.top/index/earn") #https://adbtc.top/surf/rotator
time.sleep(6)
driver.find_element_by_css_selector('.btn.btn-large.yellow.black-text').click()
time.sleep(5) #45s for you solve hCaptcha
driver.find_element_by_class_name('select-wrapper').click()
driver.find_element_by_xpath("//ul[@class='dropdown-content select-dropdown']/li[3]").click()
driver.find_element_by_css_selector('.input-field.col.s12.m9').click()
while True:
    try:
        driver.find_element_by_css_selector('.pulse.animated.valign-wrapper.btn').click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        str1=str(driver.title)
        print(str1)
        tempo=str1.split()
        tempo=int(tempo[0])+10
        #print(tempo)
        time.sleep(tempo)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        print("Please solve the captchar! Or something is wrong...")
        try:
            teste=driver.find_element_by_css_selector('.open.btn.green')
            print("sleeping")
            time.sleep(300)
            driver.get("https://adbtc.top/index/earn")  # https://adbtc.top/surf/rotator
            time.sleep(6)
            driver.find_element_by_css_selector('.btn.btn-large.yellow.black-text').click()
        except:
            print('wake up')

            #print('wait 30s to update page')
            #time.sleep(30)
            #driver.get("https://adbtc.top/surf/browse")
        time.sleep(10)
        #driver.get("https://adbtc.top/surf/browse")
    #driver.find_element_by_css_selector('.pulse.animated.valign-wrapper.btn').click()
