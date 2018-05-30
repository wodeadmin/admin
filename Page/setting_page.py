from Base.Base import Base
import Page


class Setting_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_setting_btn(self):
        # 点击个人中心设置按钮
        self.click_element(Page.person_setting_btn)

    def click_logout_btn(self):
        # 点击退出登陆按钮
        self.click_element(Page.logout_btn)