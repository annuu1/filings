import customtkinter as ttk
from selenium import webdriver
import time

class Whatsapp(ttk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")

        # Grid configuration
        self.columnconfigure((0, 1, 2, 3, 4), weight=0)

        frame = Frame(self)

class Frame(ttk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.driver = None

        self.grid(row=0, column=0, sticky="nsew")
        ttk.CTkLabel(self, text="Send Whatsapp").grid(row=0, column=0, sticky="nsew")

        self.open_whatsapp = ttk.CTkButton(self, text="Open whatsapp", command=self.open_whatsapp)
        self.open_whatsapp.grid(row=0, column=0, sticky="nsew")

    def open_whatsapp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)

if __name__ == "__main__":
    app = Whatsapp()
    app.mainloop()

# Add this line to keep the program from closing immediately
input("Press Enter to exit")
