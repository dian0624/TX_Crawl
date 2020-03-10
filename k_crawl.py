from selenium import webdriver
from time import sleep 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pymongo
import re 

conn = pymongo.MongoClient("localhost", 27017)
db = conn.Txdb
myset = db.txinfo

#無頭模式
chrome_options = Options() 
chrome_options.add_argument('--headless')  
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.taifex.com.tw/cht/3/futDailyMarketReport")


sleep(1)
#查詢資料
driver.find_element_by_name("queryDate").clear()
dateElement = driver.find_element_by_name("queryDate")
dateElement.send_keys(r"2019/12/30")
submit = driver.find_element_by_name('button')
submit.click()
sleep(2)

timeElement = Select(driver.find_element_by_name("MarketCode"))
timeElement.select_by_value("0")
sleep(2)

deedElement = Select(driver.find_element_by_name("commodity_idt"))
deedElement.select_by_value("TX")
sleep(1)

submit = driver.find_element_by_name('button')
submit.click()

for x in range(30):
	try:
		bases = driver.find_elements_by_xpath(
					'//*[@id="printhere"]/table/tbody/tr[2]/td')
		for base in bases:
			keys = base.find_element_by_xpath('./table[2]/tbody/tr[1]').text.split()
			keys[1] = ''.join(keys[1:4])
			del keys[2:4]
			keys[5] = ''.join(keys[5:7])
			del keys[6]
			keys.append('交易日期')
			for i in range(2,8):
				infos = base.find_element_by_xpath('./table[2]/tbody/tr[%s]'%(str(i)))
				info=infos.text.split()
				#當天日期
				date = base.find_element_by_xpath('./h3')
				now_date = re.findall(r"\d+[/]\d+[/]\d+",date.text)[0]
				info.append(now_date)
				dic = dict(zip(keys,info))
				myset.insert(dic)

				print("正在寫入數據庫")		

		last_day = driver.find_element_by_name('button3')
		last_day.click()
		sleep(2)
	except :
		print("當天無交易")
		last_day = driver.find_element_by_name('button3')
		last_day.click()
		sleep(2)	
sleep(2)
driver.quit()
