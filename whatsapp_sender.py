import customtkinter as ctk

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random

import pandas as pd
import threading
import time

class Whatsapp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")

        #Grid configuration
        self.columnconfigure((0,1,2,3,4), weight=0)

        frame = Frame(self)

class Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.driver = None
        self.dependency_manager = Dependency_manager()

        self.grid(row = 0, column = 0, sticky = "nsew")
        ctk.CTkLabel(self, text="Send Whatsapp").grid(row = 0, column = 0, sticky = "nsew")

        self.open_whatsap = ctk.CTkButton(self, text="Open whatsapp", command=self.open_whatsapp)
        self.open_whatsap.grid(row = 0, column = 1, sticky = "nsew")

        self.send_whatsapp = ctk.CTkButton(self, text="Start whatsapp", command=self.send_whatsapp)
        self.send_whatsapp.grid(row = 0, column = 2, sticky = "nsew")

        self.stop_whatsapp = ctk.CTkButton(self, text="Stop whatsapp", command=self.stop_whatsapp)
        self.stop_whatsapp.grid(row = 0, column = 3, sticky = "nsew")

    def open_whatsapp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com')
        time.sleep(5)
    
    def stop_whatsapp(self):
        self.dependency_manager.set_loopflag(False)

    def send_whatsapp(self):
        
        self.dependency_manager.set_loopflag(True)
        methods = Methods()
        # Create a thread for the process_data function
        data_thread = threading.Thread(target=methods.process_data, args=(self.driver, self.dependency_manager))
        # Start the thread
        data_thread.start()
        # Continue with other tasks (if needed)
        print("Main thread continues executing other tasks...")

class Methods:
    def __init__(self):
        pass

    def communicate_whatsapp(self,driver, mobile, message):
            
        try:
            search_mob = driver.find_element(By.XPATH, '//*[@id=\"side\"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
            search_mob.send_keys(Keys.CONTROL, 'a')
            search_mob.send_keys(str(mobile))
        
            sleep_time = random.randint(5, 25)
            time.sleep(sleep_time)

            search_mob.send_keys(Keys.ENTER)
            time.sleep(0.5)

            try:
                saved_contact = None
                saved_contact = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div/div/span')
            except Exception as e:
                print(f'Exception:-- not found')
            if saved_contact and saved_contact.text == "No chats, contacts or messages found":
                return "No chats, contacts or messages found" 
        
            else:
                message_box = driver.find_element(By.XPATH, '//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                message_box.send_keys(Keys.CONTROL, 'v')
                time.sleep(0.5)
                
                send_button = driver.find_element(By.XPATH, '//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                send_button.send_keys(Keys.ENTER)
                return 'sent'
                
        except Exception as e:
            print(f'Exception: {e}')
            return "Unsent"

    def process_data(self, driver, dep_manager):
        # Read data from 'claretx_agents1.csv'
        mobile_df = pd.read_csv(r"D:\Study\Python Projects\filings\resources\raw_agents1.csv")

        # Print phone numbers and status
        for index, row in mobile_df.iterrows():
            if dep_manager.get_loopflag() and mobile_df.at[index, 'Status']=="Unsent":
                print(f"Phone: {row['Phone']}, Status: {row['Status']}")
                status = self.communicate_whatsapp(driver, mobile_df.at[index, 'Phone'], "Hi")
                print(status)
                mobile_df.at[index, 'Status'] = status
                time.sleep(1)
            else:
                print(f"Phone: {row['Phone']}, Status: {row['Status']}")
                if not dep_manager.get_loopflag():
                    break

        # Save the modified DataFrame to 'claretx_agents1.csv'
        mobile_df.to_csv(r"D:\Study\Python Projects\filings\resources\raw_agents1.csv", index=False)

        print("Data saved successfully.")

class Dependency_manager():
    def __init__(self):
        self.loop_flag = True

    def get_loopflag(self):
        return self.loop_flag
    
    def set_loopflag(self, value):
        self.loop_flag  = value


if __name__ == "__main__":
    app = Whatsapp()
    app.mainloop()
