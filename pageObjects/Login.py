import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:

    Email_XPATH = (By.XPATH , "//input[@id='Email']")
    Password_XPATH = (By.XPATH , "//input[@id='Password']")
    LoginButton_XPATH = (By.XPATH , "//button[@type='submit']")
    Logout_XPATH = (By.XPATH , "//a[normalize-space()='Logout']")
    Login_Success_XPATH = (By.XPATH , "//p[normalize-space()='Dashboard']") #//h1[normalize-space()='Dashboard']

    def __init__(self , d):
        self.d = d

    def Enter_Email(self , email):
        self.d.find_element(*LoginPage.Email_XPATH).clear()
        self.d.find_element(*LoginPage.Email_XPATH).send_keys(email)

    def Enter_Password(self , password):
        self.d.find_element(*LoginPage.Password_XPATH).clear()
        self.d.find_element(*LoginPage.Password_XPATH).send_keys(password)

    def Click_On_LoginButton(self):
        self.d.find_element(*LoginPage.LoginButton_XPATH).click()

    def Click_On_LogoutButton(self):
        time.sleep(2)
        self.d.find_element(*LoginPage.Logout_XPATH).click()

    def Login_Status(self):
        try:
            self.d.find_element(*LoginPage.Login_Success_XPATH)
            return True
        except NoSuchElementException:
            return False
