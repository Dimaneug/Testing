import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class StackOverflowTest(unittest.TestCase):

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument("start-maximized")
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        # option.add_argument('--headless')
        # option.add_argument('--window-size=800,600')
        self.browser = webdriver.Chrome(options=option)

    def test_authorization(self):
        self.browser.get('https://stackoverflow.com')
        self.browser.find_element(By.XPATH, '/html/body/header/div/nav/ol/\
        li[3]/a').click()
        self.browser.find_element(By.ID, 'email').send_keys('dimaneug@gmail.com')
        self.browser.find_element(By.ID, 'password').send_keys('tDWIGNoU1vEqRDeuhOsdpQfKISaoB1')
        # try:
        #     self.browser.find_element(By.CLASS_NAME, 'js-accept-cookies').click()
        # except:
        #     pass
        self.browser.find_element(By.ID, 'submit-button').click()
        time.sleep(1)
        self.assertNotIn('Log In', self.browser.title)

    def test_find_user(self):
        self.browser.get('https://stackoverflow.com/users')
        if self.browser.find_element(By.CLASS_NAME, 'js-accept-cookies'):
            self.browser.find_element(By.CLASS_NAME, 'js-accept-cookies').click()
        self.browser.find_element(By.ID, 'userfilter').send_keys('dimaneug')
        time.sleep(1)
        link = self.browser.find_element(By.XPATH, '/html/body/div[3]/\
                      div[2]/div/div[3]/div[1]/div/div[2]/a').get_property('href')
        self.assertIn('20636431', link)

    def test_voting(self):
        self.browser.get('https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than'
                         '-processing-an-unsorted-array')
        self.browser.save_screenshot('1.png')
        self.browser.find_element(By.CLASS_NAME, 'iconArrowUpLg').click()
        time.sleep(1)
        self.assertIn('Join the Stack Overflow community',
                      self.browser.find_element(By.ID, 'anon-modal-title').get_attribute('innerHTML'))

    def test_search(self):
        self.browser.get('https://stackoverflow.com/questions')
        self.browser.find_element(By.CLASS_NAME, 's-input').send_keys('score: 100', Keys.RETURN)
        time.sleep(2)
        if 'Human verification' in self.browser.title:
            time.sleep(10)
        self.browser.save_screenshot('1.png')
        self.assertIn('500 results',
                      self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[3]/div[1]').text)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
