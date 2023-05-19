import time

from Utilities.readConfigFile import ReadConfig

from Utilities.Logger import Logging


class TestPageTitle:

    log = Logging.loggen()
    url = ReadConfig.getUrl()
    def test_PageTitle_001(self , setup):
        self.log.info("test_PageTitle_001 is Started")
        self.d = setup
        self.d.get(self.url)
        self.log.info("Launching Browser-->" + self.url)

        # time.sleep(5)
        if self.d.title == "Your store. Login":
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_PageTitle_001_Pass.png")
            self.log.info("test_PageTitle_001 is Passed")
            self.log.info("Page Title is-->" + self.d.title)
            assert True
        else:
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NonCommerse\\Screenshots\\test_PageTitle_001_Fail.png")
            self.log.info("test_PageTitle_001 is Failed")
            assert False
        self.log.info("test_PageTitle_001 is Completed")