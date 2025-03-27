#history_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import os 

class HistoryPage:
    URL = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def is_displayed(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def texts(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return [el.text for el in elements]

    def menu_list(self):
        result = []
        boxes = self.driver.find_elements(*self.menu_box_locator)
        for box in boxes:
            main = box.find_element(*self.main_category_locator).text
            sub = box.find_element(*self.sub_category_locator).text
            name = box.find_element(*self.menu_name_locator).text
            score = box.find_element(*self.score_locator).text
            result.append([main, sub, name, score])
        return result

    #히스토리 탭 진입 버튼
    history_btn = (By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[3]/a')
    #GNB 영역
    back_btn = (By.CLASS_NAME,'cursor-pointer')
    GNB_history = (By.XPATH,'//*[@id="root"]/div[1]/header/div/span')
    #히스토리탭 영역
    history_title = (By.XPATH,'//*[@id="root"]/div[1]/main/section/section/span')
    review_register_btn = (By.XPATH, '//button[normalize-space()="추천 후기 등록하기"]') 
    #히스토리탭 - 메뉴 박스 영역
    menu_box_locator = (By.XPATH, "//div[@class='flex w-full gap-6 p-4 shadow-md rounded-2xl']")
    main_category_locator = (By.XPATH, ".//div[contains(@class, 'bg-main')]")
    sub_category_locator = (By.XPATH, ".//div[contains(@class, 'bg-sub')]")
    menu_name_locator = (By.XPATH, ".//div[@class='font-bold']")
    score_locator = (By.CSS_SELECTOR, "span.font-bold.text-sub-2.text-subbody")

    #리뷰탭
    review_tab = (By.XPATH,'//*[@id="modal-root"]/div')
    #리뷰탭 - GNB 영역
    GNB_review = (By.XPATH,'//*[@id="modal-root"]/div/div[1]/span')
    GNB_review_back_btn = (By.XPATH,'//*[@id="modal-root"]/div/div[1]/button')
    #리뷰탭 - 식사 유형
    eat_alone = (By.XPATH, "//label[@for='혼밥']")
    eat_group = (By.XPATH, "//label[@for='그룹']")
    eat_together = (By.XPATH, "//label[@for='회식']")
    #리뷰탭 - 후기 사진
    review_img = (By.XPATH, ".//div[contains(@class, 'w-24 h-24')]")
    review_img_btn = (By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/button')
    review_img_input = (By.NAME, 'reviewImg')
    image_path = os.path.abspath('utils/망글곰.png')

    #리뷰탭 - 메뉴 명

    #리뷰탭 - 카테고리
    review_comment = (By.NAME, 'comment')




    