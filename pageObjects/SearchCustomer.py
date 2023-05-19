import time

from selenium.webdriver.common.by import By


class SearchCustomers:

    First_Name_XPATH = (By.XPATH , "//input[@id='SearchFirstName']")
    Last_Name_XPATH = (By.XPATH, "//input[@id='SearchLastName']")
    Search_Button_XPATH = (By.XPATH , "//button[@id='search-customers']")
    Success_Status_XPATH = (By.XPATH , "//a[normalize-space()='1']")

    def __init__(self , d):
        self.d = d

    def Enter_First_Name(self , fname):
        self.d.find_element(*SearchCustomers.First_Name_XPATH).send_keys(fname)

    def Enter_Last_Name(self , lname):
        self.d.find_element(*SearchCustomers.Last_Name_XPATH).send_keys(lname)

    def Click_Search_Button(self ):
        self.d.find_element(*SearchCustomers.Search_Button_XPATH).click()


    def Success_Status(self):
        try:
            self.l = len(self.d.find_elements(By.CSS_SELECTOR, "tbody tr"))
            self.col = len(self.d.find_elements(By.CSS_SELECTOR, "tbody td"))
            # print(self.col)
            if self.col > 1:
                print(self.l, "Search Found")
                print("Values are-->")
                for i in range(1, self.l + 1):
                    val = self.d.find_element(By.XPATH,
                                              "//div[@class='card card-default']//div[@class='card-body']/div[2]/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[" + str(
                                                  i) + "]").text
                    print(val)

            elif self.col == 1:
                print("No Search Found")

            return True

        except:
            return False














        # try:
        #     if self.d.find_elements(By.CSS_SELECTOR, "tbody tr"):
        #         return True
        # except:
        #     return False

