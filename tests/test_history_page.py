#test_history_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import time
import random
import pytest
from pages.history_page import HistoryPage
import os
from utils.image_is_similar import is_similar


'''
참고
menu_list의 출력 예시
[['회식', '기타', '랍스터롤', '44.0 %'], 
['회식', '패스트푸드', '머핀', '44.0 %'], 
['그룹', '아시안', '해물쌀국수', '53.0 %'], 
['그룹', '분식', '날치알김밥', '52.0 %'], 
['그룹', '일식', '다시마키타마고', '52.0 %'], 
['혼밥', '양식', '토르텔리니', '52.0 %'], 
['혼밥', '중식', '사천탕면', '53.0 %'], 
['혼밥', '한식', '동태탕', '52.0 %']]
'''



@pytest.mark.usefixtures("login_driver")
#@pytest.mark.skip()
class TestMyPage:

    category_list = [
    (0, "회식", "기타"),
    (1, "회식", "패스트푸드"),
    (2, "그룹", "아시안"),
    (3, "그룹", "분식"),
    (4, "그룹", "일식"),
    (5, "혼밥", "양식"),
    (6, "혼밥", "중식"),
    (7, "혼밥", "한식")]

    meal_type = ["혼밥", "그룹", "회식"]

    def navigate_to_history(self, driver):
        history_page = HistoryPage(driver)
        history_page.click(HistoryPage.history_btn)
        WebDriverWait(driver, 10).until(EC.url_contains("history"))
        return history_page

    @pytest.mark.skip()
    def test_history_001(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
        except Exception as e:
            print(f"히스토리 페이지 진입 테스트 실패")
            assert False

    @pytest.mark.skip()
    def test_history_002(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.back_btn)
            WebDriverWait(driver,10).until_not(EC.url_contains("history"))
            assert "history" != driver.current_url, "아직 history 탭에 남아있음"
        except Exception as e:
            print(f"뒤로가기 버튼 누르기 실패")
            assert False

    @pytest.mark.skip()

    def test_history_003(self, driver: WebDriver):

        try:
            history_page = self.navigate_to_history(driver)
            GNB_name = history_page.text(HistoryPage.GNB_history)
            assert GNB_name == "추천 히스토리" , "GNB 이름이 '추천 히스토리'가 아님"
        except Exception as e:
            print(f"GNB 이름 찾기 실패")
            assert False

    @pytest.mark.skip()
    def test_history_004(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            title = history_page.text(HistoryPage.history_title)
            assert "추천 받았던 메뉴들이에요!" in title , "추천 받았던 메뉴들이에요! 가 다르게 노출됨"
        except Exception as e:
            print(f"추천 받았던 메뉴들이에요! 가 미노출")
            assert False

    @pytest.mark.skip()
    def test_history_005(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            print(menu_list[0])
            assert len(menu_list) == 8 , "8개보다 적거나 많음"
        except Exception as e:
            print(f"메뉴들을 찾아내지 못함")
            assert False

    @pytest.mark.skip()
    @pytest.mark.parametrize("index, expected_main, expected_sub", category_list)
    def test_history_006_008_010_012_014_016_018_020(self,driver: WebDriver, index, expected_main, expected_sub):  #6,8,10,12,14,16,18,20번 TC
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            assert expected_main == menu_list[index][0], f"{index}번째 메인 카테고리가 다름"
            assert expected_sub == menu_list[index][1], f"{index}번째 서브 카테고리가 다름"
        except Exception as e:
            print(f"{index}번 오류: {e}")
            assert False

    @pytest.mark.skip()
    def test_history_022(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            
            btn = history_page.text(HistoryPage.review_register_btn)
            assert "추천 후기 등록" in btn, "추천 후기 등록 버튼 미노출"
        except Exception as e:
            print("추천 후기 등록하기 버튼 탐색 실패")
            assert False

    @pytest.mark.skip()
    def test_history_023(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_tab)
            assert result == True, "후기 등록 탭 미노출"
        except Exception as e:
            print("후기 등록 탭 탐색 실패")
            assert False

    @pytest.mark.skip()
    def test_history_024(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            review_title = history_page.text(HistoryPage.GNB_review)
            assert "후기 등록하기" in review_title, "후기 등록 GNB 미노출"
        except Exception as e:
            print("후기 등록하기 GNB 탐색 실패")
            assert False

    @pytest.mark.skip()
    def test_history_025(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            radio_alone = history_page.text(HistoryPage.eat_alone)
            radio_group = history_page.text(HistoryPage.eat_group)
            radio_together = history_page.text(HistoryPage.eat_together)
            print(radio_alone, radio_group, radio_together)
            assert radio_alone == "혼밥", "혼밥 라디오 버튼 미노출"
            assert radio_group == "그룹", "그룹 라디오 버튼 미노출"
            assert radio_together == "회식", "회식 라디오 버튼 미노출"
        except Exception as e:
            print("라디오 버튼 탐색 실패")
            assert False

    @pytest.mark.skip()
    def test_history_026(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_img_is_null)
            assert result == True, "이미지 영역에 무언가 들어있음"
        except Exception as e:
            print("이미지 영역 미노출")
            assert False

    @pytest.mark.skip()
    def test_history_027(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.send_keys(HistoryPage.review_img_input, HistoryPage.image_path)
            src = history_page.get_attribute(HistoryPage.review_img, "src")
            result = is_similar(src, HistoryPage.image_path)
            assert result > 0.9, "이미지가 다름"
        except Exception as e:
            print("이미지 비교 실패")
            assert False
        
    @pytest.mark.skip()
    def test_history_028(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            history_menu_name = menu_list[0][2]
            history_page.click(HistoryPage.review_register_btn)
            value = history_page.get_attribute(HistoryPage.review_menu, "value")
            assert history_menu_name == value, "히스토리 메뉴명과 후기 메뉴명이 다름"

        except Exception as e:
            print("히스토리 메뉴명 또는 후기 메뉴명 탐색 실패")
            assert False

    @pytest.mark.skip()
    def test_history_029(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_category)
            assert result == True, "카테고리 미노출"

        except Exception as e:
            print("카테고리 탐색 실패")
            assert False
    
    @pytest.mark.skip()
    def test_history_030(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_comment)
            assert result == True, "후기 입력란 감지 실패"

        except Exception as e:
            print("후기 입력란 탐색 실패")
            assert False
    
    @pytest.mark.skip()
    def test_history_031(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.get_attribute(HistoryPage.review_comment, "placeholder")
            assert "후기를 입력해주세요." in result, "후기 입력 placeholder이 다르게 노출됨"
        except Exception as e:
            print("후기 입력란 탐색 실패")
            assert False        

    @pytest.mark.skip()
    def test_history_032(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)

            lenth = len(history_page.texts(HistoryPage.review_star_gray))
            assert lenth == 5, "칠해지지 않은 별점 수가 5개가 아님"
        except Exception as e:
            print("별점 탐색 실패")
            assert False

    @pytest.mark.skip()
    def test_history_033(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.eat_alone_radio)
            result = history_page.get_attribute(HistoryPage.eat_alone_radio, "data-state")
            assert result == "unchecked", "혼밥 라디오 버튼이 선택됨"
            
        except Exception as e:
            print("라디오 버튼 탐색 실패")
            assert False


    #34번부터 41번까지는 테스트데이터 준비가 필요



    @pytest.mark.skip()
    def test_history_042(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            with pytest.raises(ElementNotInteractableException):
                history_page.send_keys(HistoryPage.review_menu, "123")
            
        except Exception as e:
            print("라디오 버튼 탐색 실패")
            assert False
    
    #@pytest.mark.skip()
    def test_history_043(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)

            history_page.send_keys(HistoryPage.review_comment, "123")
            result = history_page.get_attribute(HistoryPage.review_comment, "value")
            assert result == "124", print("val")
        except Exception as e:
            assert False