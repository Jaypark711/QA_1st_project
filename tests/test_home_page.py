import os 
import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("Rlogin_driver")
class TestHomePage:
    def setup_method(self) :
        """테스트 실행 전에 setup"""
        self.home_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/" 
        self.alone_button_xpath = "/html/body/div[1]/div[1]/main/section/div/div[1]/button[1]"
        self.alone_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone"
        self.together_button_xpath = "/html/body/div[1]/div[1]/main/section/div/div[1]/button[2]"
        self.together_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        self.team_button_xpath = "/html/body/div[1]/div[1]/main/section/div/div[1]/button[3]"
        self.team_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"
        self.recommendation_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation"

    
### 혼자 먹기 테스트 시작, 한식 > 중식 > 양식 순서로 실행 ###
# 1. 혼자 먹기 클릭 하기 (한식)
    def test_alone_korean_food_001(self,driver: WebDriver):
        """혼자 먹기 버튼 클릭"""
        try:
            
            alone_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.alone_button_xpath))
            )
            alone_button.click()

            print("혼자 먹기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            print(f"혼자 먹기 버튼을 찾을 수 없음: {e}")
            assert False
        except ElementNotInteractableException as e:
            print(f"혼자 먹기 버튼 클릭 실패: {e}")
            assert False

    def test_alone_korean_food_002(self, driver: WebDriver):
        """혼자 먹기 페이지 URL 확인"""
        self.test_alone_korean_food_001(driver)
        current_url = driver.current_url
        try:
            assert current_url == self.alone_url
            print("혼자 먹기 페이지에 정상적으로 이동했습니다.")
            
        except AssertionError:
            assert False , print(f"혼자 먹기 페이지 이동 실패! 현재 URL: {current_url}")
            assert False

# 2. 펼침 메뉴 > 한식 선택하기
    def test_alone_korean_food_003(self, driver: WebDriver):
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            self.test_alone_korean_food_002(driver)
            time.sleep(0.05)
            menu_category = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            assert False , print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
            assert False
        except ElementNotInteractableException as e:
            assert False , print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")
            assert False

    def test_alone_korean_food_004(self, driver: WebDriver):
        """'한식' 카테고리 선택하기"""
        try:
            self.test_alone_korean_food_003(driver)
            korean_food = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[2]"))
        ).click()
            print("한식 선택 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'한식'을 찾을 수 없음: {e}")
            assert False
        except ElementNotInteractableException as e:
            assert False , print(f"'한식' 요소 클릭 실패!: {e}")
            assert False

# 3. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def test_alone_korean_food_005(self, driver: WebDriver):
        """선택 완료 버튼을 눌러 한식 메뉴 추천 받기"""
        try:
            self.test_alone_korean_food_004(driver)
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"선택 완료 버튼 클릭 실패 : {e}")

# 4. 메뉴 추천 받은 후, 추천 수락하기
    def test_alone_korean_food_006(self, driver: WebDriver):
        """추천 메뉴 확인"""
        self.test_alone_korean_food_005(driver)
        current_url = driver.current_url
        try:
            assert current_url == self.recommendation_url
            time.sleep(1)
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def test_alone_korean_food_007(self, driver: WebDriver):
        """추천 수락 버튼 클릭하기"""
        try:
            self.test_alone_korean_food_006(driver)
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            time.sleep(1)
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"추천 수락 버튼 클릭 실패 : {e}")

# 5. 다시 홈 탭으로 돌아가 다음 테스트 준비
    # def test_alone_korean_food_008(self):
    #     """홈 버튼 클릭하여 홈 페이지로 이동"""
    #     try:
    #         home_button = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a'))
    #         )
    #         home_button.click()
    #         time.sleep(1)
    #         print("홈 버튼 클릭 : PASS")
    #     except NoSuchElementException as e:
    #         assert False , print(f"홈 버튼을 찾을 수 없음: {e}")
    #     except ElementNotInteractableException as e:
    #         assert False , print(f"홈 버튼 클릭 실패: {e}")

    # def test_alone_korean_food_009(self):
    #     """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
    #     current_url = self.driver.current_url
    #     try:
    #         assert current_url == self.home_url
    #         print("홈 탭으로 정상적으로 이동했습니다.")
    #     except AssertionError:
    #         assert False , print(f"홈 탭 이동 실패! 현재 URL: {current_url}")
    #     time.sleep(1)
            
# 6. 혼자 먹기 클릭 하기 (중식)
    def test_alone_chinese_food_001(self, driver: WebDriver):
        """혼자 먹기 버튼 클릭"""
        try:
            alone_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.alone_button_xpath))
            )
            alone_button.click()
            
            print("혼자 먹기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"혼자 먹기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"혼자 먹기 버튼 클릭 실패: {e}")

    def test_alone_chinese_food_002(self, driver: WebDriver):
        
        self.test_alone_chinese_food_001(driver)
        try:
            
            """혼자 먹기 페이지 URL 확인"""
            current_url = driver.current_url
            assert current_url == self.alone_url
            print("혼자 먹기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"혼자 먹기 페이지 이동 실패! 현재 URL: {current_url}")

# 7. 펼침 메뉴 > 중식 선택하기
    def test_alone_chinese_food_003(self, driver: WebDriver):
        self.test_alone_chinese_food_002(driver)
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            time.sleep(0.05)
            menu_category = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            assert False , print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")

    def test_alone_chinese_food_004(self, driver: WebDriver):
        self.test_alone_chinese_food_003(driver)
        """'중식' 카테고리 선택하기"""
        try:
            korean_food = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[3]"))
        ).click()
            
            print("중식 선택 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'중식'을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"'중식' 클릭 실패!: {e}")

# 8. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def test_alone_chinese_food_005(self, driver: WebDriver):
        self.test_alone_chinese_food_004(driver)
        """선택 완료 버튼을 눌러 중식 메뉴 추천 받기"""
        try:
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"선택 완료 버튼 클릭 실패 : {e}")

# 9. 메뉴 추천 받은 후, 추천 수락하기
    def test_alone_chinese_food_006(self, driver: WebDriver):
        self.test_alone_chinese_food_005(driver)
        """추천 메뉴 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.recommendation_url
            
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def test_alone_chinese_food_007(self, driver: WebDriver):
        self.test_alone_chinese_food_006(driver)
        """추천 수락 버튼 클릭하기"""
        try:
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"추천 수락 버튼 클릭 실패 : {e}")

# 10. 다시 홈 탭으로 돌아가 다음 테스트 준비
    # def test_alone_chinese_food_008(self, driver: WebDriver):
    #     """홈 버튼 클릭하여 홈 페이지로 이동"""
    #     try:
    #         home_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a'))
    #         )
    #         home_button.click()
    #         time.sleep(1)
    #         print("홈 버튼 클릭 : PASS")
    #     except NoSuchElementException as e:
    #         assert False , print(f"홈 버튼을 찾을 수 없음: {e}")
    #     except ElementNotInteractableException as e:
    #         assert False , print(f"홈 버튼 클릭 실패: {e}")

    # def test_alone_chinese_food_009(self, driver: WebDriver):
    #     """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
    #     current_url = driver.current_url
    #     try:
    #         assert current_url == self.home_url
    #         print("홈 탭으로 정상적으로 이동했습니다.")
    #     except AssertionError:
    #         assert False , print(f"홈 탭 이동 실패! 현재 URL: {current_url}")
    #     time.sleep(1)

# 11. 혼자 먹기 클릭 하기 (양식)
    def test_alone_western_food_001(self, driver: WebDriver):
        
        """혼자 먹기 버튼 클릭"""
        try:
            alone_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.alone_button_xpath))
            )
            alone_button.click()
            print("혼자 먹기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"혼자 먹기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"혼자 먹기 버튼 클릭 실패: {e}")

    def test_alone_western_food_002(self, driver: WebDriver):
        self.test_alone_western_food_001(driver)
        """혼자 먹기 페이지 URL 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.alone_url
            print("혼자 먹기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"혼자 먹기 페이지 이동 실패! 현재 URL: {current_url}")

# 12. 펼침 메뉴 > 양식 선택하기
    def test_alone_western_food_003(self, driver: WebDriver):
        self.test_alone_western_food_002(driver)
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            time.sleep(0.05)
            menu_category = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            assert False , print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")

    def test_alone_western_food_004(self, driver: WebDriver):
        self.test_alone_western_food_003(driver)
        """'양식' 카테고리 선택하기"""
        try:
            korean_food = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[4]"))
        ).click()
            
            print("양식 선택 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'양식'을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"'양식' 클릭 실패!: {e}")

# 13. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def test_alone_western_food_005(self, driver: WebDriver):
        self.test_alone_western_food_004(driver)
        """선택 완료 버튼을 눌러 양식 메뉴 추천 받기"""
        try:
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"선택 완료 버튼 클릭 실패 : {e}")

# 14. 메뉴 추천 받은 후, 추천 수락하기
    def test_alone_western_food_006(self, driver: WebDriver):
        self.test_alone_western_food_005(driver)
        """추천 메뉴 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.recommendation_url
            
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def test_alone_western_food_007(self, driver: WebDriver):
        self.test_alone_western_food_006(driver)
        """추천 수락 버튼 클릭하기"""
        try:
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"추천 수락 버튼 클릭 실패 : {e}")

# 15. 다시 홈 탭으로 돌아가 다음 테스트 준비
    # def test_alone_western_food_008(self, driver: WebDriver):
    #     """홈 버튼 클릭하여 홈 페이지로 이동"""
    #     try:
    #         home_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a'))
    #         )
    #         home_button.click()
    #         time.sleep(1)
    #         print("홈 버튼 클릭 : PASS")
    #     except NoSuchElementException as e:
    #         assert False , print(f"홈 버튼을 찾을 수 없음: {e}")
    #     except ElementNotInteractableException as e:
    #         assert False , print(f"홈 버튼 클릭 실패: {e}")

    # def test_alone_western_food_009(self, driver: WebDriver):
    #     """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
    #     current_url = driver.current_url
    #     try:
    #         assert current_url == self.home_url
    #         print("홈 탭으로 정상적으로 이동했습니다.")
    #     except AssertionError:
    #         assert False , print(f"홈 탭 이동 실패! 현재 URL: {current_url}")
    #     time.sleep(1)

### 혼자 먹기 테스트 종료 ###
### 같이 먹기 테스트 시작, 일식 > 분식 > 아시안 순서로 실행 ###

# 1. 같이 먹기 클릭 하기 (일식)
    def test_togehter_japanese_food_001(self, driver: WebDriver):
        """같이 먹기 버튼 클릭"""
        try:
            together_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.together_button_xpath))
            )
            together_button.click()
            time.sleep(2)
            print("같이 먹기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"같이 먹기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"같이 먹기 버튼 클릭 실패: {e}")

    def test_togehter_japanese_food_002(self, driver: WebDriver):
        self.test_togehter_japanese_food_001(driver)
        """같이 먹기 페이지 URL 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.together_url
            print("같이 먹기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"같이 먹기 페이지 이동 실패! 현재 URL: {current_url}")

# 2. 펼침 메뉴 > 일식 선택하기
    def test_togehter_japanese_food_003(self, driver: WebDriver):
        self.test_togehter_japanese_food_002(driver)
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            time.sleep(0.05)
            menu_category = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            assert False , print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")

    def test_togehter_japanese_food_004(self, driver: WebDriver):
        self.test_togehter_japanese_food_003(driver)
        """'일식' 카테고리 선택하기"""
        try:
            japanese_food = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[5]"))
        ).click()
            
            print("일식 선택 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'일식'을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"'일식' 요소 클릭 실패!: {e}")

# 3. 같이 먹을 사람 선택하기
    def test_togehter_japanese_food_005(self, driver: WebDriver):
        self.test_togehter_japanese_food_004(driver)
        """첫번째 멤버 선택하기"""
        try:
            member_one = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[2]/div[4]/div[1]/input'))
            )
            member_one.click()
            
            print("첫번째 멤버가 선택되었습니다.")
        except NoSuchElementException as e:
            assert False , print(f"해당 멤버를 찾지 못했습니다. : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"해당 멤버를 선택하지 못했습니다. : {e}")

    def test_togehter_japanese_food_006(self, driver: WebDriver):
        self.test_togehter_japanese_food_005(driver)
        """강호동 검색해서 선택하기"""
        try:
            # 검색 입력창 선택
            search_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='이름을 검색해주세요']")
                )
            )
            search_field.send_keys("강호동")  # 검색어 입력
            
            search_field.send_keys(Keys.RETURN)  # 검색 실행
            # 검색 결과에서 "강호동" 멤버 선택
            click_member_two = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[2]/div[3]/ul/li/div'))
            )
            click_member_two.click()
            
            print("멤버가 선택되었습니다.")
        except NoSuchElementException as e:
            assert False , print(f"해당 멤버를 찾지 못했습니다. : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"해당 멤버를 선택하지 못했습니다. : {e}")

# 4. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def test_togehter_japanese_food_007(self, driver: WebDriver):
        self.test_togehter_japanese_food_006(driver)
        """선택 완료 버튼을 눌러 일식 메뉴 추천 받기"""
        try:
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"선택 완료 버튼 클릭 실패 : {e}")

# 5. 메뉴 추천 받은 후, 추천 수락하기
    def test_togehter_japanese_food_008(self, driver: WebDriver):
        self.test_togehter_japanese_food_007(driver)
        """추천 메뉴 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.recommendation_url
            
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def test_togehter_japanese_food_009(self, driver: WebDriver):
        self.test_togehter_japanese_food_008(driver)
        """추천 수락 버튼 클릭하기"""
        try:
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"추천 수락 버튼 클릭 실패 : {e}")

# 6. 다시 홈 탭으로 돌아가 다음 테스트 준비
    # def test_togehter_japanese_food_010(self, driver: WebDriver):
    #     """홈 버튼 클릭하여 홈 페이지로 이동"""
    #     try:
    #         home_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a'))
    #         )
    #         home_button.click()
    #         time.sleep(1)
    #         print("홈 버튼 클릭 : PASS")
    #     except NoSuchElementException as e:
    #         assert False , print(f"홈 버튼을 찾을 수 없음: {e}")
    #     except ElementNotInteractableException as e:
    #         assert False , print(f"홈 버튼 클릭 실패: {e}")

    # def test_togehter_japanese_food_011(self, driver: WebDriver):
    #     """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
    #     current_url = driver.current_url
    #     try:
    #         assert current_url == self.home_url
    #         print("홈 탭으로 정상적으로 이동했습니다.")
    #     except AssertionError:
    #         assert False , print(f"홈 탭 이동 실패! 현재 URL: {current_url}")
    #     time.sleep(1)
            
# 7. 같이 먹기 클릭 하기 (분식)
    def test_togehter_street_food_001(self, driver: WebDriver):
        """같이 먹기 버튼 클릭"""
        try:
            together_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.together_button_xpath))
            )
            together_button.click()
            
            print("같이 먹기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"같이 먹기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"같이 먹기 버튼 클릭 실패: {e}")

    def test_togehter_street_food_002(self, driver: WebDriver):
        self.test_togehter_street_food_001(driver)
        """같이 먹기 페이지 URL 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.together_url
            print("같이 먹기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"같이 먹기 페이지 이동 실패! 현재 URL: {current_url}")

# 8. 펼침 메뉴 > 분식 선택하기
    def test_togehter_street_food_003(self, driver: WebDriver):
        self.test_togehter_street_food_002(driver)
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            time.sleep(0.05)
            menu_category = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            assert False , print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")

    def test_togehter_street_food_004(self, driver: WebDriver):
        self.test_togehter_street_food_003(driver)
        """'분식' 카테고리 선택하기"""
        try:
            street_food = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[6]"))
        ).click()
            
            print("분식 선택 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'분식'을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"'분식' 요소 클릭 실패!: {e}")

# 9. 같이 먹을 사람 선택하기
    def test_togehter_street_food_005(self, driver: WebDriver):
        self.test_togehter_street_food_004(driver)
        """첫번째 멤버 선택하기"""
        try:
            member_one = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[2]/div[4]/div[1]/input'))
            )
            member_one.click()
            
            print("첫번째 멤버가 선택되었습니다.")
        except NoSuchElementException as e:
            assert False , print(f"해당 멤버를 찾지 못했습니다. : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"해당 멤버를 선택하지 못했습니다. : {e}")

    def test_togehter_street_food_006(self, driver: WebDriver):
        self.test_togehter_street_food_005(driver)
        """유재석 검색해서 선택하기"""
        try:
            # 검색 입력창 선택
            search_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='이름을 검색해주세요']")
                )
            )
            search_field.send_keys("유재석")  # 검색어 입력
            
            search_field.send_keys(Keys.RETURN)  # 검색 실행
            
            # 검색 결과에서 "유재석" 멤버 선택
            click_member_two = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[2]/div[3]/ul/li/div'))
            )
            click_member_two.click()
            
            print("멤버가 선택되었습니다.")
        except NoSuchElementException as e:
            assert False , print(f"해당 멤버를 찾지 못했습니다. : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"해당 멤버를 선택하지 못했습니다. : {e}")

# 10. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def test_togehter_street_food_007(self, driver: WebDriver):
        self.test_togehter_street_food_006(driver)
        """선택 완료 버튼을 눌러 분식 메뉴 추천 받기"""
        try:
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            time.sleep(1)
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"선택 완료 버튼 클릭 실패 : {e}")

# 11. 메뉴 추천 받은 후, 추천 수락하기
    def test_togehter_street_food_008(self, driver: WebDriver):
        self.test_togehter_street_food_007(driver)
        """추천 메뉴 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.recommendation_url
            
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def test_togehter_street_food_009(self, driver: WebDriver):
        self.test_togehter_street_food_008(driver)
        """추천 수락 버튼 클릭하기"""
        try:
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"추천 수락 버튼 클릭 실패 : {e}")

# 12. 다시 홈 탭으로 돌아가 다음 테스트 준비
    # def test_togehter_street_food_010(self, driver: WebDriver):
    #     """홈 버튼 클릭하여 홈 페이지로 이동"""
    #     try:
    #         home_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a'))
    #         )
    #         home_button.click()
    #         time.sleep(1)
    #         print("홈 버튼 클릭 : PASS")
    #     except NoSuchElementException as e:
    #         assert False , print(f"홈 버튼을 찾을 수 없음: {e}")
    #     except ElementNotInteractableException as e:
    #         assert False , print(f"홈 버튼 클릭 실패: {e}")

    # def test_togehter_street_food_011(self, driver: WebDriver):
    #     """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
    #     current_url = driver.current_url
    #     try:
    #         assert current_url == self.home_url
    #         print("홈 탭으로 정상적으로 이동했습니다.")
    #     except AssertionError:
    #         assert False , print(f"홈 탭 이동 실패! 현재 URL: {current_url}")
    #     time.sleep(1)

# 13. 같이 먹기 클릭 하기 (아시안)
    def test_togehter_asian_food_001(self, driver: WebDriver):
        """같이 먹기 버튼 클릭"""
        try:
            together_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.together_button_xpath))
            )
            together_button.click()
            
            print("같이 먹기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"같이 먹기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"같이 먹기 버튼 클릭 실패: {e}")

    def test_togehter_asian_food_002(self, driver: WebDriver):
        self.test_togehter_asian_food_001(driver)
        """같이 먹기 페이지 URL 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.together_url
            print("같이 먹기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"같이 먹기 페이지 이동 실패! 현재 URL: {current_url}")

# 14. 펼침 메뉴 > 아시안 선택하기
    def test_togehter_asian_food_003(self, driver: WebDriver):
        self.test_togehter_asian_food_002(driver)
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            time.sleep(0.05)
            menu_category = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            assert False , print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")

    def test_togehter_asian_food_004(self, driver: WebDriver):
        self.test_togehter_asian_food_003(driver)
        """'아시안' 카테고리 선택하기"""
        try:
            asian_food = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[7]"))
        ).click()
            
            print("아시안 선택 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'아시안'을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"'아시안' 요소 클릭 실패!: {e}")

# 15. 같이 먹을 사람 선택하기
    def test_togehter_asian_food_005(self, driver: WebDriver):
        self.test_togehter_asian_food_004(driver)
        """첫번째 멤버 선택하기"""
        try:
            member_one = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[2]/div[4]/div[1]/input'))
            )
            member_one.click()
            
            print("첫번째 멤버가 선택되었습니다.")
        except NoSuchElementException as e:
            assert False , print(f"해당 멤버를 찾지 못했습니다. : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"해당 멤버를 선택하지 못했습니다. : {e}")

    def test_togehter_asian_food_006(self, driver: WebDriver):
        self.test_togehter_asian_food_005(driver)
        """김보민 검색해서 선택하기"""
        try:
            # 검색 입력창 선택
            search_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='이름을 검색해주세요']")
                )
            )
            search_field.send_keys("김보민")  # 검색어 입력
            
            search_field.send_keys(Keys.RETURN)  # 검색 실행
            
            # 검색 결과에서 "김보민" 멤버 선택
            click_member_two = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[2]/div[3]/ul/li/div'))
            )
            click_member_two.click()
            
            print("멤버가 선택되었습니다.")
        except NoSuchElementException as e:
            assert False , print(f"해당 멤버를 찾지 못했습니다. : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"해당 멤버를 선택하지 못했습니다. : {e}")

# 16. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def test_togehter_asian_food_007(self, driver: WebDriver):
        self.test_togehter_asian_food_006(driver)
        """선택 완료 버튼을 눌러 아시안 메뉴 추천 받기"""
        try:
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"선택 완료 버튼 클릭 실패 : {e}")

# 17. 메뉴 추천 받은 후, 추천 수락하기
    def test_togehter_asian_food_008(self, driver: WebDriver):
        self.test_togehter_asian_food_007(driver)
        """추천 메뉴 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.recommendation_url
            
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def test_togehter_asian_food_009(self, driver: WebDriver):
        self.test_togehter_asian_food_008(driver)
        """추천 수락 버튼 클릭하기"""
        try:
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"추천 수락 버튼 클릭 실패 : {e}")

# 18. 다시 홈 탭으로 돌아가 다음 테스트 준비
    # def test_togehter_asian_food_010(self, driver: WebDriver):
    #     """홈 버튼 클릭하여 홈 페이지로 이동"""
    #     try:
    #         home_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a'))
    #         )
    #         home_button.click()
    #         time.sleep(1)
    #         print("홈 버튼 클릭 : PASS")
    #     except NoSuchElementException as e:
    #         assert False , print(f"홈 버튼을 찾을 수 없음: {e}")
    #     except ElementNotInteractableException as e:
    #         assert False , print(f"홈 버튼 클릭 실패: {e}")

    # def test_togehter_asian_food_011(self, driver: WebDriver):
    #     """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
    #     current_url = driver.current_url
    #     try:
    #         assert current_url == self.home_url
    #         print("홈 탭으로 정상적으로 이동했습니다.")
    #     except AssertionError:
    #         assert False , print(f"홈 탭 이동 실패! 현재 URL: {current_url}")
    #     time.sleep(1)

### 같이 먹기 테스트 종료 ###
### 회식하기 테스트 시작, 패스트푸드 > 기타 순서로 실행 ###

# 1. 회식하기 클릭 하기 (패스트푸드)
    def test_team_fast_food_001(self, driver: WebDriver):
        """회식하기 버튼 클릭"""
        try:
            team_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.team_button_xpath))
            )
            team_button.click()
            
            print("회식하기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"회식하기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"회식하기 버튼 클릭 실패: {e}")

    def test_team_fast_food_002(self, driver: WebDriver):
        self.test_team_fast_food_001(driver)
        """회식하기 페이지 URL 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.team_url
            print("회식하기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"회식하기 페이지 이동 실패! 현재 URL: {current_url}")

# 2. 펼침 메뉴 > 패스트푸드 선택하기
    def test_team_fast_food_003(self, driver: WebDriver):
        self.test_team_fast_food_002(driver)
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            time.sleep(0.05)
            menu_category = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            assert False , print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")

    def test_team_fast_food_004(self, driver: WebDriver):
        self.test_team_fast_food_003(driver)
        """'패스트푸드' 카테고리 선택하기"""
        try:
            fast_food = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[8]"))
        ).click()
            
            print("패스트푸드 선택 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'패스트푸드'을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"'패스트푸드' 요소 클릭 실패!: {e}")

# 3. 팀 요소 확인 하기
    def test_team_fast_food_005(self, driver: WebDriver):
        self.test_team_fast_food_004(driver)
        """개발 1팀 선택 여부 확인"""
        try:
            team_one = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '개발 1팀')]"))
            )
            displayd_team = team_one.text
            assert displayd_team == "개발 1팀", f"'개발 1팀'이 포함되지 않았습니다.: {displayd_team}"
            
            print("개발 1팀이 정상적으로 포함되었습니다. : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'개발 1팀' 텍스트 요소를 찾을 수 없음: {e}")
        except AssertionError as e:
            assert False , print(f"텍스트 확인 실패: {e}")

# 4. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def test_team_fast_food_006(self, driver: WebDriver):
        self.test_team_fast_food_005(driver)
        """선택 완료 버튼을 눌러 패스트푸드 메뉴 추천 받기"""
        try:
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"선택 완료 버튼 클릭 실패 : {e}")

# 5. 메뉴 추천 받은 후, 추천 수락하기
    def test_team_fast_food_007(self, driver: WebDriver):
        self.test_team_fast_food_006(driver)
        """추천 메뉴 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.recommendation_url
            
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def test_team_fast_food_008(self, driver: WebDriver):
        self.test_team_fast_food_007(driver)
        """추천 수락 버튼 클릭하기"""
        try:
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"추천 수락 버튼 클릭 실패 : {e}")

# 6. 다시 홈 탭으로 돌아가 다음 테스트 준비
    # def test_team_fast_food_009(self, driver: WebDriver):
    #     """홈 버튼 클릭하여 홈 페이지로 이동"""
    #     try:
    #         home_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a'))
    #         )
    #         home_button.click()
    #         time.sleep(1)
    #         print("홈 버튼 클릭 : PASS")
    #     except NoSuchElementException as e:
    #         assert False , print(f"홈 버튼을 찾을 수 없음: {e}")
    #     except ElementNotInteractableException as e:
    #         assert False , print(f"홈 버튼 클릭 실패: {e}")

    # def test_team_fast_food_010(self, driver: WebDriver):
    #     """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
    #     current_url = driver.current_url
    #     try:
    #         assert current_url == self.home_url
    #         print("홈 탭으로 정상적으로 이동했습니다.")
    #     except AssertionError:
    #         assert False , print(f"홈 탭 이동 실패! 현재 URL: {current_url}")
    #     time.sleep(1)

# 7. 회식하기 클릭 하기 (기타)
    def test_team_others_food_001(self, driver: WebDriver):
        """회식하기 버튼 클릭"""
        try:
            team_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.team_button_xpath))
            )
            team_button.click()
            
            print("회식하기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"회식하기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"회식하기 버튼 클릭 실패: {e}")

    def test_team_others_food_002(self, driver: WebDriver):
        self.test_team_others_food_001(driver)
        """회식하기 페이지 URL 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.team_url
            print("회식하기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"회식하기 페이지 이동 실패! 현재 URL: {current_url}")

# 8. 펼침 메뉴 > 기타 선택하기
    def test_team_others_food_003(self, driver: WebDriver):
        self.test_team_others_food_002(driver)
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            time.sleep(0.05)
            menu_category = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            assert False , print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")

    def test_team_others_food_004(self, driver: WebDriver):
        self.test_team_others_food_003(driver)
        """'기타' 카테고리 선택하기"""
        try:
            others_food = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[9]"))
        ).click()
            
            print("기타 선택 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'기타'을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"'기타' 요소 클릭 실패!: {e}")

# 9. 팀 요소 확인 하기
    def test_team_others_food_005(self, driver: WebDriver):
        self.test_team_others_food_004(driver)
        """개발 1팀 선택 여부 확인"""
        try:
            team_one = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '개발 1팀')]"))
            )
            displayd_team = team_one.text
            assert displayd_team == "개발 1팀", f"'개발 1팀'이 포함되지 않았습니다.: {displayd_team}"
            
            print("개발 1팀이 정상적으로 포함되었습니다. : PASS")
        except NoSuchElementException as e:
            assert False , print(f"'개발 1팀' 텍스트 요소를 찾을 수 없음: {e}")
        except AssertionError as e:
            assert False , print(f"텍스트 확인 실패: {e}")

# 10. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def test_team_others_food_006(self, driver: WebDriver):
        self.test_team_others_food_005(driver)
        """선택 완료 버튼을 눌러 기타 메뉴 추천 받기"""
        try:
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"선택 완료 버튼 클릭 실패 : {e}")

# 11. 메뉴 추천 받은 후, 추천 수락하기
    def test_team_others_food_007(self, driver: WebDriver):
        self.test_team_others_food_006(driver)
        """추천 메뉴 확인"""
        current_url = driver.current_url
        try:
            assert current_url == self.recommendation_url
            
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            assert False , print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def test_team_others_food_008(self, driver: WebDriver):
        self.test_team_others_food_007(driver)
        """추천 수락 버튼 클릭하기"""
        try:
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            assert False , print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            assert False , print(f"추천 수락 버튼 클릭 실패 : {e}")

# 12. 다시 홈 탭으로 돌아가 다음 테스트 준비
    # def test_team_others_food_009(self, driver: WebDriver):
    #     """홈 버튼 클릭하여 홈 페이지로 이동"""
    #     try:
    #         home_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[1]/a'))
    #         )
    #         home_button.click()
    #         time.sleep(1)
    #         print("홈 버튼 클릭 : PASS")
    #     except NoSuchElementException as e:
    #         assert False , print(f"홈 버튼을 찾을 수 없음: {e}")
    #     except ElementNotInteractableException as e:
    #         assert False , print(f"홈 버튼 클릭 실패: {e}")

    # def test_team_others_food_010(self, driver: WebDriver):
    #     """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
    #     current_url = driver.current_url
    #     try:
    #         assert current_url == self.home_url
    #         print("홈 탭으로 정상적으로 이동했습니다.")
    #     except AssertionError:
    #         assert False , print(f"홈 탭 이동 실패! 현재 URL: {current_url}")
    #     time.sleep(1)

### 회식하기 테스트 종료 ###        

### 홈 > 메뉴 추천 확인 테스트 ###
    def test_menu_canvas(self, driver: WebDriver):
        """캔버스 정상 출력확인"""
        try:
            canvas = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'canvas'))
            )
            canvas.click()

        except NoSuchElementException as e:
            assert False , print(f"요소를 찾을 수 없습니다.: {e}")
            
        except AssertionError as e:
            assert False , print(f"요소 확인 실패: {e}")

    def test_menu_recommendation(self, driver: WebDriver):
        """메뉴 추천 화면이 정상 노출되는지 확인"""
        try:
            recommend_menu = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'text-lg font-semibold')]"))
            )
            element_text = recommend_menu.text
            assert '오늘 점심은' in element_text, "점심 메뉴 추천 텍스트가 노출되지 않습니다."
            assert '어떠세요?' in element_text, "점심 메뉴 추천 텍스트가 노출되지 않습니다."
            
            print("점심 메뉴 추천 텍스트가 노출되고 있습니다.")
        except NoSuchElementException as e:
            assert False , print(f"텍스트 요소를 찾을 수 없습니다.: {e}")
            
        except AssertionError as e:
            assert False , print(f"텍스트 확인 실패: {e}")

### 나의 취향 분석은 아무 것도 나오지 않아 확인 제외, 테스트 종료 ###