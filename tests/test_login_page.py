import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

@pytest.mark.skip
@pytest.mark.usefixtures("driver")
class TestLoginPage:
    @pytest.mark.skip
    def test_login_TC001(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            login_page.open()
            #페이지 로딩
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("signin"))
            assert "signin" in driver.current_url
            #로그인 버튼 클릭
            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"로그인")]')
            button.click()
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url
            login_page.login("qwer1@qwer.qwer","qwerQWER1!")
            
            time.sleep(2)
        except NoSuchElementException as e:
            assert False
    @pytest.mark.skip
    def test_login_TC002_err(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            login_page.open()
            #페이지 로딩
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("signin"))
            assert "signin" in driver.current_url
            #로그인 버튼 클릭
            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"로그인")]')
            button.click()
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url
            #비밀번호 틀림
            login_page.login("qwer1@qwer.qwer","1234")
            
            time.sleep(2)
        except NoSuchElementException as e:
            assert False
    @pytest.mark.skip
    def test_login_TC003_err(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            login_page.open()
            #페이지 로딩
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("signin"))
            assert "signin" in driver.current_url
            #로그인 버튼 클릭
            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"로그인")]')
            button.click()
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url
            #아이디 틑림
            login_page.login("qwer.qwer","qwerQWER1!")
            
            time.sleep(2)
        except NoSuchElementException as e:
            assert False

    @pytest.mark.skip
    def test_signup_TC001(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            #페이지 로딩
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("signin"))
            assert "signin" in driver.current_url
            #로그인 버튼 클릭
            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"회원가입")]')
            button.click()
            wait.until(EC.url_contains("u/signup"))
            assert "u/signup" in driver.current_url
            #정상회원가입
            login_page.signup("qwer3@qwer.qwer","qwerQWER1!")
            
            time.sleep(5)
        except NoSuchElementException as e:
            assert False
    
    @pytest.mark.skip
    def test_signup_TC002(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            #페이지 로딩
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("signin"))
            assert "signin" in driver.current_url
            #로그인 버튼 클릭
            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"회원가입")]')
            button.click()
            wait.until(EC.url_contains("u/signup"))
            assert "u/signup" in driver.current_url
            #이미 있는 이메일
            login_page.signup("qwer3@qwer.qwer","qwerQWER1!")
            
            time.sleep(5)
        except NoSuchElementException as e:
            assert False

    @pytest.mark.skip
    def test_signup_TC003(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            #페이지 로딩
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("signin"))
            assert "signin" in driver.current_url
            #로그인 버튼 클릭
            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"회원가입")]')
            button.click()
            wait.until(EC.url_contains("u/signup"))
            assert "u/signup" in driver.current_url
            #비밀번호 규칙 틀림
            login_page.signup("qwer3@qwer.qwer","QWER1!")
            
            time.sleep(5)
        except NoSuchElementException as e:
            assert False