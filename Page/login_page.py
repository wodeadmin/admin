from Base.Base import Base
import Page, allure

class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self,driver)

    def click_my_btn(self):
        # 点击我的按钮
        self.click_element(Page.my_btn)

    def click_insert_login(self):
        # 点击登陆/注册
        self.click_element(Page.insert_login)


    def login(self, phone, passwd):
        # 登陆操作
        # 输入用户名
        self.input_element(Page.login_name, phone)
        # 输入密码
        self.input_element(Page.login_passwd, passwd)
        # 点击登陆按钮
        self.click_element(Page.login_btn)

    def get_suc_login_status(self):
        # 判断是否登陆成功，成功返回True 不成功返回False
        try:
            self.search_element(Page.login_suc_mes, timeout=10)
            return True
        except Exception as e:
            return False

    def login_faile_x(self):
        # 点击登陆页面关闭按钮
        self.click_element(Page.login_page_close)


