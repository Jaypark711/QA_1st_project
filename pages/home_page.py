# 테스트에 필요한 함수를 동작할 수 있게 하는 Selenium 모듈 불러오기 (이건 test 문서가 아니므로 pytest는 필요 없음)
from selenium.webdriver.chrome.webdriver import WebDriver # 테스트를 크롬으로 실행
from selenium.webdriver.common.by import By # 경로를 가져올 때 쓰기 위함
from selenium.webdriver.common.keys import Keys # 같이 먹기 검색할 때 글자 입력 용으로 쓰기 위함
from selenium.webdriver.support.ui import Select # 드롭다운 메뉴에서 선택할 때 쓰기 위함
from selenium.webdriver.support.ui import WebDriverWait # 페이지가 로딩될 때까지 대기하기 위함
# 예외처리
from selenium.webdriver.support import expected_conditions as EC

#홈 페이지의 클래스 정의
class TestHomePage:
    # 홈 탭의 URL을 정의 (이 뒤에 혼자먹기, 같이먹기, 회식하기 경로가 추가됨)
    URL = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
    alone_url = URL+"selectoptions/alone"
    together_url = URL+"selectoptions/together" 
    team_url = URL+"selectoptions/team"
    reconmendation_url = URL+"recommendation"

    # init(self)는 초기화 initialize 메서드. 객체가 생성될 때, 자동으로 호출되는 메서드이며 객체의 초기값을 설정해야 할 때 사용한다.
    def __init__(self, driver: WebDriver):
        self.driver = driver

# 아래는 테스트에 사용할 Xpath 경로들
    # 혼자먹기, 같이먹기, 회식하기
    def alone_btn(self):
        return self. driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/section/div/div[1]/button[1]")
    def together_btn(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/section/div/div[1]/button[2]")
    def team_btn(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/section/div/div[1]/button[3]")
    
    # 메뉴 드롭다운 리스트
    def menu_cate(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')

    # 확인 버튼
    def confirm_btn(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/section/div/button')

    #추천수락 버튼
    def recommend_btn(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/section/section/button[2]')

    # 홈 버튼
    def home_btn(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a')