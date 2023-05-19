import time

from Utilities.Logger import Logging
from Utilities.readConfigFile import ReadConfig
from pageObjects.Login import LoginPage


class TestLoginParam:

    url = ReadConfig.getUrl()
    log = Logging.loggen()

    def test_Login_Param_005(self , setup , getLoginData):

        self.d = setup
        self.log.info("test_Login_Param_005 is Started")
        self.d.get(self.url)
        self.log.info("Launching Browser")
        self.lp = LoginPage(self.d)
        time.sleep(5)
        self.lp.Enter_Email(getLoginData[0])
        self.log.info("Entering Email-->" + getLoginData[0])
        self.lp.Enter_Password(getLoginData[1])
        self.log.info("Entering password-->" + getLoginData[1])
        self.lp.Click_On_LoginButton()
        self.log.info("Click on Login Button")

        if self.lp.Login_Status() == True:
            if getLoginData[2] == 'Pass':

                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\"+getLoginData[0]+"#"+getLoginData[1]+"test_Login_Param_005_Pass.png")
                self.log.info("test_Login_002 is Passed")
                self.lp.Click_On_LogoutButton()
                self.log.info("Click on Logout Button")
                assert True

            else:
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\"+getLoginData[0]+"#"+getLoginData[1]+"test_Login_Param_005_Fail.png")
                self.log.info("test_Login_Param_005 is Failed")
                assert False
        else:
            if getLoginData[2] == 'Fail':
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\"+getLoginData[0]+"#"+getLoginData[1]+"test_Login_Param_005_Pass.png")
                self.log.info("test_Login_002 is Passed")
                assert True

            else:
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\"+getLoginData[0]+"#"+getLoginData[1]+"test_Login_Param_005_Fail.png")
                self.log.info("test_Login_002 is Passed")
                assert False


        self.log.info("test_Login_Param_005 is Completed")
