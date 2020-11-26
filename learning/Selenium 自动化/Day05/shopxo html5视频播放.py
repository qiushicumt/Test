from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost/shopxo/")
#进入到1楼第一个商品
driver.find_element_by_css_selector("#floor1 .goods-list a").click()

# print(driver.window_handles)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if 'MARNI Trunk' in driver.title:
        break

#滑动到可见（非必填代码，看效果）
js="window.scrollTo(0,800)"
driver.execute_script(js)

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[src*='youku']"))

# from selenium.webdriver.common.action_chains import ActionChains
# ac=ActionChains(driver)
# #鼠标移动到播放控制条
# ac.move_to_element(driver.find_element_by_css_selector(".h5player-dashboard"))

#way1，通过正常元素定位，播放暂停
# print("正常元素定位播放暂停")
# driver.find_element_by_css_selector(".control-play-icon").click()
# print("播放10秒...")
# time.sleep(10)
# driver.find_element_by_css_selector(".control-play-icon").click()
# print("暂停5秒")
# time.sleep(5)
# driver.find_element_by_css_selector(".control-play-icon").click()
# print("继续播放...")
# time.sleep(10)
# ###########################################################################################################
#way2，通过js播放暂停
#浏览器为了提高用户体验，减少数据消耗，chrome浏览器在18年4月起，就在桌面浏览器全面禁止了音视频的自动播放功能，无用户交互的情况下js调用play也被禁用
#chrome没有点击或者滑动等交互行为，不给自动播放视频
driver.find_element_by_css_selector(".control-play-icon").click()
print("先点击，产生交互，再播放5秒")
time.sleep(5)
#
# print("js控制播放暂停")
video=driver.find_element_by_css_selector("#youku-playerBox .youku-film-player>video")#找到html5 video标签
#暂停视频
driver.execute_script("arguments[0].pause()",video)
print("暂停5秒")
time.sleep(5)
#播放视频
driver.execute_script("arguments[0].play()",video)
print("播放10秒...")
time.sleep(10)
#暂停视频
driver.execute_script("arguments[0].pause()",video)
print("暂停播放")
#############################################################################################################
input("press any key to continue...")
driver.quit()
