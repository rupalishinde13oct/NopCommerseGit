import time

from Utilities import XLUtils
from Utilities.Logger import Logging
from Utilities.XLUtils import getRowCount
from Utilities.readConfigFile import ReadConfig
from pageObjects.Login import LoginPage


class TestLogin:

    url = ReadConfig.getUrl()
    log = Logging.loggen()
    path = "D:\\Rupali Prathamesh Pandit\\NonCommerse\\TestData\\LoginData.xlsx"

    def test_Login_DDT_006(self , setup):

        self.d = setup
        self.log.info("test_Login_DDT_006 is Started")
        self.d.get(self.url)
        self.log.info("Launching Browser")
        self.lp = LoginPage(self.d)
        time.sleep(5)

        self.row = getRowCount(self.path, 'Sheet1')
        print(self.row)
        for i in range(2, self.row + 1):
            self.email = XLUtils.readXLData(self.path, 'Sheet1', i, 2)
            self.password = XLUtils.readXLData(self.path, 'Sheet1', i, 3)
            self.status = XLUtils.readXLData(self.path , 'Sheet1' , i , 4)
            self.lp.Enter_Email(self.email)
            self.log.info("Entering Email-->" + self.email)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering password-->" + self.password)
            self.lp.Click_On_LoginButton()
            self.log.info("Click on Login Button")


            if self.lp.Login_Status() == True:
                if self.status == "Pass":
                    self.d.save_screenshot(
                        "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\"+self.email+"#"+self.password+"test_Login_DDT_006_Pass.png")
                    self.log.info("test_Login_DDT_006 is Passed")
                    self.lp.Click_On_LogoutButton()
                    self.log.info("Click on Logout Button")

                else:
                    self.d.save_screenshot(
                        "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\"+self.email+"#"+self.password+"test_Login_DDT_006_Fail.png")
                    self.log.info("test_Login_DDT_006 is Failed")

            else:
                if self.status == "Fail":
                    self.d.save_screenshot(
                        "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\"+self.email+"#"+self.password+"test_Login_DDT_006_Pass.png")
                    self.log.info("test_Login_DDT_006 is Passed")

                else:
                    self.d.save_screenshot(
                        "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\"+self.email+"#"+self.password+"test_Login_DDT_006_Fail.png")
                    self.log.info("test_Login_DDT_006 is Failed")


        self.d.close()
        self.log.info("test_Login_DDT_006 is Completed")
