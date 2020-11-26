from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
##########################################################################################

#案例1
driver=webdriver.Chrome()
driver.get("https://www.helloweba.net/demo/2017/unlock/")
#滑块
slider=driver.find_elements_by_class_name("slide-to-unlock-handle")[0]
#滑动框
ele=driver.find_element_by_class_name("slide-to-unlock-bg")
print(ele.location,ele.size)

# 方法一：一点一点滑过去
# ac=ActionChains(driver)
# ac.click_and_hold(slider).perform()
#
# while True:
#     try:
#         ac.move_by_offset(10,0).perform()
#         # ac.reset_actions()#error:会释放click_and_hold,滑块释放
#         #ActionChains会把你的每次操作都会被保存到action._actions这个列表里面,也就是说在while循环中每移动一次，
#         # 这个操作就会被保存到这个列表里面，下面再移动的时候之前操作的操作还会被执行
#         ac=ActionChains(driver)  #解决重复位移问题
#
#     except:#滑到底会有alert弹窗，此时再滑动会报错
#         print("已滑到底...")
#         break

#方法二：一下就滑过去
#way1
# ac=ActionChains(driver)
# ac.drag_and_drop_by_offset(slider,298,0).perform()

#way2
# ac=ActionChains(driver)
# ac.click_and_hold(slider).move_by_offset(298,0).perform()

#way3
ac=ActionChains(driver)
ac.click_and_hold(slider).move_to_element_with_offset(slider,298,38).perform()


input("press any key to continue...")
driver.quit()
