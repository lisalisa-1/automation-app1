import os
from loguru import logger
import yaml
import pytest
from tests.common.test_base import  BaseTest
from utils import DataUtils


class TestFullOrder(BaseTest):

    current_dir = os.path.dirname(__file__)
    order_data = DataUtils.read_yaml(os.path.join(os.path.dirname(os.path.dirname(current_dir)), "test_data/scenario/test_full_order.yaml"))

    @pytest.mark.parametrize("case",DataUtils.get_pytest_params(order_data["test_order_flow"]))
    def test_order_flow(self,page_factory,case):
        home_page = page_factory.get_page("home_page")
        logger.info("开始测试订单流程")
        home_page.click_my_button()
        self.login("test_user", "123456",page_factory)


