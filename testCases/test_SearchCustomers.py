import time

from selenium.webdriver.common.by import By
from Utilities.Logger import Logging
from Utilities.readConfigFile import ReadConfig
from pageObjects.Login import LoginPage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomer import SearchCustomers
class TestSearchCustomers:

    url = ReadConfig.getUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    log = Logging.loggen()

    def test_SearchCustomer_004(self , setup1):
        self.d = setup1
        self.log.info("test_SearchCustomer_004 is Started")
        self.d.get(self.url)
        self.log.info("Go to --> " + self.url)

        self.lp = LoginPage(self.d)
        self.lp.Enter_Email(self.email)
        self.log.info("Entering Email -->" + self.email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering password -->" + self.password)
        self.lp.Click_On_LoginButton()
        self.log.info("Click on Login Button")

        self.ac = AddCustomer(self.d)
        self.ac.Click_On_Customers()
        self.log.info("Click on Customers")
        self.ac.Click_Add_Customers()
        self.log.info("Click on Add Customers")
        self.sc = SearchCustomers(self.d)
        self.sc.Enter_First_Name("Rupali")
        self.log.info("Entering First Name")
        self.sc.Enter_Last_Name("Shinde")
        self.log.info("Entering Last Name")
        time.sleep(2)
        self.sc.Click_Search_Button()
        self.log.info("Click on Search Button")
        time.sleep(10)

        if self.sc.Success_Status() == True :

                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_SearchCustomer_004_Pass.png")
                self.log.info("test_SearchCustomer_004 is Passed")

        else:
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_SearchCustomer_004_Fail.png")
            self.log.info("test_SearchCustomer_004 is Failed")
            assert False

        self.log.info("test_SearchCustomer_004 is Completed")











        # if self.sc.Success_Status() == True :
        #
        #     self.l = len(self.d.find_elements(By.CSS_SELECTOR, "tbody tr"))
        #     self.col = len(self.d.find_elements(By.CSS_SELECTOR , "tbody td"))
        #     # print(self.col)
        #     if self.col > 1:
        #         print(self.l, "Search Found")
        #         print("Values are-->")
        #         for i in range(1, self.l + 1):
        #             val = self.d.find_element(By.XPATH,
        #                                       "//div[@class='card card-default']//div[@class='card-body']/div[2]/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[" + str(
        #                                           i) + "]").text
        #             print(val)
        #         self.d.save_screenshot(
        #             "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_SearchCustomer_004_Pass.png")
        #         self.log.info("test_SearchCustomer_004 is Passed")
        #
        #
        #     elif self.col == 1:
        #         print("No Search Found")
        #
        #     assert True
        # else:
        #     self.d.save_screenshot(
        #         "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_SearchCustomer_004_Fail.png")
        #     self.log.info("test_SearchCustomer_004 is Failed")
        #     assert False
        #
        # self.log.info("test_SearchCustomer_004 is Completed")



