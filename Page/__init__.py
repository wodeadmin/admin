from selenium.webdriver.common.by import By
"""
    个人中心页面
"""
# 我的按钮
my_btn = (By.XPATH, "//*[contains(@text,'我的') and contains(@resource-id,'com.tpshop.malls:id/tab_txtv')]")
# 进入登陆页面
insert_login = (By.ID, "com.tpshop.malls:id/nickname_txtv")

"""
    登陆页面
"""
# 登陆用户名
login_name = (By.ID, "com.tpshop.malls:id/edit_phone_num")
# 登陆密码
login_passwd = (By.ID, "com.tpshop.malls:id/edit_password")
# 登陆按钮
login_btn = (By.ID, "com.tpshop.malls:id/btn_login")
# 登陆成功页面,判断我的订单是否存在
login_suc_mes = (By.XPATH, "//*[contains(@text,'我的订单') and contains(@resource-id,'com.tpshop.malls:id/title_txtv')]")
# 登陆页面点击关闭按钮
login_page_close = (By.ID, "com.tpshop.malls:id/titlebar_back_rl")

# 个人中心设置按钮
person_setting_btn = (By.ID, "com.tpshop.malls:id/setting_btn")
"""
    设置页面
"""
# 退出按钮
logout_btn = (By.ID, "com.tpshop.malls:id/exit_btn")