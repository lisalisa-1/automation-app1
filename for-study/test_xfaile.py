import pytest

# 标记为预期失败，依然会执行
@pytest.mark.xfail
def test_divide_by_zero():
    # 这个用例预期会抛异常（失败），符合xfail预期
    print("xfaile111111111111111111")
    assert 1 / 0 == 0

# 标记为预期失败，但实际执行成功（会显示xpass）
@pytest.mark.skip
def test_always_true():
    print("skip11111111111111111111111111111")
    assert 1 + 1 == 2