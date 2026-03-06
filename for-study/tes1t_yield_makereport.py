

# 测试用例文件 test_demo.py
import pytest

@pytest.fixture
def setup_teardown():
    print("\n--- setup阶段：初始化driver ---")  # setup阶段
    yield
    print("\n--- teardown阶段：关闭driver ---")  # teardown阶段

def test_demo(driver,setup_teardown):
    print("\n--- call阶段：执行用例核心逻辑 ---")  # call阶段
    assert 1 == 1  # 用例成功