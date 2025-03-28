# 테스트에 필요한 함수를 동작할 수 있게 하는 Selenium 모듈 불러오기 (이건 test 문서가 아니므로 pytest는 필요 없음)
from selenium.webdriver.chrome.webdriver import WebDriver # 테스트를 크롬으로 실행
from selenium.webdriver.common.by import By # 경로를 가져올 때 쓰기 위함
from selenium.webdriver.common.keys import Keys # 같이 먹기 검색할 때 글자 입력 용으로 쓰기 위함
from selenium.webdriver.support.ui import Select # 드롭다운 메뉴에서 선택할 때 쓰기 위함
from selenium.webdriver.support.ui import WebDriverWait # 페이지가 로딩될 때까지 대기하기 위함
# 예외처리
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
#pages 파일에 작성한 TestHomePage의 함수들 불러오기
from pages.home_page import TestHomePage
import pytest
import time


# pytest.mark.usefixtures("login_driver")는 테스트 케이스 실행 전 login_driver라는 fixture를 사용하겠다는 의미이다.
@pytest.mark.usefixtures("login_driver")
# @pytest.mark.skip(skip 사유 적기)

#홈 페이지의 클래스 아래의 함수들을 테스트 시도
class TestHomePage:
    category_xpath= {"한식" : "/html/body/div[3]/div/div/div/div[2]",
                     "중식" : "/html/body/div[3]/div/div/div/div[3]",
                     "양식" : "/html/body/div[3]/div/div/div/div[4]",
                     "일식" : "/html/body/div[3]/div/div/div/div[5]",
                     "분식" : "/html/body/div[3]/div/div/div/div[6]",
                     "아시안" : "/html/body/div[3]/div/div/div/div[7]",
                     "패스트푸드" : "/html/body/div[3]/div/div/div/div[8]",
                     "기타" : "/html/body/div[3]/div/div/div/div[9]"}

    # 혼자 먹기의 기능 테스트 (한식)
    def test_eat_alone_korea_001(self):
        '''한식 혼자 먹기 기능 테스트 시작'''
        try:
            # 혼자 먹기 시도를 위해 우선 홈 화면으로 이동함
            enter_homepage = self.URL
            self.driver.get(enter_homepage) # 홈 페이지로 이동
            time.sleep(1)
            # 혼자 먹기 버튼 클릭 시도
            find_alone_btn = self.alone_btn() # 혼자 먹기 버튼 찾기
            find_alone_btn.click() # 혼자 먹기 버튼 클릭
            assert self.driver.current_url == self.alone_url # 혼자 먹기 페이지로 이동했는지 확인
        except NoSuchElementException as e:
            assert False, "혼자 먹기 버튼을 찾을 수 없습니다."




