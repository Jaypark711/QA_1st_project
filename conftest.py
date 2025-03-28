# conftest.py
import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
<<<<<<< HEAD
=======
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from user_info import LOGIN_INFO, LOGIN_INFO_SECOND
>>>>>>> 2a219a8 (Merge pull request #24 from Jaypark711/feature/Jaeyun)

@pytest.fixture(scope="function")
def driver():
    
    
    # 크롬 옵션 설정
    chrome_options = Options()

    #도커 젠킨스 실행용 코드
    # chrome_options .add_argument("--headless")
    # chrome_options .add_argument("--no-sandbox")
    # chrome_options .add_argument("--disable-dev-shm-usage")

    # chrome_options.add_argument('--disable-dev-shm-usage')  # shared memory 문제 방지
    # chrome_options.add_argument('--disable-gpu')  # 가상환경에서 GPU 기능 비활성화
   
    # 드라이버 객체 생성
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
        # instantiate a Chrome browser and add the options



    driver.delete_all_cookies()
    #  대기시간 설정
    driver.implicitly_wait(5)
    
    yield driver 

    # 테스트가 끝나면 드라이버 종료
    driver.quit()


<<<<<<< HEAD
@pytest.fixture
def login():
    print("임시 기능입니다..")
    #로그인 픽스쳐를 만드는 공간
=======
    url = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[text()='로그인하기']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "username").send_keys(LOGIN_INFO["user_id"])
    driver.find_element(By.ID, "password").send_keys(LOGIN_INFO["user_password"] + Keys.ENTER)
    WebDriverWait(driver,3).until_not(EC.url_contains("signin")) #signin이 url에 없어질때까지 명시적 대기
    yield driver

@pytest.fixture
def login_driver_second(driver):

    url = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[text()='로그인하기']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "username").send_keys(LOGIN_INFO_SECOND["user_id"])
    driver.find_element(By.ID, "password").send_keys(LOGIN_INFO_SECOND["user_password"] + Keys.ENTER)
    WebDriverWait(driver,3).until_not(EC.url_contains("signin")) #signin이 url에 없어질때까지 명시적 대기
    yield driver
>>>>>>> 2a219a8 (Merge pull request #24 from Jaypark711/feature/Jaeyun)
