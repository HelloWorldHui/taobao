# coding=utf
"""
author=Hui_T
"""
import time
from setting import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import pymongo
def taobao(user,passwd):

    # 查找元素 等待十秒
    # driver.implicitly_wait(10)

    # 打开网页 点击 账号密码登录
    login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.J_Quick2Static')))
    # login_button = driver.find_element_by_css_selector(".J_Quick2Static")
    login_button.click()

    # 点击微博登录
    weibo_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"html.ks-gecko66.ks-gecko.ks-firefox66.ks-firefox body.chl-reg div#page div#content div.content-layout div.login-box-warp div#J_LoginBox.login-box.no-longlogin.module-static div.bd div#J_StaticForm.static-form form#J_Form ul.entries li#J_OtherLogin.other-login a.weibo-login")))
    weibo_login.click()
    time.sleep(1)

    # 输入账号
    user_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".username > input:nth-child(1)")))
    user_input.send_keys(user)
    time.sleep(1)

    # 输入密码
    pass_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".password > input:nth-child(1)")))
    pass_input.send_keys(passwd)
    time.sleep(1)

    # 登录按钮
    login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".W_btn_g > span:nth-child(1)")))
    login.click()

    # 获取用户名
    name_info = False
    while not name_info:
        try:
            name_info = driver.find_element_by_css_selector(".site-nav-login-info-nick")
            print("登录成功", name_info.text)
        except Exception as e :
            print("尝试手动登录",1)
            time.sleep(3)

def my_order():
    pass
if __name__ == '__main__':
    user = input("输入会员名/微博/手机号:")
    password = input("输入密码:")
    # 创建驱动器对象           驱动器位置
    driver = webdriver.Firefox(executable_path="F:/火狐/geckodriver")
    login_url = "https://login.taobao.com/member/login.jhtml"
    wait = WebDriverWait(driver, 20)  # 显示等待 20秒元素加载
    driver.get(login_url)

    # 登录
    taobao(user,password)

    # 进入我的订单
    my_order()