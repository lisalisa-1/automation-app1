# -*- coding: utf-8 -*-
import allure
import pytest


@pytest.fixture(params=[("admin", "123"), ("guest", "456")], ids=["管理员", "访客"],name='get_data1')
def user_data(request):
    return request.param  # 通过 request 对象获取当前参数

class TestCartPage:

    @pytest.mark.regress
    @pytest.mark.skipif(pytest.__version__ < "11.0", reason="pytest版本低于7.0，跳过")
    def test_skipif(self):
        print(f"pytest版本低于7.0，跳过 {pytest.__version__}")
        assert True

    @pytest.mark.smoke
    def test_capsys(self,capsys):
        print("hello pytest")
        # 捕获输出
        captured = capsys.readouterr()
        # 断言输出内容
        assert captured.out.strip() == "hello pytest"

    # @pytest.mark.parametrize("page_objects", [["category", "home"]], indirect=True)
    def test_click_cart_button(self,page_factory):
        """测试点击购物车按钮"""
        # home_page = page_factory.get_page("home_page")
        # category_page = page_factory.get_page("category_page")

        pages=page_factory.get_pages(["home_page","category_page"])
        pages["home_page"].click_cart_button()


    @pytest.mark.parametrize("number", [1, 2, 3, 4])
    def test_is_even(self,number):
        assert number % 2 == 0  # 依次验证 1、2、3、4 是否为偶数

    @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (3, 5, 8), (2, 4, 6)])
    def test_add(self,a, b, expected):
        assert a + b == expected  # 验证三组加法运算

    @pytest.mark.parametrize("user", ["admin", "guest"])
    @pytest.mark.parametrize("status", [200, 401, 403])
    def test_permission(self,user, status):
        print(f"用户: {user}, 预期状态码: {status}")

    @pytest.mark.parametrize("user, pwd", [("anjing", "123"), ("test", "456")],
                             ids=["正常用户", "测试用户"])
    def test_login(self,user, pwd):
        assert user!=pwd


    data = [
        ("valid", "pass"),
        pytest.param("invalid", "fail", marks=[pytest.mark.skip(reason="暂不执行"), allure.story("无效用户登录")])
    ]
    @pytest.mark.parametrize("user, pwd", data)
    def test_login_(self,user, pwd):
        assert user!=pwd



    #@pytest.mark.skipif(reason="暂不执行")
    def test_access(self,get_data1):
        user, pwd = get_data1
        assert user!=pwd  # 执行2个用例，分别使用管理员和访客账号
        assert "h" in "hello"

    def test_assert_demo(self):
        # 基础相等/不等断言
        assert 10 == 10
        assert 10 != 5

        # 包含/不包含断言
        assert "hello" in "hello world"
        assert "python" not in "java"

        # 布尔断言
        assert True
        assert not False

        # 异常断言（核心：测试函数是否抛出预期异常）
        def divide(a, b):
            return a / b

        # 断言抛出 ZeroDivisionError 异常
        with pytest.raises(ZeroDivisionError):
            divide(1, 1)

        # 进阶：捕获异常并验证异常信息
        with pytest.raises(ZeroDivisionError) as exc_info:
            divide(1, 0)
        assert "division by zero" in str(exc_info.value)
        print(exc_info.value)




