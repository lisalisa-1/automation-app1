# 数据解析工具
import yaml
import pandas as pd


class DataUtils:
    """数据解析工具"""
    
    @staticmethod
    def load_yaml(file_path):
        """加载YAML文件"""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data
    
    @staticmethod
    def load_excel(file_path, sheet_name=None):
        """加载Excel文件"""
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path)
        
        # 转换为字典列表
        data = df.to_dict('records')
        return data
    
    @staticmethod
    def get_test_data(data, test_case):
        """根据测试用例名称获取测试数据"""
        for item in data:
            if item.get('test_case') == test_case:
                return item
        return None