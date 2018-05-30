import pytest, allure

class Test_00x:

    def test_abc(self):
        with open("/Users/li/Documents/Worker/app_pro/Screen/111.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        try:
            1/0
            assert True
        except:
            assert False
        finally:
            print(1111111)

if __name__ == '__main__':
    pytest.main("-s test.py")