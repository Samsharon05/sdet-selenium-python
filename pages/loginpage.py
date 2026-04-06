from selenium.webdriver.common.by import By

class LoginPage:
    username=(By.XPATH,'//input[@placeholder="Username"]')
    password=(By.XPATH,'//input[@placeholder="Password"]')
    loginbutton=(By.XPATH,'//input[@id="login-button"]')
    