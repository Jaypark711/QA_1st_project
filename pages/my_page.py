#my_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import random
from selenium.webdriver import ActionChains
import os 

class MyPage:
    URL = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

    def element(self,by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))

    def elements(self,by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))

    def click(self, by_locator):
        # 요소가 클릭 가능할 때까지 기다림
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        # 요소가 화면 중앙에 오도록 스크롤
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            # 클릭 인터셉트 발생 시 짧은 대기 후 재시도
            time.sleep(0.5)
            element.click()
    def clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def texts(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return [el.text for el in elements]

    def is_displayed(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
    
    def get_attribute(self, by_locator, attribute):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).get_attribute(attribute)

    def get_attributes(self, by_locator, attribute):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return [element.get_attribute(attribute) for element in elements]

    def move_sliders(self, by_sliders_locator, by_sliders_size_locator, by_sliders_size_sub_locator, sweet_value, salty_value, spicy_value):
        # 불필요한 암시적 대기는 제거하고 명시적 대기만 사용
        sliders = self.elements(by_sliders_locator)
        sliders_size = self.elements(by_sliders_size_locator)
        slider_size = sliders_size[0].size['width']
        right_values = self.get_attributes(by_sliders_size_sub_locator,"style")
        current_values = []
        for value in right_values:
            value = value.split("right:")[1].split("%")[0].strip()
            current_values.append(100.0 - float(value))
        sweet = round((slider_size * ((-(current_values[0] - float(sweet_value) * 20)) * 0.01)),2)
        salty = round((slider_size * ((-(current_values[1] - float(salty_value) * 20)) * 0.01)),2)
        spicy = round((slider_size * ((-(current_values[2] - float(spicy_value) * 20)) * 0.01)),2)
        offset_value = [sweet, salty, spicy]
        action = ActionChains(self.driver)
        for slider, offset in zip(sliders, offset_value):
            # 스크롤로 요소 노출
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", slider)
            action.move_to_element(slider).perform()
            action.click_and_hold(slider).move_by_offset(offset + (slider_size * 0.005), 0).release().perform()
            
            

    #개인 피드 탭 진입 버튼
    my_feed_btn = (By.XPATH,'//*[@href="/my"]')
    
    #GNB 영역
    back_btn = (By.CLASS_NAME,'cursor-pointer')
    GNB_my_page = (By.XPATH, '//span[contains(@class, "text-title")]')
        
    #프로필
    my_profile_team = (By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/div/div')
    my_profile_name = (By.XPATH, '//span[text()="육조임"]')
    my_profile_food_value = (By.XPATH, '//span[@class="w-8 text-right text-gray-500 text-subbody"]')
    my_profile_prefer = (By.XPATH, '//p[@class="w-4/5"]')
    
    #내 통계
    my_status = (By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[1]/span')

    #내 프로필 진입 버튼
    my_profile_section = (By.XPATH,'//section[contains(@class,"w-full flex")]')
    my_profile_btn = (By.CSS_SELECTOR, "div.flex.items-center.justify-between.text-subbody > svg.cursor-pointer")
    my_profile_gnb = (By.XPATH, "//span[text()='프로필 정보 수정']")
    my_profile_back_btn = (By.XPATH,'//button[contains(@class, "cursor-pointer")]')
    my_profile_edit_title = (By.XPATH,'//span[text()="프로필 이미지 수정"]')
    my_profile_img = (By.XPATH,"//img[@alt='프로필 이미지' and contains(@class, 'border-light-gray')]")
    default_profile = os.path.abspath('utils/default_profile_image.png')
    my_profile_img_input = (By.NAME, "profileImageUrl")
    my_profile_prefer = (By.NAME,"pros")
    my_profile_hate = (By.NAME,"cons")
    my_profile_warn = (By.XPATH,"//p[contains(text(),'10자 이상 입력해주세요')]")
    my_profile_submit_btn = (By.XPATH,"//button[@type='submit']")
    my_profile_edit_complete = (By.XPATH,"//div[@role='status']")
    my_profile_feed = (By.XPATH, "//p[@class='w-4/5']")
    ## 슬라이더 요소 (role="slider"인 요소)
    sliders = (By.XPATH, '//*[@id="modal-root"]//span[@role="slider"]')
    sliders_amount = (By.XPATH,'//*[@id="modal-root"]//span[@class="w-8 text-right text-gray-500 text-subbody"]')
    sliders_size = (By.XPATH, '//*[@id="modal-root"]//span[@class="relative h-2 w-full grow overflow-hidden rounded-full bg-light-gray"]')
    sliders_size_sub = (By.XPATH,'//*[@id="modal-root"]//span[@class="absolute h-full bg-sub"]')

    #홈 탭 - 혼자 먹기
    eat_alone_home_btn = (By.XPATH, "//button[.//p[text()='혼자 먹기']]")
    eat_alone_home_combobox = (By.XPATH, "//button[@role='combobox']")
    eat_alone_home_category_Korean = (By.XPATH, "//span[text()='한식']")
    eat_alone_home_choose_btn = (By.XPATH, "//button[text()='선택 완료']")
    eat_alone_home_accept_recommend = (By.XPATH, "//button[text()='추천 수락하기']")   

    # 내가 먹은 메뉴 추가
    my_add_menu = (By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button') 
    my_add_history_menu = (By.XPATH, "//*[contains(text(), '내가 먹은 메뉴')]")
    my_add_same_menu_btn = (By.XPATH, "//button[text()='같은 메뉴 먹기']")

    # 새로운 후기 등록하기
    my_add_review_tab = (By.XPATH,'//*[@id="modal-root"]/div')
    my_add_review_GNB = (By.XPATH,'//span[text()="새로운 후기 등록하기"]')
    my_add_review_again_GNB = (By.XPATH,'//span[text()="또 먹은 후기 등록하기"]')
    my_add_review_back_btn = (By.XPATH,'//button[contains(@class, "cursor-pointer")]')
    ## 식사 유형
    my_add_eat_title = (By.XPATH,'//h1[text()="식사 유형"]')    
    my_add_eat_alone = (By.XPATH, "//label[@for='혼밥']")
    my_add_eat_group = (By.XPATH, "//label[@for='그룹']")
    my_add_eat_together = (By.XPATH, "//label[@for='회식']")
    my_add_eat_alone_radio = (By.ID, "혼밥")
    my_add_eat_group_radio = (By.ID, "그룹")
    my_add_eat_together_radio = (By.ID, "회식")
    my_add_eat_alone_click = (By.XPATH,'//button[@type="radio" and @value="혼밥"]')
    my_add_eat_group_click = (By.XPATH, '//button[@role="radio" and @value="그룹"]')
    my_add_eat_together_click = (By.XPATH,'//button[@type="radio" and @value="회식"]')
    ## 후기 사진
    my_add_review_title = (By.XPATH,'//h1[text()="후기 사진"]')
    my_add_review_img_is_null = (By.XPATH, ".//div[contains(@class, 'object-cover w-24 h-24 rounded-md border-[1px] border-light-gray')]")
    my_add_review_img_btn = (By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/button')
    my_add_review_img_input = (By.NAME, 'reviewImg')
    my_add_image_path = os.path.abspath('utils/망글곰.png')
    my_add_review_img = (By.XPATH,"//img[@alt='후기 사진']")
    ## 메뉴 명
    my_add_menu_title = (By.XPATH,'//h1[text()="메뉴 명"]')
    my_add_menu_name = (By.NAME,'menu')
    ## 카테고리
    my_add_category_title = (By.XPATH,'//h1[text()="카테고리"]')
    my_add_category_name = (By.XPATH,'//*[@id="modal-root"]//button[@role="combobox"]')
    my_add_category_text = (By.XPATH,'//button[span[@style="pointer-events: none;"]]')
    my_add_category_list_name = (By.XPATH, "//select/option")
    my_add_category_clickable_list = (By.XPATH, '//div[@role="option"]')
    ## 후기
    my_add_comment_title = (By.XPATH,'//h1[text()="후기"]')
    my_add_comment_name = (By.NAME, 'comment')
    ## 별점
    my_add_star_title = (By.XPATH,'//h1[text()="별점"]')
    my_add_star_rate = (By.XPATH,".//div[contains(@class, 'text-gray-300')]" )
    my_add_star_yellow = (By.XPATH,".//div[contains(@class, 'text-yellow-400')]" )
    my_add_stars_3 = (By.XPATH, '//div[text()="★"][3]')
    my_add_stars_5 = (By.XPATH, '//div[text()="★"][5]')
    ## 같이 먹은 사람 등록
    my_add_eat_with_title = (By.XPATH,'//h1[text()="같이 먹은 사람 등록"]')
    my_add_eat_with_name = (By.XPATH,'//input[contains(@placeholder, "이름을 검색해주세요")]')
    ## 필수 영역 안내
    my_add_desc_list = (By.XPATH, '//p[contains(@class,"text-red-500")]')
    ## 후기 작성 완료
    my_add_submit_btn = (By.XPATH, '//button[@type="submit"]')
    ## 리뷰 등록 완료 버튼 확인
    my_add_review_status = (By.XPATH,'//div[text()="리뷰 등록 완료"]')

    #내가 먹은 메뉴
    my_add_history_menu_recent = (By.XPATH, '//div[contains(@class, "flex w-full gap-6 p-4 shadow-md rounded-2xl")]')
    my_add_history_eat_main_type = (By.XPATH,"//div[@class='inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-main text-white']")
    my_add_history_eat_sub_type = (By.XPATH,"//div[@class='inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-sub text-white']")    
    my_add_history_eat_sub_2_type = (By.XPATH,"//div[@class='inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-sub-2 text-white']")
    my_add_history_pic = (By.XPATH,'//img[not(@alt="프로필 이미지")]')
    my_add_history_star = (By.XPATH,'//span[@class="text-[#FFCD29]"]')
    my_add_history_btn = (By.XPATH,'//button[text()="같은 메뉴 먹기"]')

    #AI추천 사전조건
    add_AI_recommend = (By.XPATH,"//button[.//p[text()='회식 하기']]")
    add_AI_category = (By.XPATH,"//button[@role='combobox']")
    add_AI_categories_list = (By.XPATH, '//div[@role="option"]')
    add_AI_btn = (By.XPATH, "//button[text()='선택 완료']")
    add_AI_accept_btn = (By.XPATH,"//button[text()='추천 수락하기']")
    history_add_review = (By.XPATH,"//button[text()='추천 후기 등록하기']")
    add_review_img = (By.NAME, 'reviewImg')
    menu_name = (By.NAME,"menu")
    image_path = os.path.abspath('utils/망글곰.png')
    comment = (By.NAME,"comment")
    star_3 = (By.XPATH, '//div[text()="★"][3]')
    review_submit_btn = (By.XPATH, '//button[@type="submit"]')