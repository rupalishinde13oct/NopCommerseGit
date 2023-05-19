import time

from Utilities.Logger import Logging
from Utilities.readConfigFile import ReadConfig
from pageObjects.AddCustomer import AddCustomer

from pageObjects.Login import LoginPage


class TestAddCustomer:

    url = ReadConfig.getUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    log = Logging.loggen()

    def test_AddCustomer_003(self , setup1):
        self.d = setup1
        self.log.info("test_AddCustomer_003 is Started")
        self.log.info("Launching browser")
        self.d.get(self.url)
        self.log.info("Go to -->" + self.url)
        self.lp = LoginPage(self.d)

        self.lp.Enter_Email(self.email)
        self.log.info("Entering email --> " + self.email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password -->" + self.password)
        self.lp.Click_On_LoginButton()
        self.log.info("Click on Login Button")

        self.ac = AddCustomer(self.d)
        self.ac.Click_On_Customers()
        self.log.info("Click on Customers")
        self.ac.Click_Add_Customers()
        self.log.info("Click on Add Customers")
        # time.sleep(2)
        self.ac.Click_AddNew_Button()
        self.log.info("Click on Add Button")
        self.ac.Enter_Email("ruupaaaldishhind231e@gmail.com")
        self.log.info("Entering Email address")
        self.ac.Enter_Password("rupali1323")
        self.log.info("Entering password")
        self.ac.Enter_FirstName("Rupali")
        self.log.info("Entering First Name")
        self.ac.Enter_LastName("Shinde")
        self.log.info("Entering Last Name")
        self.ac.Select_Gender()
        self.log.info("Select Gender")
        self.ac.Enter_DOB("05/03/2023")
        self.log.info("Entering Date Of Birth")
        self.ac.Enter_Company_Name("Credence")
        self.log.info("Entering Company Name")
        time.sleep(3)
        self.ac.Enter_NewsLetter()
        self.log.info("Entering NewsLetter")
        # self.ac.Enter_Customer_Roles()
        self.ac.Enter_Manager_Vender()
        self.log.info("Entering Manager Vender")
        self.ac.Click_Save()
        self.log.info("Click on Save Button")

        if self.ac.Success_Status() == True:
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_AddCustomer_003_Pass.png")
            self.log.info("test_AddCustomer_003 is Passed")
            assert True
        else:
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_AddCustomer_003_Fail.png")
            self.log.info("test_AddCustomer_003 is Failed")
            assert False

        self.log.info("test_AddCustomer_003 is Completed")






