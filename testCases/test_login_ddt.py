import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = "C:/Users/vinay/PycharmProjects/PythonWithSelenium/TestData/LoginData.xlsx"
    #username = ReadConfig.getUseremail()
    #password = ReadConfig.getPassword()
    logger = LogGen.loggen()



    def test_login_ddt(self,setup):
        self.logger.info("*********** Test_002_DDT_Login ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("number of rows" , self.rows)
        last_status = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)


            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    time.sleep(3)
                    self.lp.clickLogOut()
                    last_status.append("Pass")
                elif self.exp == "Fail":
                    time.sleep(3)
                    self.lp.clickLogOut()
                    last_status.append("Fail")
            elif act_title != "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    last_status.append("Fail")
                elif self.exp == "Fail":
                    last_status.append("Pass")

        if "Fail" not in last_status:
            self.logger.info("Login DDT test pass............")
            self.driver.close()
            assert True

        else:
            self.logger.info("Login DDT Fail ...........")
            self.driver.close()
            assert False





