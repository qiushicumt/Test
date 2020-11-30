from HTMLTestRunner import HTMLTestRunner
import unittest
import os
import time

# os.path.abspath(__file__)   #返回当前文件的绝对路径
# os.path.dirname(os.path.abspath(__file__))  #返回当前文件的目录
# print(os.path.dirname(os.path.abspath(__file__)))
###########################################################################################
# print(os.getcwd()) #返回的是当前工作目录
# !!!当前工作路径 working directory 就是脚本运行/调用/执行的地方，而不是脚本本身的地方。


#获取项目根目录
start_dir=os.path.dirname(os.path.abspath(__file__))
testsuite=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern='test*.py')
now=time.strftime("%Y-%m-%d %H_%M_%S")
fp=open("./report/result_"+now+".html",'wb')
# stream 指定生成HTML测试报告的文件
# verbosity 日志的级别，默认为1
# title 用例的标题，默认为None
# description 用例的描述，默认为None
runner=HTMLTestRunner(stream=fp,title="shopxo test report",description='None',verbosity=2)
runner.run(testsuite)
fp.close()