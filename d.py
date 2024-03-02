from abc import ABC, abstractmethod

class LoginMethod(ABC):
    @abstractmethod
    def login(self, data):
        pass

# logging, 
# loguru,
# Google_auth

class logging(LoginMethod):
    def login(self, data):
        print("login using LoginMethod")
        print(f"login data: {data}")

class loguru(LoginMethod):
    def login(self, data):
        print("login using Loguru")
        print(f"login data: {data}")

class Google_auth(LoginMethod):
    def login(self, data):
        print("login using Google_auth")
        print(f"login data: {data}")

class login:
    def __init__(self, loginMethod: LoginMethod):
        self.loginMethod = loginMethod
    def loginProcess(self, data):
        self.loginMethod.login(data)

def demo():
    data = "Greg"
    loginProcessor = login(logging())
    loginProcessor.loginProcess(data)

    loginProcessor = login(loguru())
    loginProcessor.loginProcess(data)

    loginProcessor = login(Google_auth())
    loginProcessor.loginProcess(data)

if __name__ == "__main__":
    demo()