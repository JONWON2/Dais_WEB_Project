#  Side Project -> Django를 활용한 웹사이트 제작하기

<br>

![main page](https://user-images.githubusercontent.com/82020691/152634327-0ad8ee5f-dda6-41a4-95d4-4bb3b55724d4.JPG)


작성자 : 김종원 / 최근 수정일자 : 2022.02.03. 

  * 추후 개발했던 방법에 대해서 기록을 남기고자 합니다.
    * 부트스트랩 템플릿을 사용하는 방법
    * XD 프로그램 핵심 사용방법
      * XD 디자인 후 해당 디자인에 대한 CSS 만들어 적용하는 방법
    * Django 프레임워크를 사용해 웹사이트 만드는 동작 원리 및 꿀팁!
      * MTV 패턴 소개
    * DB 설계시 ERD 작성에 대한 무료 툴 소개
 
<br>
<br>

## 🚗 How to run
*우분투 -> 도커편

1. 도커 허브(https://hub.docker.com/)에서 아나콘다 최신 이미지를 다운받아주세요.
```
  docker pull continuumio/anaconda3:latest
```
2. 로컬 환경에서 /home/pratice/ 폴더를 만들고, Dais_WEB_Project repository를 clone해주세요.
```
  mkdir /home/pratice/
  cd /home/pratice/
  git clone https://github.com/dais-lab/Dais_WEB_Project.git
```

3. 시크릿키를 발급 받아서 깃허브 홈디렉토리에 secrets.json 파일을 생성 후 기입해주세요.
```
  cd Dais_WEB_Project/
  https://www.miniwebtool.com/django-secret-key-generator/
  vi secrets.json
  {
    "SECRET_KEY": "..."
  }
```
4. 격리된 컨테이너 공간을 생성합니다.
```
  docker run --name Lab -v /home/pratice/:/working_docker_folder -p 8000:8000 continuumio/anaconda3:latest

  ## 도커 환경에 진입했다면, 파이썬 3.6.4 버전으로 가상환경 생성.
  conda create -n lab python=3.6.4
  conda activate lab

  ## 도커 환경에 진입하지 못했다면
  docker start Lab
  docker exec -it Lab bash
  ## 파이썬 3.6.4 버전으로 가상환경 생성.
  conda create -n lab python=3.6.4
  conda activate lab
```
5. 생성된 가상환경 내에서 필요한 패키지 설치해주세요.
```
  cd /working_docker_folder/Dais_WEB_Project/
  # mysqlclient를 설치하기 위해 아래 코드를 진행.
  apt-get update
  # 만약 아래 코드가 에러가 난다면 - > apt-get install default-libmysqlclient-dev build-essential 
  apt-get install python3.6-dev default-libmysqlclient-dev build-essential
  # mysqlclient가 반드시 설치가 되어야한다.
  pip install mysqlclient
  pip install -r requirements.txt
```

6. 프로젝트 실행에 필요한 테이블을 생성해주세요.
```
  python manage.py migrate
```

7. 웹 어플리케이션(WAS)을 실행시켜주세요.
```
  python manage.py runserver 0.0.0.0:8000
```

8. 웹 사이트에 아래 링크를 입력해주세요.
```
  http://127.0.0.1:8000/app/main or http://외부IP:8000/app/main or http://도메인:8000/app/main 
```

9. 만약 AWS를 사용해 실행시키는 경우. 보안 그룹을 다음과 같이 설정해야 접속이 가능하다.
![aws 보안규칙](https://user-images.githubusercontent.com/46054315/152639107-711432db-85b5-4cd5-9746-0eaf73646740.PNG)

---
<br>
<br>

## 🚗 How to run

* 윈도우 -> 아나콘다
1. 아나콘다 프롬프트를 실행시켜 python 3.6.4의 가상환경을 만든다.
```
  conda create -n django python=3.6.4
```
2. vscode를 실행 시켜서 git clone을 진행한다.
```
  git clone https://github.com/dais-lab/Dais_WEB_Project.git
```
3. 아까 설치한 django 가상환경으로 설정 후, 필요한 패키지를 설치한다.
```
  # vs code 창에서 command Propt를 클릭하여 아래 명령어를 입력해 패키지를 설치한다.
  pip install -r requirements.txt
  pip install mysqlclient-1.4.6-cp36-cp36m-win_amd64.whl
```
4. 시크릿키를 발급 받아서 secrets.json 파일을 생성 후 기입해주세요.
```
  https://www.miniwebtool.com/django-secret-key-generator/
  
  secrets.json 파일에 ... 부분에 시크릿키를 발급받아서 진행해주세요.
  {
    "SECRET_KEY": "..."
  }
```
5. 프로젝트 실행에 필요한 테이블을 생성해주세요.
```
  python manage.py migrate
```

6. 웹 어플리케이션(WAS)을 실행시켜주세요.
```
  python manage.py runserver
```

7. 웹 사이트에 아래 링크를 입력해주세요.
```
  http://127.0.0.1:8000/app/main 
```

---


## ⚙ Environment

Frontend

```
- bootstrap4 : 0.1.0
```

Backend

```
- django version : 3.2.11
```

Database

```
- MySql
```

<br>

## ⚡ tech-stack

### front-end

- bootstrap
- css

### backend

- django
- Mysql

## tools
- github
- erd cloud
- adove xd

<br>

## 📅 Development period

2022.01.30 ~ 2022.02.03(5-Days)
---
