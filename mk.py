from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#### 가상환경 실행시 셀레니움 설치 필요
#### 크롤링 실행전
#### 마이그레이트 한 뒤 판매자 유저 id(pk=1) 반드시 생성!!!
import time

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt.settings")
django.setup()
from products.models import Product

# 크롬드라이버 가져오기
driver = webdriver.Chrome("chromedriver.exe")
# 마켓컬리 베스트 상품 페이지
url = "https://www.kurly.com/goods-list?category=029"
driver.get(url)
driver.implicitly_wait(time_to_wait=5)

# 상품 div 가져옴
elements = driver.find_elements(By.CLASS_NAME, "css-1xyd46f")
print("찾은 항목수: ", len(elements))
item_list = []
# 크롤링 딜레이시간, 에러가 날 경우 count+=1 헤서 딜레이를 늘려줄것
count = 2
error = []
# 상품의 개수만큼 반복
for i in range(len(elements) - 2):
    # 페이지를 이동하면 driver의 elements를 다시 받아줘야한다.
    # 상품 상세보기로 이동했다가 다시 돌아오면 elements사용에 오류가 났다.
    # 그래서 반복문을 시작할 때 elemets를 새로 받아준다.
    elements = driver.find_elements(By.CLASS_NAME, "css-1xyd46f")
    element = elements[i]

    # 제품 이름, 이미지 URL 가져오기
    item_name = element.find_element(By.CLASS_NAME, "e1c07x485").text
    ori_img = element.find_element(By.TAG_NAME, "img").get_attribute("src")
    sales_price = element.find_element(By.CLASS_NAME, "sales-price").text
    sales_price = int(sales_price[:-2].replace(",", ""))
    user = 0
    # print(sales_price)
    # print(item_name)
    # 상품 클릭
    element.click()

    time.sleep(count)

    try:
        # 상품 설명 페이지

        descriptions = driver.find_elements(By.ID, "description")
        summeary = driver.find_elements(By.CSS_SELECTOR, ".exslwju2")
        description = descriptions[0].find_element(By.CSS_SELECTOR, ".goods_intro").text
        produt_detail_img = (
            descriptions[0].find_element(By.TAG_NAME, "img").get_attribute("src")
        )

        # print("",summeary[7].find_element(By.CSS_SELECTOR, ".exslwju1").text)
        # print(summeary[6].find_element(By.CSS_SELECTOR, ".exslwju1").text)
        # print(summeary[8].find_element(By.CSS_SELECTOR, ".exslwju1").text)
        # print(summeary[9].find_element(By.CSS_SELECTOR, ".exslwju1").text)
        # discount_rate = element.find_element(By.CLASS_NAME, "discount-rate").text
        # dimmed_price = element.find_element(By.CLASS_NAME, "dimmed-price").text
        # 상세보기 페이지의 elements가져옴
        details = driver.find_elements(By.ID, "detail")
        # 설명글
        # 상품 상세 이미지ezpe9l14
        # produt_detail_img=0

        allergy = 0
        unit = 0
        weight = 0
        # 영양성분표 이미지 URL
        detail_img = details[0].find_element(By.TAG_NAME, "img").get_attribute("src")
        # 리스트에 넣기
        print("상품이름:", item_name)
        print("판매가:", sales_price)
        print("상품 대표 이미지", ori_img)
        print("상품 성분 이미지:", detail_img)
        print("상품 상세 이미지", produt_detail_img)
        print("상품 설명글:", description)
        produt_thum_img = ori_img
        produt_desc_img = detail_img
        # 배송 타입
        shiping_type = summeary[0].find_element(By.CSS_SELECTOR, ".exslwju1").text
        print("배송 타입:", shiping_type)
        # 판매자
        user = summeary[1].find_element(By.CSS_SELECTOR, ".exslwju1").text
        print("판매자:", user)
        # 포장형태
        pack_type = summeary[2].find_element(By.CSS_SELECTOR, ".exslwju1").text
        print("포장형태:", pack_type)
        # 판매 단위
        unit = summeary[3].find_element(By.CSS_SELECTOR, ".exslwju1").text
        print("판매단위:", unit)
        # 중량
        weight = summeary[4].find_element(By.CSS_SELECTOR, ".exslwju1").text
        print("중량:", weight)
        # 원산지
        loc = summeary[5].find_element(By.CSS_SELECTOR, ".exslwju1").text
        print("원산지:", loc)
        allergy = summeary[6].find_element(By.CSS_SELECTOR, ".exslwju1").text
        print("알러지:", allergy)
        item_list.append(
            {
                "item_name": item_name,
                "sales_price": sales_price,
                "ori_img": ori_img,
                "detail_img": detail_img,
                "description": description,
                "produt_detail_img": produt_detail_img,
                "produt_thum_img": produt_thum_img,
                "produt_desc_img": produt_desc_img,
                "shiping_type": shiping_type,
                "user_id": 1,
                "package_type": pack_type,
                "unit": unit,
                "weight": weight,
                "loc": loc,
            }
        )
        # 확인
        # print(item_list[-1])
    # 만약 에러가 발생하면
    except:
        # 대기시간 증가 및 확인
        count += 1
        print("에러발생횟수:", count)
        # 에러 리스트에 넣기
        error.append(element)
        # 만약 count가 100번 이상이면 루프 탈출
        if count >= 100:
            break

    # 브라우져 뒤로가기
    driver.execute_script("window.history.go(-1)")
    time.sleep(count)

# 작업 완료 후 드라이버 종료
driver.close()
print(error)


def add_data():
    result = []

    # 자료 수집 함수 실행
    for data in item_list:
        tmp = data
        # 만들어진 dic를 리스트에 저장
        result.append(tmp)
    # print(result)
    # DB에 저장
    for item in result:

        Product(
            title=(item["item_name"]),
            price=item["sales_price"],
            unit=item["unit"],
            weight=item["weight"],
            crawl_produt_thum_img=(item["produt_detail_img"]),
            crawl_produt_detail_img=(item["produt_thum_img"]),
            crawl_produt_desc_img=(item["produt_desc_img"]),
            description=(item["description"]),
            stock=1000,
            sales_rate=1,
            user_id=1,
            ship_type=item["shiping_type"],
            is_crawl=True,
            allergy="",
        ).save()

    return result


add_data()
