from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base:

    def __init__(self,driver):
        self.driver = driver

    def search_element(self, loc,timeout, poll=0.5):
        """
        # 定位单个元素
        :param loc:
        :param timeout:
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))
    def search_elements(self, loc,timeout):
        """
        # 定位一组元素
        :param loc:
        :param timeout:
        :return:
        """
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(*loc))
    def click_element(self,loc, timeout=5):
        """
        点击元素
        :param loc:
        :param timeout:
        :return:
        """
        self.search_element(loc, timeout).click()

    def input_element(self,loc, text,timeout=5):
        """
        输入内容
        :param loc:
        :param text:
        :param timeout:
        :return:
        """
        # 定位到元素
        input_text = self.search_element(loc, timeout)
        input_text.clear()
        input_text.send_keys(text)

    def find_toast(self,message, timeout=10):
        """
        # message: 预期要获取的toast的部分消息
        """
        try:
            message = "//*[contains(@text,'{}')]".format(message)  # 使用包含的方式定位
            toast_data = self.search_element((By.XPATH,message),timeout=5,poll=0.1)
            return toast_data.text
        except Exception as e:
            return False
