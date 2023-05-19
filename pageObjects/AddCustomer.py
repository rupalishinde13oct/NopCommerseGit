import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomer:

    Customer_XPATH = (By.XPATH , "//a[@href='#']//p[contains(text(),'Customers')]")
    Click_Add_Customer_XPATH = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    AddNew_Button_XPATH = (By.XPATH, "//a[@class='btn btn-primary']")
    Txt_Email_XPATH = (By.XPATH, "//input[@id='Email']")
    Txt_Password_XPATH = (By.XPATH, "//input[@id='Password']")
    FirstName_XPATH = (By.XPATH, "//input[@id='FirstName']")
    LastName_XPATH = (By.XPATH, "//input[@id='LastName']")
    Gender_XPATH = (By.XPATH, "//input[@id='Gender_Female']")
    Click_calender_XPATH = (By.XPATH, "//span[@class='k-icon k-i-calendar']")
    DOB_XPATH = (By.XPATH , "//input[@id='DateOfBirth']")
    CompanyName_XPATH = (By.XPATH, "//input[@id='Company']")
    NewsLetter_XPATH = (By.XPATH ,  "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    NewsLetterSelect_XPATH = (By.XPATH, "//li[normalize-space()='Your store name']")
    Customer_Roles_XPATH = (By.XPATH , "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]")
    Customer_RolesSelect_XPATH = (By.XPATH , "//li[normalize-space()='Guests']")
    Manager_OF_Vender_XPATH = (By.XPATH, "//select[@id='VendorId']")
    Save_Button_XPATH = (By.XPATH, "//button[@name='save']")
    Success_MSG_XPATH = (By.XPATH , "//div[@class='alert alert-success alert-dismissable']")

    def __init__(self , d ):
        self.d = d
        # self.wait = WebDriverWait(self.d , 10)



    def Click_On_Customers(self):
        time.sleep(5)
        self.d.find_element(*AddCustomer.Customer_XPATH).click()

    def Click_Add_Customers(self):
        # self.wait.until(ec.presence_of_element_located((AddCustomer.Click_Add_Customer_XPATH)))
        time.sleep(5)
        self.d.find_element(*AddCustomer.Click_Add_Customer_XPATH).click()

    def Click_AddNew_Button(self):
        self.d.find_element(*AddCustomer.AddNew_Button_XPATH).click()

    def Enter_Email(self , email):
        # time.sleep(5)
        self.d.find_element(*AddCustomer.Txt_Email_XPATH).send_keys(email)

    def Enter_Password(self , password):
        self.d.find_element(*AddCustomer.Txt_Password_XPATH).send_keys(password)

    def Enter_FirstName(self , fname):
        self.d.find_element(*AddCustomer.FirstName_XPATH).send_keys(fname)

    def Enter_LastName(self ,lname):
        self.d.find_element(*AddCustomer.LastName_XPATH).send_keys(lname)

    def Select_Gender(self):
        self.d.find_element(*AddCustomer.Gender_XPATH).click()



    def Enter_DOB(self , dob):
        self.d.find_element(*AddCustomer.DOB_XPATH).send_keys(dob)

    def Enter_Company_Name(self , cname):
        self.d.find_element(*AddCustomer.CompanyName_XPATH).send_keys(cname)

    def Enter_NewsLetter(self):
        self.d.find_element(*AddCustomer.NewsLetter_XPATH).click()
        time.sleep(2)
        self.d.find_element(*AddCustomer.NewsLetterSelect_XPATH).click()

    def Enter_Customer_Roles(self):
        self.d.find_element(*AddCustomer.Customer_Roles_XPATH).clear()
        self.d.find_element(*AddCustomer.Customer_Roles_XPATH).click()
        # time.sleep(2)
        self.d.find_element(*AddCustomer.Customer_RolesSelect_XPATH).click()

    def Enter_Manager_Vender(self):
        Select(self.d.find_element(*AddCustomer.Manager_OF_Vender_XPATH)).select_by_visible_text("Vendor 1")

    def Click_Save(self):
        self.d.find_element(*AddCustomer.Save_Button_XPATH).click()


    def Success_Status(self):

        try:
            self.d.find_element(*AddCustomer.Success_MSG_XPATH)
            return True
        except NoSuchElementException:
            return False
