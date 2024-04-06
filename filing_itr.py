import customtkinter as ctk
import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Computation(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.columnconfigure((0,1,2,3,4), weight=1)
        self.main_frame = MainFrame(self)
        self.methods = Methods()

class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row = 0, column = 0, sticky = "nsew", columnspan = 5)

        self.methods = Methods()
        self.driver = None
        
        #grid config
        self.columnconfigure((0,1,2,3,4), weight=1)
        
        self.generate_pdf = ctk.CTkButton(self, text="Open Page", command=self.open_driver)
        self.generate_pdf.grid(row = 0, column = 0)

        self.close_window = ctk.CTkButton(self, text="Close Driver", command=self.close_window)
        self.close_window.grid(row = 6, column = 0)

        self.user_login = ctk.CTkButton(self, text="Login", command=self.user_login)
        self.user_login.grid(row = 0, column = 1)

        self.file_now = ctk.CTkButton(self, text="File Now", command=self.file_now)
        self.file_now.grid(row = 0, column = 2)

        self.personal_info = ctk.CTkButton(self, text="Personal info", command=self.enter_personal_info)
        self.personal_info.grid(row = 0, column = 3)

        self.personal_info = ctk.CTkButton(self, text="Income info", command=self.enter_income_info)
        self.personal_info.grid(row = 0, column = 4)


    def enter_income_info(self):
        self.methods.enter_income_info(self.driver)
    
    def enter_personal_info(self):
        self.methods.enter_personal_info(self.driver)
    
    def file_now(self):
        self.methods.file_now(self.driver)

    def open_driver(self):
        self.driver = self.methods.open_driver()
    
    def user_login(self):
        self.methods.user_login(self.driver)

    def close_window(self):
        self.driver.quit()

class Methods():
    def __init__(self):
        super().__init__()

    def open_driver(self):
        # Set Chrome options to disable automation flag
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        # Create a new instance of the Chrome driver with the specified options
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to Google's website
        driver.get('https://eportal.incometax.gov.in/iec/foservices/')
        time.sleep(5)

        return driver

    def user_login(self, driver):
        user_id = driver.find_element(By.ID, "panAdhaarUserId")
        user_id.send_keys(Keys.CONTROL, 'a')
        user_id.send_keys("ehfpr0552a")

        time.sleep(0.3)

        cont_btn = driver.find_element(By.XPATH, "//button[@class='large-button-primary width marTop16']")
        cont_btn.click()
        time.sleep(5)
        check_box = driver.find_element(By.XPATH, "//span[@class='mat-checkbox-label']")
        check_box.click()
        time.sleep(0.3)
        password = driver.find_element(By.ID, "loginPasswordField")
        password.send_keys(Keys.CONTROL, 'a')
        password.send_keys(str("Naina@7557"))
        time.sleep(0.3)
        login = driver.find_element(By.XPATH, "//button[@class='large-button-primary width marTop26']")
        login.click()

    def file_now(self, driver): 
        file_now = driver.find_element(By.ID, "fileNowRevisedBtn")
        file_now.click()
        time.sleep(2)

        select_mode = driver.find_element(By.XPATH, '//div[@class="A-Gross-Total-Income"]')
        select_mode.click()
        time.sleep(0.5)

        cont = driver.find_element(By.XPATH, '//button[@type="submit"]')
        cont.click()

        time.sleep(2)
        start_new_filing = driver.find_element(By.XPATH, '//button[@class="primaryButton mt-4 mt-md-0 float-right downloadButtons largeButton"]')
        start_new_filing.click()

    def enter_personal_info(self, driver):
        personal_info = driver.find_element(By.ID, "uniservenxtcmp_text_18")
        personal_info.click()

        time.sleep(5)
        employment = driver.find_element(By.ID, "select2-uniservenxtcmp_dropdown_357-container")
        employment.click()

        time.sleep(1)

        try:
            select_employment = driver.find_element(By.ID, "select2-uniservenxtcmp_dropdown_357-result-53p0-OTH")
            select_employment.click()
        except Exception as e:
            print(f"select_employment {e}")

        rep = driver.find_element(By.ID, "form2")
        rep.click()

        time.sleep(0.3)
        cont = driver.find_element(By.ID, "uniservenxtcmp_button_218")
        cont.click()

    def enter_income_info(seld, driver):
        income = driver.find_element(By.ID, "uniservenxtcmp_text_22")
        income.click()
        time.sleep(2)
        try:
            cont = driver.find_element(By.ID, "uniservenxtcmp_button_60")
            cont.click()
        except Exception as e:
            time.sleep(4)
            cont = driver.find_element(By.ID, "uniservenxtcmp_button_60")
            cont.click()
        try:
            time.sleep(4)
            add_income = driver.find_element(By.ID, "uniservenxtcmp_button_348")
            add_income.click()
        except Exception as e:
            time.sleep(4)
            add_income = driver.find_element(By.ID, "uniservenxtcmp_button_348")
            add_income.click()

        business_name1 = driver.find_element(By.ID, "uniservenxtcmp_textbox_39")
        business_name1.send_keys(Keys.CONTROL, 'a')
        business_name1.send_keys("business_name")
        time.sleep(1)

        b_code = driver.find_element(By.ID, "select2-uniservenxtcmp_dropdown_53-container")
        b_code.click()
        time.sleep(1)
        b_code = driver.find_element(By.XPATH, '//input[@aria-label="searchbox"]')
        b_code.send_keys("14007")

        time.sleep(1)

        b_code = driver.find_element(By.ID, "select2-uniservenxtcmp_dropdown_53-result-wsuc-14007")
        b_code.click()

        time.sleep(1)

        add = driver.find_element(By.ID, "uniservenxtcmp_button_169")
        add.click()

if __name__ == "__main__":
    comp = Computation()
    comp.mainloop()