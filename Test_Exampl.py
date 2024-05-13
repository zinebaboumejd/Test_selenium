
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# Renseignez le chemin de votre chromedriver dans executable_path
service = Service(executable_path='C:\\chromedriver_win32\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com/pulse/selenium-un-guide-exhaustif-pour-lautomatisation-des-tests-barta/")

# ...
sleep(10)
driver.quit()



    # def test_testLoginvalide(self):
    #     self.driver.get("http://localhost:3000/login")
    #     self.driver.set_window_size(974, 1032)
    #     self.driver.find_element(By.NAME, "name").click()
    #     self.driver.find_element(By.NAME, "name").send_keys("admin@gmail.com")
    #     self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
    #     self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys("admin1234")
    #     self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()



   # def test_testLoginchampsvide(self):
    #     self.driver.get("http://localhost:3000/login")
    #     self.driver.set_window_size(974, 1032)
    #     self.driver.find_element(By.NAME, "name").click()
    #     self.driver.find_element(By.NAME, "name").send_keys("t")
    #     self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
    #     self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys("t")
    #     self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()

    # def test_testLoginemailinvalide(self):
    #     self.driver.get("http://localhost:3000/login")
    #     self.driver.set_window_size(974, 1032)
    #     self.driver.find_element(By.NAME, "name").click()
    #     self.driver.find_element(By.NAME, "name").send_keys("admin/gmail.com")
    #     self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
    #     self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys("admin1234")
    #     self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()

    # def test_testLoginpasswordinvalide(self):
    #     self.driver.get("http://localhost:3000/login")
    #     self.driver.set_window_size(974, 1032)
    #     self.driver.find_element(By.NAME, "name").click()
    #     self.driver.find_element(By.NAME, "name").send_keys("admin@gmail.com")
    #     self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
    #     self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys("admin")
    #     self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()