import pytest
import allure

'''
pytest 可以自動把 fixture 的名字帶到測試函數中，N 個測試函數都需要同樣的 fixture 的話，就可以直接在測試函數寫上與該 fixture 同名的參數， pytest 就會自動幫忙代入 fixture
'''
@pytest.fixture()
def hello_world():
    return "hello_world"

def test_h_in_hello_world(hello_world):
    assert "h" in hello_world

def test_w_in_hello_world(hello_world):
    assert "w" in hello_world

def test_s_in_hello_world(hello_world):
    assert "s" in hello_world

def test_d_in_hello_world(hello_world):
    assert "d" in hello_world

'''
可以利用 @allure.step("說明") 裝飾子(decorator)將流程細分為多個步驟
'''

@allure.step("註冊")
@allure.step("a account")
def signup():
    key_in_account_and_password("a", "passwda")

@allure.step("登入")
@allure.step("b account")
def login():
    key_in_account_and_password("b", "passwdb")

@allure.step("輸入帳號密碼")
def key_in_account_and_password(account, password):
    pass

def test_signup_and_login():
    signup()
    login()
