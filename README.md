# How To Install
## Virtualenv 만들기
***
virtualenv을 이용해 가상환경을 만들어 사용한다.

> 사용 환경: python3
> 
> Framework: Flask
> 
> DB: MySQL 8.0.32

가상환경 설치 & 생성 
``` 
$ sudo pip3 install virtualenv
``` 

프로젝트 폴더에서 가상환경을 생성하고 켜준다.
``` 
$ virtualenv [venv_name] -p python3
$ source [venv_name]/bin/activate
``` 
가상환경을 끄고 싶으면 deactivate을 입력한다.
```
(venv)$ deactivate
```  
### Packages
***
1. Flask-SQLAlchemy
``` 
(venv)$ pip install Flask Flask-SQLAlchemy
```
### 패키지 관리 팁
파이썬 프로젝트들은 보통 requirements.txt에 사용하는 패키지명들을 기록하여 아래의 명령어로 쉽게 설치 가능.
```
(venv)$ pip install -U -r requirements.txt
```
현재 설치된 패키지들을 모두 requirements.txt에 기록하려면 다음 명령을 사용하면 된다.
```
(venv)$ pip freeze > requirements.txt
```


for test commit