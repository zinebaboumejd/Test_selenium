import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testLoginvalide(self):
        self.driver.get("http://localhost:3000/login")
        self.driver.set_window_size(974, 1032)
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("admin@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
        self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys("admin1234")
        self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()

    def test_testLoginchampsvide(self):
        self.driver.get("http://localhost:3000/login")
        self.driver.set_window_size(974, 1032)
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
        self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()

    def test_testLoginemailinvalide(self):
        self.driver.get("http://localhost:3000/login")
        self.driver.set_window_size(974, 1032)
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("admin/gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
        self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys("admin1234")
        self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()

    def test_testLoginpasswordinvalide(self):
        self.driver.get("http://localhost:3000/login")
        self.driver.set_window_size(974, 1032)
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("admin@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
        self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys("admin")
        self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()

    # Pause de 10 secondes pour observer les résultats
    time.sleep(10)

if __name__ == "__main__":
    pytest.main([__file__])