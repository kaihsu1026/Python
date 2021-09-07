from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install('./')  
"""
chromedriver_autoinstaller.install('選擇要安裝的路徑') 

# Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path

# 檢查當前版本的 chromedriver 是否存在
# 如果它不存在，則自動下載，
# 然後將 chromedriver 添加到路徑
"""

path = 'http://zabbix.rv88.tw/fw_vip_all.html'
driver = webdriver.Chrome()
driver.get(path)
time.sleep(10)
driver.find_element_by_xpath('//*[@id="table_id_filter"]/label/input').send_keys("Selenium")
time.sleep(10)


driver.close()

"""
# 模擬iphone x瀏覽
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'}) 
driver = webdriver.Chrome(options=options)

driver.get(path)
time.sleep(10)
driver.save_screenshot('B26.png')  #擷取當下頁面

"""







