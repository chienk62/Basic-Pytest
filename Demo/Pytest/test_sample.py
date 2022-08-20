from selenium import webdriver
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:/Python/Robot/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_xpath("//input[@placeholder = 'Username']").send_keys("Admin")
        driver.find_element_by_xpath("//input[@placeholder = 'Password']").send_keys("admin123")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        x = driver.title
        assert x == "OrangeHRM"
        
    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")
