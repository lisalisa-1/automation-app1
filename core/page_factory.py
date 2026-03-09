# page_factory.py
class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self.page_cache = {}  # 缓存已初始化的Page，避免重复创建

    def get_page(self, page_name):
        """获取指定Page对象（单例模式，避免重复初始化）"""
        if page_name not in self.page_cache:
            if page_name == "home_page":
                from pages import HomePage
                self.page_cache["home_page"] = HomePage(self.driver)
            elif page_name == "category_page":
                from pages import CategoryPage
                self.page_cache["category_page"] = CategoryPage(self.driver)
            elif page_name == "my_page":
                from pages import MyPage
                self.page_cache["my_page"] = MyPage(self.driver)
            elif page_name == "cart_page":
                from pages import CartPage
                self.page_cache["cart_page"] = CartPage(self.driver)

            elif page_name == "goods_page":
                from pages import GoodsPage
                self.page_cache["goods_page"] = GoodsPage(self.driver)
            else:
                raise ValueError(f"未定义Page: {page_name}")

        return self.page_cache.get(f"{page_name}")

    def get_pages(self, page_names):
        """批量获取多个Page对象"""
        return {f"{name}": self.get_page(name) for name in page_names}