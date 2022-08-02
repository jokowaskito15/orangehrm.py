import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class TestMenuAdmin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_search_blank_username_employee(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("") # isi username
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("") # isi employee
        browser.find_element(By.ID,"searchBtn").click() # klik tombol search

        # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        self.assertEqual(expected_current_url,browser.current_url)

    def test_b_search_username_belum_terdaftar(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("wkwkwkwkwkk") # isi username
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("") # isi employee
        browser.find_element(By.ID,"searchBtn").click() # klik tombol search

        # validasi
        expected_message = "No Records Found"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#resultTable > tbody > tr > td").text
        self.assertEqual(expected_message,actual_message)

    def test_c_search_employee_belum_terdaftar(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("") # isi username
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("awokawokawok") # isi employee
        browser.find_element(By.ID,"searchBtn").click() # klik tombol search

        # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        self.assertEqual(expected_current_url,browser.current_url)

    def test_d_search_username_employee_belum_terdaftar(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("wkwkwkwkwkk") # isi username
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("awokawokawok") # isi employee
        browser.find_element(By.ID,"searchBtn").click() # klik tombol search

        # validasi
        expected_message = "No Records Found"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#resultTable > tbody > tr > td").text
        self.assertEqual(expected_message,actual_message)

    def test_e_tombol_reset(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("wkwkwkwkwkk") # isi username
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("awokawokawok") # isi employee
        browser.find_element(By.ID,"resetBtn").click() # klik tombol reset

        # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        self.assertEqual(expected_current_url,browser.current_url)

    def test_f_tombol_search(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("jokoganteng") # isi username
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("Garry White") # isi employee
        browser.find_element(By.ID,"searchBtn").click() # klik tombol search

        # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        self.assertEqual(expected_current_url,browser.current_url)

    def test_g_tombol_add(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"btnAdd").click() # klik tombol add

        # validasi
        expected_message = "Add User"
        actual_message = browser.find_element(By.ID,"UserHeading").text
        self.assertEqual(expected_message,actual_message)

    def test_h_form_adduser_dibiarkan_kosong(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"btnAdd").click() # klik tombol add
        Select(browser.find_element(By.ID,"systemUser_userType")).select_by_index(0) # select admin
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("") # isi employee
        browser.find_element(By.ID,"systemUser_userName").send_keys("") # isi username
        Select(browser.find_element(By.ID,"systemUser_status")).select_by_index(0) # select status
        browser.find_element(By.ID,"systemUser_password").send_keys("") # isi password
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("") # isi new password
        browser.find_element(By.ID,"btnSave").click() # klik button Save

    #     # validasi
        expected_message = "Required"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#frmSystemUser > fieldset > ol > li:nth-child(2) > span").text
        self.assertEqual(expected_message,actual_message)

    def test_i_form_adduser_test_tombol_save(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"btnAdd").click() # klik tombol add
        Select(browser.find_element(By.ID,"systemUser_userType")).select_by_index(0) # select admin
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Garry White") # isi employee
        browser.find_element(By.ID,"systemUser_userName").send_keys("nangisajah2") # isi username
        Select(browser.find_element(By.ID,"systemUser_status")).select_by_index(0) # select status
        browser.find_element(By.ID,"systemUser_password").send_keys("123123123") # isi password
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("123123123") # isi new password
        browser.find_element(By.ID,"btnSave").click() # klik button Save

    #     # validasi
        expected_message = "Admin"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#menu_admin_viewAdminModule > b").text
        self.assertEqual(expected_message,actual_message)
        
    def test_j_form_adduser_test_tombol_cancel(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"btnAdd").click() # klik tombol add
        Select(browser.find_element(By.ID,"systemUser_userType")).select_by_index(0) # select admin
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Garry White") # isi employee
        browser.find_element(By.ID,"systemUser_userName").send_keys("jokoganteng10") # isi username
        Select(browser.find_element(By.ID,"systemUser_status")).select_by_index(0) # select status
        browser.find_element(By.ID,"systemUser_password").send_keys("123123123") # isi password
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("123123123") # isi new password
        browser.find_element(By.ID,"btnCancel").click() # klik button Cancel

    #     # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers?userId="
        self.assertEqual(expected_current_url,browser.current_url)

    def test_k_test_tombol_delete(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        browser.maximize_window()
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login

        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#resultTable > tbody > tr:nth-child(1) > td:nth-child(1)").click() # klik ceklis
        time.sleep(1)
        browser.find_element(By.ID,"btnDelete").click() # klik button Delete
        time.sleep(1)
        browser.find_element(By.ID,"dialogDeleteBtn").click() # klik button Delete

    #     # validasi
        expected_message = "Admin"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#menu_admin_viewAdminModule > b").text
        self.assertEqual(expected_message,actual_message)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()