# 数据解析工具
import pytest
import yaml
import pandas as pd
import json


class DataUtils:
    """数据解析工具"""
    #
    # @staticmethod
    # def load_yaml(file_path):
    #     """加载YAML文件"""
    #     with open(file_path, 'r', encoding='utf-8') as f:
    #         data = yaml.safe_load(f)
    #     return data

    # common/data_reader.py（改造读取方法）
    import yaml

    @staticmethod
    def load_yaml(file_path):
        """读取YAML并转成{case_name: 数据}的字典（精准匹配核心）"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = yaml.safe_load(f)
                print("11",raw_data)

            # 转成{case_name: 数据}的结构（兼容分组/非分组YAML）
            case_dict = {}
            for key, value in raw_data.items():
                # 如果是分组（value是字典且包含case_name）
                if isinstance(value, dict) and "case_name" in value:
                    case_name = value["case_name"]
                    case_dict[case_name] = value
                # 如果是原始列表（兼容旧格式）
                elif isinstance(raw_data, list):
                    for item in raw_data:
                        case_name = item["case_name"]
                        case_dict[case_name] = item

            # 校验case_name唯一性（企业级必做）
            if len(case_dict) != len(raw_data):
                raise Exception("YAML中存在重复的case_name！")

            return case_dict
        except Exception as e:
            raise Exception(f"读取YAML失败：{e}")
    
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

    @staticmethod
    def read_json(file_path):
        """读取JSON文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"读取JSON失败：{e}")

    @staticmethod
    def read_yaml(file_path):
        """读取YAML数据（通用方法）"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            raise Exception(f"读取YAML失败：{e}")

    @staticmethod
    def get_pytest_params(case_data_dict):
        """
        通用方法：将单条/多条数据转为pytest.param列表
        :param case_data_dict: YAML中读取的单条/多条数据字典（如login_success_single/login_failed_multi）
        :return: pytest.param列表（单条返回长度1，多条返回对应长度）
        """
        param_list = []

        # 遍历caseN（case1/case2/case3），自动适配单条/多条
        for case_key, case_data in case_data_dict.items():
            # 校验必要字段（企业级必做）
            required_fields = ["case_name", "mark"]
            for field in required_fields:
                if field not in case_data:
                    raise Exception(f"数据{case_key}缺少必要字段：{field}")

            # 生成pytest.param对象
            param = pytest.param(
                case_data,  # 核心数据（字典）
                id=case_data["case_name"],  # 自定义用例ID（报告显示）
                marks=pytest.mark.__getattr__(case_data["mark"])  # 传递测试标记
            )
            param_list.append(param)

        # 校验：至少有一条数据
        if not param_list:
            raise Exception("未找到任何测试数据！")

        return param_list