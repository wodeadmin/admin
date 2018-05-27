import pytest,allure


class Test_001:
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a",[1,2,3,4])
    def test_abc(self,a):
        assert a != 3
    @allure.step(title="测试步骤002")
    @pytest.mark.parametrize("a",[1,6,3,4])
    def test_abcc(self,a):
        assert a != 3