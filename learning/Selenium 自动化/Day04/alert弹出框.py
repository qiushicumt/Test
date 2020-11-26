from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get(r'file:///D:\BaiduNetdiskDownload\selenium-update\selenium API\12-alert弹出框处理\alert弹出框.html')
# ----------------------------------
# driver.find_element_by_id('b1').click()
# time.sleep(3)
# driver.switch_to.alert.accept()
# driver.find_element_by_id('other').click()
# ----------------------------------
# driver.find_element_by_id('b1').click()
# alert = driver.switch_to.alert
# print(alert.text)
# # ----------------------------------
# driver.find_element_by_id("b2").click()
# time.sleep(3)
# driver.switch_to.alert.dismiss()
# # ----------------------------------

# driver.find_element_by_id('b3').click()
# alert = driver.switch_to.alert
# time.sleep(2)
# alert.send_keys('哈哈哈')
# time.sleep(2)
# alert.accept()
# driver.find_element_by_id('other').click()



# -------------------------------------
input("press any key to continue...")
driver.quit()   # 浏览器退出