import time

from Utilities.Logger import Logging
from Utilities.readConfigFile import ReadConfig
from pageObjects.Login import LoginPage


class TestLogin:

    url = ReadConfig.getUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    log = Logging.loggen()

    def test_Login_002(self , setup):

        self.d = setup
        self.log.info("test_Login_002 is Started")
        self.d.get(self.url)
        self.log.info("Launching Browser")
        self.lp = LoginPage(self.d)
        time.sleep(5)
        self.lp.Enter_Email(self.email)
        self.log.info("Entering Email-->" + self.email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering password-->" + self.password)
        self.lp.Click_On_LoginButton()
        self.log.info("Click on Login Button")

        if self.lp.Login_Status() == True:
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_Login_002_Pass.png")
            self.log.info("test_Login_002 is Passed")
            self.lp.Click_On_LogoutButton()
            self.log.info("Click on Logout Button")
            assert True
        else:
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_Login_002_Fail.png")
            self.log.info("test_Login_002 is Failed")
            assert False

        self.log.info("test_Login_002 is Completed")
