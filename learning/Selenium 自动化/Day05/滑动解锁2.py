from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

######################################################################################################
#案例2
driver=webdriver.Chrome()
driver.get(r"file:///D:\BaiduNetdiskDownload\selenium-update\selenium API\19-滑动解锁（ActionChains）\滑动解锁.html")
#定位到滑块
slider=driver.find_element_by_class_name("inner")
#整个滑块
span=driver.find_element_by_tag_name("span")
print(span.location,span.size)
########################################################################################################################
#方法一：一点一点滑动
# ac=ActionChains(driver)
# ac.click_and_hold(slider).perform()
#
# for i in range(20):
#     try:
#         ac.move_by_offset(10,0).perform()
#         # ac.reset_actions()#error:会释放click_and_hold,滑块释放
#         #ActionChains会把你的每次操作都会被保存到action._actions这个列表里面,也就是说在while循环中每移动一次，
#         # 这个操作就会被保存到这个列表里面，下面再移动的时候之前操作的操作还会被执行
#         ac=ActionChains(driver)  #解决重复位移问题
#         print(i)
#     except:
#         print("已滑到底...")
#         break
# ac.release().perform()#释放鼠标


########################################################################################################################
#方法二：一下滑动
ac=ActionChains(driver)
ac.drag_and_drop_by_offset(slider,198,0).perform()  #会自动释放鼠标


input("press any key to continue...")
driver.quit()
