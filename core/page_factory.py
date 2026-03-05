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

        return self.page_cache.get(f"{page_name}")

    def get_pages(self, page_names):
        """批量获取多个Page对象"""
        return {f"{name}": self.get_page(name) for name in page_names}