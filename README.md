# Brokuly🥦

> 이커머스 사이트 [ Brokuly🥦] project
>
> Domain : http://brokurly.shop/
>
> ![logo.png](assets/9d4aadd340d3ad41028ddcbf41a645a7a24fb09a.png)



## 🔖 Table of contents

- [General info](#general-info)
- [Requirements](#requirements)
- [Modeling](#modeling)
- [Technologies](#technologies)
- [Features](#features)
- [Reviews](#reviews)
- [Scrum Record](#Scrum Record)



## 📜 General info

- ![Untitled.png](assets/ee7adae9988bb42a593642e491a4d5d192d2b2ff.png)
- 개발기간 : 2022. 11. 09 - 2022. 11. 22
- 팀원 :  
  Front-end([김예린](https://github.com/ererink/), [임선주](https://github.com/snnzzoo/))
  Back-end([이동근](https://github.com/qlghwp123/), [이태극](https://github.com/uRo3YA/), [최준우](https://github.com/wnsn8546/))



## 🧭Requirements

- 1️⃣ 서비스에는 최소 20개의 콘텐츠 정보(여행지, 맛집, 영화, 상품)가 생성된 상태여야 합니다.
- 2️⃣ 콘텐츠 정보 & 후기 공유 커뮤니티 서비스에 필요한 최소한의 CRUD를 구현해야 합니다.
- 3️⃣ 회원 인증 기능을 구현하고, 권한에 따라 서비스 사용을 제한해야 합니다.
- 4️⃣ 사용자는 콘텐츠 또는 후기에 좋아요를 남길 수 있어야합니다.
- 5️⃣ 사용자간 팔로우를 할 수 있어야합니다.
- 6️⃣ HTML / CSS / JavaScript를 활용해서 웹 사이트를 디자인합니다.
- **7️⃣ 완성한 서비스는 배포해야하며 발표회에서는 배포된 서비스를 시연해야 합니다.**



## 🗃️Modeling

### ERD 모델

> ![brokuly_20221120_221825.png](assets/44acdf0f19105dcc740be7e9619498ca38c07c7f.png)

### 와이어 프레임

> ![Screenshot 2022-11-20 at 22.24.30.JPG](assets/57f934bf2a6c240800146820c4a25af9436a08cb.JPG)



## 💻Technologies

### Technology stack

* Version Control and Messenger

  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"> <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white">

* Backend and Testing

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"><img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white">

* Frontend

  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"> <img src="https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=Axios&logoColor=white">

* Infra

  <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white">![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)



## 🔍Features

### 담당 역할

#### 이동근

- ⭐Team Leader⭐
- Back-end(Accounts App)
- Deploy to Amazon EC2 
- Bug Fix

#### 김예린

- Front-end
- 메인 페이지, 상품 메인 페이지, 상품 상세 페이지 화면 구현
- navbar 구현
- 회원가입 및 로그인, 회원탈퇴 페이지 화면 구현

#### 임선주

- Front-end
- 

#### 이태극

- Back-end (Products, Review App, Accounts 일부)
- Crawling
- Search
- Bug Fix

#### 최준우

- Back-end(Order,Qnas)
- Social Login(Naver, KaKao)
- Social Share(Facebook, Twitter, Naver, KaKao)
- KAKAO Address Search API, KAKAO Map API, KAKAO Pay API
- ID , Email Duplication Check, Email Verification(Number check)
- Bug Fix

### 기능 소개

### Main Page

- Navbar
  

  > ![Untitled (1).png](assets/56bf0f649a919283257a0a5de499fe3f470fe333.png)

  > 스크롤을 내리면 다른 Navbar 출력 


- Section
  
  > 각각의 섹션에서 조회기준을 통해 여러 객체 출력

### Accounts APP

- CRUD

  >판매자 / 구매자를 선택하여 유저 생성 가능

- 로그인, 로그아웃

  > 로그인, 로그아웃 기능 구현

* 마이페이지

  > 판매자 / 구매자에 따라 화면 구성을 다르게 보여줌

* 장바구니

  > 상품 상세에서는 장바구니로 redirect
  >
  > 검색 및 위시리스트에서 모두 비동기 통신으로 장바구니 추가/삭제 구현 

* 위시리스트

  > 상품 상세에서 비동기로 추가 기능 구현

* 유저가 작성한 리뷰 목록

  > 유저가 작성한 리뷰 목록을 마이페이지에서 조회 가능

* 아이디 및 이메일 중복체크

  > DB 에서 ID 중복 체크, 이메일

* 네이버 로그인 

  > 네이버 로그인 구현

* 상품 관리

  > 현재 판매자가 판매하고 있는 상품을 조회

* 상품 문의

  > 현재 구매자가 생성한 문의 목록을 조회

* 이메일 인증

  > 랜덤 코드 발송을 비동기로 구현 

* 주문 목록

  > 현재 구매자가 주문 생성한 목록을 조회

### Products APP

- index 페이지
  
  > 호버로 제품별 이미지 효과

- 상세 페이지
  
  > 상품 리뷰 작성은 모달 팝업으로 제작
  > 상품 문의는 아코디언으로 확장

- 데코레이터
  
  > 데코레이터 구성으로 유저 권한(판매자/구매자)에 따른 기능 접근 제한

- CRUD
  
  > 상품 생성시 멀티셀렉트 필드를 이용한 다양한 옵션 선택 가능

- 크롤링
  
  > 크롤링을 통한 기존 상품들 대량 등록

- 페이지네이션
  
  > 페이징처리하여 상품별 출력 갯수 적절히 조절

- 검색 기능
  
  > Q 모듈을 이용한 검색기능
  > Listview를 이용한 페이지네이션

- 판매자 팔로우 기능
  
  > 비동기 통신으로구현 Accounts 앱으로 연결
  > 마이페이지의 팔로잉 목록에서 판매자의 최근 판매 상품 볼 수 있음

- 위시리스트 기능
  
  > 비동기 통신으로구현 Accounts 앱으로 연결

- 상품문의 기능
  
  > 상품별 상세 페이지에서 문의사항과 답변을 출력하며
  > 기능은 Qnas앱으로 연결

- 장바구니 기능
  
  > Orders 앱으로 연결

### Reviews APP

- CRUD
  
  > 상품 생성시 멀티셀렉트 필드를 이용한 다양한 옵션 선택 가능
  > 리뷰 모델과 분리한 이미지 모델을 이용해 하나의 리뷰에 여러 이미지 삽입

- 평점
  
  > 상품에 해당하는 리뷰 평점을 계산하여 상품 평점 반환

- 추천
  
  > 비동기 통신으로 구현

- 댓글
  
  > 비동기 통신으로 구현

### Qnas APP

- 질문 CRUD
  
  > 상품에 대한 구매자의 문의 작성, 조회, 수정, 삭제
  
- 답변 CRUD

  > 문의에 대한 판매자의 답변 작성, 조회, 수정, 삭제

- 상태

  > 답변대기, 답변완료상태 표시

### Orders APP

* 주문 기능

  > 카트 -> 주문서 -> 주문완료의 흐름으로 구현

* 결제 기능

  > 카카오페이 API 를 활용한 결제 확인 테스트 구현



## 💬Reviews

- 이동근
  - 이번 프로젝트에서 팀의 팀장으로서 미숙했던 점이 아주 많았다는 것을 알게 되었습니다. 
  - 제가 생각한 문제점과 알게된 것은 다음과 같습니다.
  - 기획에 비해 저의 개발 속도가 매우 느렸습니다. 
    - 개인 개발 역량을 키워야 함을 깨달았습니다.
  - 업무 분담이나 소통 및 팀원 역량 파악 등 많이 부족합니다.
    - 더 많이 소통하고 팀원 이전에 사람으로서 다가가는 것이 필요하다는 것을 알게 되었습니다.
  - 결정 해야할 때를 놓치고 우유부단하여 초기 생각했던 것보다 많은 시간이 소요되었습니다.
    - 팀에 필요한 일이라면 직언이 필요함을 깊이 깨달았습니다.
  - 노션과 디스코드를 사용하다 보니 문서의 통일을 못한거 같습니다. 
    - 분명하게 정하고 문서화하는 습관과 정리하는 습관이 필요하다는 것을 알게 되었습니다.
  - 역량이 부족해서 항상 팀원분들께 많이 미안하고 죄송하고 감사했습니다.
  - 힘들었지만 정말 값진 시간을 얻은거 같습니다.
- 김예린
  - 
- 임선주
  - 
- 이태극
 
  > 왜 사람들이 Django에서 함수형 뷰를 안쓰고, 제네릭 뷰로 상속 받아서 쓰는지 알게되었습니다.<br> 특히 마이페이지 구현이나, 검색의 경우 이전 페이지에서 값들 불러온 상태에서 렌더링이 되야 하는데 <br>일반 함수형 뷰를 쓸 경우 context에 많은양을 집어넣어야 해서 다른 코드를 재활용하기 힘들었습니다.
  
- 최준우
  - 이전 프로젝트에서 하고 싶었던 다양한 API들을 사용해볼 수 있었던 기회였습니다.
  - 주문, 이메일 인증 등의 기능 흐름을 살펴보고 해당 기능을 구현할 수 있는 다양한 방법들을 찾아 볼 수 있었습니다.
  - 다음 프로젝트에서는 이번 프로젝트의 경험을 바탕으로 DRF 등을 활용하여 직접 API서버도 구축 해봐야겠다는 생각이 들었습니다. 감사합니다.



## Scrum Record

main 브랜치의 경우
[스크럼 일지 바로가기!](https://github.com/qlghwp123/SPJT-02/tree/main/scrum)

develop 브랜치의 경우
[스크럼 일지 바로가기!](https://github.com/qlghwp123/SPJT-02/tree/develop/scrum)

