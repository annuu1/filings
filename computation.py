import os
import customtkinter as ctk
import json
import pdfkit
from codes import codes
from customtkinter import filedialog

class Dependency_manager():
    def __init__(self):
        pass

class Computation(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.columnconfigure((0,1,2,3,4), weight=1)
        main_frame = MainFrame(self)

class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row = 0, column = 0, sticky = "nsew", columnspan = 5)
        
        self.json_path = None

        #grid config
        self.columnconfigure((0,1,2,3,4), weight=1)

        self.ask_file =ctk.CTkLabel(self, text="Open File:", width=50)
        self.ask_file.grid(row = 0, column = 0, padx = (5,5), pady = (5,5), sticky = "nsew")

        self.open_file_button = ctk.CTkButton(self, text="Select File", command=self.get_file)
        self.open_file_button.grid(row = 0, column = 1, padx = (5,5), pady = (5,5), sticky = "nsew")

        self.gender = ctk.CTkComboBox(self, values=["Male", "Female"])
        self.gender.grid(row = 0, column = 3, padx = (5,5), pady = (5,5), sticky = "nsew")
        self.gender.set(value="Male")

        self.regime = ctk.CTkComboBox(self, values=["Old Regime", "New Regime"])
        self.regime.grid(row = 0, column = 4, padx = (5,5), pady = (5,5), sticky = "nsew")
        self.regime.set(value="New Regime")
        ctk.CTkLabel(self, text="Enter Ack").grid(row = 1, column = 0, padx = (5,5), pady = (5,5), sticky = "nsew")

        self.acknowledgement= ctk.CTkEntry(self)
        self.acknowledgement.grid(row = 1, column = 1, padx = (5,5), pady = (5,5), sticky = "nsew")

        self.generate_pdf = ctk.CTkButton(self, text="Generate Pdf", command=self.create_pdf)
        self.generate_pdf.grid(row = 5, column = 0, columnspan = 5,  padx = (5,5), pady = (5,5), sticky = "nsew")

    def create_pdf(self):
        methods = Methods()

        path = self.json_path
        gender = self.gender.get()
        regime = self.regime.get()
        acknowledgement = self.acknowledgement.get()
        print(acknowledgement)
        
        methods.create_pdf(path, gender, regime, acknowledgement)
    
    def get_file(self):
        self.json_path = filedialog.askopenfilenames(initialdir = r"C:\Users\avnin\Downloads",
										title = "Select a File",
										filetypes = (("JSON files",
														"*.json*"),
													("all files",
														"*.*")))
        if self.json_path:  # Check if any file is selected
            self.json_path = str(self.json_path[0])

        # self.ask_file.configure(text = self.json_path)

class Methods:
    def __init__(self):
        pass

    def generate_comp_pdf(self,customer_name, ay, address, mob, email, pan, status, dob, res_status, father, gender, ac, ifsc, filing_status, aadhar, regime, acknowledgement, IncomeFromBusinessProf, income, other_income, exempt_income, gross_income, deductions, rounded_off, special_rates_tax, total_tax, rebate, tax_payable, tds, tds_round, gross_total_income, total_net_income, bank, b_nature, b_code, b_trade_name, sundry_deb, sundry_cred, inventory, cash, total_other_income):
        template_path = r'D:\Study\Python Projects\filings\computation_template.html'
        output_path = f"C:\\Users\\avnin\\Desktop\\computations\\{customer_name} COMP {ay}.pdf"

        # Replace placeholders in the template
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()
            template_content = template_content.replace('{{name}}', str(customer_name))
            template_content = template_content.replace('{{ay}}', str(ay))
            template_content = template_content.replace('{{address}}', str(address))
            template_content = template_content.replace('{{mob}}', str(mob))
            template_content = template_content.replace('{{email}}', email)
            template_content = template_content.replace('{{pan}}', pan)
            template_content = template_content.replace('{{status}}', status)
            template_content = template_content.replace('{{dob}}', dob)
            template_content = template_content.replace('{{res_status}}', res_status)
            template_content = template_content.replace('{{father}}', father)
            template_content = template_content.replace('{{gender}}', gender)
            template_content = template_content.replace('{{ac}}', ac)
            template_content = template_content.replace('{{ifsc}}', ifsc)
            template_content = template_content.replace('{{filing_status}}', str(filing_status))
            template_content = template_content.replace('{{aadhar}}', aadhar)
            template_content = template_content.replace('{{regime}}', regime)
            template_content = template_content.replace('{{acknowledgement}}', acknowledgement)
            template_content = template_content.replace('{{IncomeFromBusinessProf}}', str(IncomeFromBusinessProf))
            template_content = template_content.replace('{{other_income}}', str(other_income))
            template_content = template_content.replace('{{exempt_income}}', str(exempt_income))
            template_content = template_content.replace('{{gross_income}}', str(gross_income))
            template_content = template_content.replace('{{deductions}}', str(deductions))
            template_content = template_content.replace('{{rounded_off}}', str(rounded_off))
            template_content = template_content.replace('{{special_rates_tax}}', str(special_rates_tax))
            template_content = template_content.replace('{{total_tax}}', str(total_tax))
            template_content = template_content.replace('{{rebate}}', str(rebate))
            template_content = template_content.replace('{{tax_payable}}', str(tax_payable))
            template_content = template_content.replace('{{tds}}', str(tds))
            template_content = template_content.replace('{{tds_round}}', str(tds_round))
            template_content = template_content.replace('{{gross_total_income}}', str(gross_total_income))
            template_content = template_content.replace('{{total_net_income}}', str(total_net_income))
            template_content = template_content.replace('{{bank}}', bank)
            template_content = template_content.replace('{{b_nature}}', str(b_nature))
            template_content = template_content.replace('{{b_code}}', b_code)
            template_content = template_content.replace('{{b_trade_name}}', b_trade_name)
            template_content = template_content.replace('{{sundry_deb}}', str(sundry_deb))
            template_content = template_content.replace('{{sundry_cred}}', str(sundry_cred))
            template_content = template_content.replace('{{inventory}}', str(inventory))
            template_content = template_content.replace('{{cash}}', str(cash))
            template_content = template_content.replace('{{total_other_income}}', str(total_other_income))

        # Generate PDF
        config = pdfkit.configuration(wkhtmltopdf=r'D:\my files\Applications\wkhtmltopdf.exe')
        pdfkit.from_string(template_content, output_path, configuration=config) #pdfkit.configuration(wkhtmltopdf=r"D:\my files\Applications\wkhtmltopdf.exe"))
        
    def create_pdf(self, file_path, gender, regime, acknowledgement):
        # file_path = r"C:\Users\avnin\Downloads\BXFPA4275G_upload_2024-25_03-04-2024-11-51.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Join the script directory with the provided file path
        absolute_file_path = os.path.join(script_dir, file_path)
        print("Absolute file path:", absolute_file_path)
        print("Current working directory:", os.getcwd())
        
        try:
            with open(absolute_file_path, 'r', encoding='utf-8') as json_file:
                itr_data = json.load(json_file)
                # Extract values
                customer_name = itr_data['ITR']['ITR4']['Verification']['Declaration']['AssesseeVerName'] #+ ' ' + itr_data['ITR']['ITR4']['PersonalInfo']['AssesseeName']['SurNameOrOrgName']
                ay = itr_data['ITR']['ITR4']['Form_ITR4']['AssessmentYear']
                address_data = itr_data['ITR']['ITR4']['PersonalInfo']['Address']
                excluded_keys = ["Phone", 'StateCode','CountryCode','CountryCodeMobile', 'MobileNo', 'EmailAddress']
                address_values = [str(value) for key, value in address_data.items() if key not in excluded_keys]
                address = ', '.join(address_values)

                # gender='Male'
                mob = itr_data['ITR']['ITR4']['PersonalInfo']['Address']['MobileNo']
                email = itr_data['ITR']['ITR4']['PersonalInfo']['Address']['EmailAddress']
                pan = itr_data['ITR']['ITR4']['PersonalInfo']['PAN']
                status = 'Individual'
                dob = itr_data['ITR']['ITR4']['PersonalInfo']['DOB']
                res_status = 'Resident'
                father = itr_data['ITR']['ITR4']['Verification']['Declaration']['FatherName']
                ac = itr_data['ITR']['ITR4']['Refund']['BankAccountDtls']['AddtnlBankDetails'][0]['BankAccountNo']
                ifsc = itr_data['ITR']['ITR4']['Refund']['BankAccountDtls']['AddtnlBankDetails'][0]['IFSCCode']
                filing_status = "Filed" #itr_data['ITR']['ITR4']['FilingStatus']['ReturnFileSec']
                aadhar = itr_data['ITR']['ITR4']['PersonalInfo']['AadhaarCardNo']
                # regime = "New Regime" #itr_data['ITR']['ITR4']['FilingStatus']['OptOutNewTaxRegime']
                IncomeFromBusinessProf = itr_data['ITR']['ITR4']['IncomeDeductions']['IncomeFromBusinessProf']
                income = itr_data['ITR']['ITR4']['IncomeDeductions']['IncomeFromBusinessProf']
                # Some values not provided in the data, hence set to 0
                other_income = itr_data['ITR']['ITR4']['IncomeDeductions']['IncomeOthSrc']
                exempt_income = 0
                gross_income = itr_data['ITR']['ITR4']['IncomeDeductions']['GrossTotIncome']
                deductions = 0
                rounded_off = itr_data['ITR']['ITR4']['IncomeDeductions']['TotalIncome']
                special_rates_tax = itr_data['ITR']['ITR4']['TaxComputation']['TotalTaxPayable']

                total_tax = special_rates_tax
                rebate = itr_data['ITR']['ITR4']['TaxComputation']['Rebate87A']
                tax_payable = itr_data['ITR']['ITR4']['TaxComputation']['TaxPayableOnRebate']
                tds = itr_data['ITR']['ITR4']['TaxPaid']['TaxesPaid']['TDS']
                tds_round = round(tds, -1)
                gross_total_income = itr_data['ITR']['ITR4']['IncomeDeductions']['GrossTotIncome']
                total_net_income = itr_data['ITR']['ITR4']['IncomeDeductions']['TotalIncome']
                bank = itr_data['ITR']['ITR4']['Refund']['BankAccountDtls']['AddtnlBankDetails'][0]['BankName']
                
                b_code = itr_data['ITR']['ITR4']['ScheduleBP']['NatOfBus44AD'][0]['CodeAD']
                b_nature = codes.get(b_code)
                b_trade_name = itr_data['ITR']['ITR4']['ScheduleBP']['NatOfBus44AD'][0]['NameOfBusiness']
                sundry_deb = itr_data['ITR']['ITR4']['ScheduleBP']['FinanclPartclrOfBusiness']['SundryDebtors']
                sundry_cred = itr_data['ITR']['ITR4']['ScheduleBP']['FinanclPartclrOfBusiness']['SundryCreditors']
                inventory = itr_data['ITR']['ITR4']['ScheduleBP']['FinanclPartclrOfBusiness']['Inventories']
                cash = itr_data['ITR']['ITR4']['ScheduleBP']['FinanclPartclrOfBusiness']['CashInHand']
                total_other_income = other_income

                # Return extracted data as dictionary
                self.generate_comp_pdf(
                customer_name,
                ay,
                address,
                mob,
                email,
                pan,
                status,
                dob,
                res_status,
                father,
                gender,
                ac,
                ifsc,
                filing_status,
                aadhar,
                regime,
                acknowledgement,
                IncomeFromBusinessProf,
                income,
                other_income,
                exempt_income,
                gross_income,
                deductions,
                rounded_off,
                special_rates_tax,
                total_tax,
                rebate,
                tax_payable,
                tds,
                tds_round,
                gross_total_income,
                total_net_income,
                bank,
                b_nature,
                b_code,
                b_trade_name,
                sundry_deb,
                sundry_cred,
                inventory,
                cash,
                total_other_income
    )
        except FileNotFoundError as e:
            print(f"File not found: {absolute_file_path}")
        except json.JSONDecodeError:
            print(f"JSON Decode error: JSON data in file {file_path}")
        except KeyError as e:
            print(f"Key not found in JSON data: {e}")

if __name__ == "__main__":
    comp = Computation()
    comp.mainloop()