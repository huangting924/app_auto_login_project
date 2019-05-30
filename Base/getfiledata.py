import os
import yaml


class GetFileData:

    def __init__(self):
        pass

    def get_yaml_data(self, name):
        """返回 yaml 文件数据"""
        with open(os.getcwd() + os.sep + "data" + os.sep + name, "r") as f:
            return yaml.safe_load(f)
