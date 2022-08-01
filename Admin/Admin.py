from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAdmin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_SearchUser(self): #search a valid username
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#menu_admin_viewAdminModule").click()
        time.sleep(1)
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(1)

        response_message = driver.find_element(By.XPATH,"//tbody/tr[1]/td[2]").text
        self.assertEqual(response_message, 'Admin')

    def test_b_AddLanguage(self): #add an existing language
        driver = self.driver
        action = ActionChains(driver)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#menu_admin_viewAdminModule").click()
        time.sleep(1)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_Qualifications")).perform()
        time.sleep(1)
        driver.find_element(By.ID,"menu_admin_viewLanguages").click()
        time.sleep(1)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        driver.find_element(By.ID,"language_name").send_keys("French")
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(1)

        response_data = driver.find_element(By.CSS_SELECTOR, "#recordsListDiv").text
        self.assertIn("Already Exists", response_data)
    
    def tearDown(self):
        self.driver.close()

unittest.main()