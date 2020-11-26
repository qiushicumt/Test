#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_day03_homework.py
@time:2020/11/24
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 5、
# 按照以下格式，打印出首页导航菜单
# 首页|自定义页面test|商品分类|ShopXO
# 考察点：css
def nav_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("http://localhost:8088/shopxo/index.php")
    list1 = driver.find_elements_by_css_selector("#doc-topbar-collapse .am-nav>li>a")
    list2 = []
    for one in list1:
        list2.append(one.text)
    print('|'.join(list2))
    input("Press any key to continue...")
    driver.quit()

# 6.QQ音乐新歌榜，https://y.qq.com/n/yqq/toplist/27.html#stat=y_new.toplist.menu.27
# 找出排名上升的歌曲和歌唱家并打印出来。
# 锁在轮回,任然
# 青丝,唐伯虎Annie
# .......
# 考察点：get_attribute,css

def get_QQMusic():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://y.qq.com/n/yqq/toplist/27.html#stat=y_new.toplist.menu.27")
    if len(driver.find_elements_by_class_name("popup__hd"))>0:        # 查找弹出的安装QQ音乐客户端的弹窗
        driver.find_element_by_class_name("popup__close").click()       # 关闭弹出的安装QQ音乐客户端的弹窗
    list1 = driver.find_elements_by_css_selector(".songlist__list>li>div")
    for one in list1:
        if one.find_element_by_css_selector(".songlist__rank i").get_attribute("class") == "icon_rank_up":  #   判断是否有class为icon_rank_up的i标签
            song_name = one.find_element_by_css_selector(".js_song").get_attribute("title")
            singer_name = one.find_element_by_css_selector(".songlist__artist").get_attribute("title")
            print(f"歌曲：{song_name}，歌手：{singer_name}")
    input("Press any key to continue...")
    driver.quit()

# 7.访问 51job ，http://www.51job.com
# 输入搜索关键词 "软件测试"， 地区选择 "南京"（注意，如果所在地已经选中其他地区，要去掉），
# 搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
#
# 软件测试工程师|10-23发布|4.5-6千/月|南京-雨花台区 | 在校生/应届生 | 大专 | 招2人|南京柯普瑞信息技术有限公司|民营公司 | 少于50人|计算机软件
# 软件测试-电网调度自动化、变电站保护及自动化、直流输电及柔性交流输电|10-23发布||南京 | 硕士 | 招若干人|南瑞研究院|国企|电气/电力/水利
# 软件测试工程师（南京）|10-23发布||南京 | 硕士 | 招4人|南京芯驰半导体科技有限公司|民营公司|电子技术/半导体/集成电路
# 考察点：css

def get_51job_1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get("https://www.51job.com/")
    # 查找输入框，输入搜索文字
    driver.find_element_by_css_selector("#kwdselectid").send_keys("软件测试")

    # 点击地区按钮，选择上海地区
    driver.find_element_by_css_selector("#work_position_input").click()
    spans = driver.find_elements_by_css_selector("#work_position_click_multiple_selected>span")  # 将选择的地区先全部清除掉
    for span in spans:
        span.click()
    driver.find_element_by_css_selector(
        "#work_position_click_center_right_list_category_000000_020000").click()  # 找到上海地区的标签，然后点击选中
    driver.find_element_by_css_selector("#work_position_click_bottom_save").click()  # 点击确定，保存选中的地区

    # 点击搜索按钮进行职位搜索
    driver.find_element_by_css_selector(".ush.top_wrap button").click()

    # 分析搜索结果
    divs = driver.find_elements_by_css_selector(".j_joblist>div")  # 获取职位结果列表
    for div in divs:
        result_list = []
        eles = div.find_elements_by_css_selector(".t span, .info span, .er a, .er p")  # 通过组选择器，获取想要打印的文字所在的元素
        for ele in eles:
            result_list.append(ele.text)  # 遍历获取每一个元素的text
        print('|'.join(result_list))

    input('...')
    driver.quit()


# 8.51job-2
# 登录 http://www.51job.com
#     点击高级搜索
#     输入搜索关键词 软件测试
#     地区选择 南京
#     职能类别 选 测试 -> 软件测试工程师
#     工作年限选 1-3 年
# 搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
# 软件测试工程师|10-23发布|4.5-6千/月|南京-雨花台区 | 在校生/应届生 | 大专 | 招2人|南京柯普瑞信息技术有限公司|民营公司 | 少于50人|计算机软件
# 软件测试-电网调度自动化、变电站保护及自动化、直流输电及柔性交流输电|10-23发布||南京 | 硕士 | 招若干人|南瑞研究院|国企|电气/电力/水利
# 软件测试工程师（南京）|10-23发布||南京 | 硕士 | 招4人|南京芯驰半导体科技有限公司|民营公司|电子技术/半导体/集成电路
# 考察点：css

def get_51job_2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.51job.com")

    # 进入高级搜索
    driver.find_element_by_css_selector(".ush.top_wrap>a").click()

    # 查找输入框，输入搜索文字
    driver.find_element_by_css_selector("#kwdselectid").send_keys("软件测试")

    # 点击地区按钮，选择上海地区
    driver.find_element_by_css_selector("#work_position_input").click()
    spans = driver.find_elements_by_css_selector(
        "#work_position_click_multiple_selected>span")  # 获取多选的工作地区的div的第一个span元素，形成列表
    for one in spans:
        one.click()  # 清除所有已经被选择的地区
    driver.implicitly_wait(1)
    driver.find_element_by_css_selector(
        "#work_position_click_center_right_list_category_000000_020000").click()  # 选中上海地区
    driver.find_element_by_css_selector("#work_position_click_bottom_save").click()

    # 点击空白区域使搜索框的下拉菜单关闭掉
    driver.find_element_by_css_selector(".tit").click()

    # 点职能列表，选择测试->软件测试工程师
    # 点击职能按钮
    driver.find_element_by_css_selector("#funtype_click").click()
    driver.find_element_by_css_selector("#funtype_click_center_right_list_category_0100_2700").click()  # 点击测试按钮
    driver.find_element_by_css_selector(
        "#funtype_click_center_right_list_sub_category_each_0100_2707").click()  # 点击软件测试工程师按钮
    driver.find_element_by_css_selector("#funtype_click_bottom_save").click()  # 点击确定按钮，保存选择

    # 选择工作年限
    driver.find_element_by_css_selector("#workyear_list>span").click()
    driver.find_element_by_css_selector("#workyear_list div.ul span[title='1-3年']").click()

    # 点击搜索按钮进行职位搜索
    driver.find_element_by_css_selector(".p_sou span").click()

    # 分析搜索结果
    divs = driver.find_elements_by_css_selector(".j_joblist>div")  # 获取所有搜索结果的div生成列表
    for div in divs:  # 对div列表进行遍历
        result_list = []
        eles = div.find_elements_by_css_selector(".t span, .info span, .er a, .er p")
        for ele in eles:
            result_list.append(ele.text)
        print('|'.join(result_list))

    input("Press any key to continue...")
    driver.quit()

# 11.打开网易云音乐首页（https://music.163.com/），进入到排行榜，按照如下格式打印出当前100首歌曲的信息
# 1|经济舱(Live)|03:43|Kafe.Hu
# 2|顽家|02:55|Jony J
# 考察点：frame
def get_163Music():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://music.163.com/")

    # 打开排行榜页面
    driver.find_element_by_css_selector("#g_nav2 li:nth-child(2) a").click()

    # 榜单列表是另外的一个frame，切换进入另外一个frame
    driver.switch_to.frame("g_iframe")

    # 获取歌曲榜单列表
    song_list = driver.find_elements_by_css_selector(".m-table-rank tbody tr")  # 将一百首歌曲生成一个列表

    # 分析数据
    # 遍历歌曲列表
    for one in song_list:
        result_list = []
        eles = one.find_elements_by_css_selector(".hd>span, .ttc b, .u-dur , .text")  # 获取被打印的内容的元素，生成一个列表
        for ele in eles:
            if ele.get_attribute("title"):  # 元素具有title属性，则返回title属性的字符串，不具有title属性，则返回空行
                result_list.append(ele.get_attribute("title"))
            else:
                result_list.append(ele.text)  # 不具有title属性的元素获取其text值
        print('|'.join(result_list))

    input("Press any key to continue...")
    driver.quit()

if __name__ == '__main__':
    # nav_selector()
    # get_QQMusic()
    get_51job_1()
    # get_51job_2()
    # get_163Music()

