import configparser
import  os

class ReadConfig:
    """
    读取配置信息
    """
    def __init__(self):
        """
        读取配置文件
        """
        self.config=configparser.ConfigParser()
        project_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config.read(project_dir+'/config/config.ini',encoding='utf-8')
    def get_config(self,key):
        """
        读取配置项,section默认default
        :param key: 配置项的键
        :return: 返回配置信息
        """

        return self.config.get('default',key)
# print(ReadConfig().get_config('url'))