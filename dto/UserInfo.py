'''사용자의 기본정보 및 계정 정보 저장하는 엔티티 '''

class UserInfo:
    def __init__(self, usrId:str, money:int, usrPwd:str):
        self.usrId = usrId
        self.usrPwd = usrPwd
