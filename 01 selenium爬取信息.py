# coding=utf
"""
author=Hui_T
"""
import time

from selenium import webdriver
# 驱动器
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree

# 登录淘宝
def taobao(user,passwd):

    # 查找元素 等待十秒
    # driver.implicitly_wait(10)
    # 打开网页 点击 账号密码登录
    driver.get(login_url)
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
            print("手动输入验证码",1)
            time.sleep(3)

def search(shop):
    # 搜索商品
    search_input = wait.until(EC.presence_of_element_located((By.ID,"q")))
    search_input.send_keys(shop)

    # 搜索按钮
    search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button")))
    search_button.click()
    time.sleep(1)
    return driver.page_source

# 网站源码
# print(driver.page_source)

if __name__ == '__main__':
    user = input("输入会员名/微博/手机号:")
    password = input("输入密码:")
    shop = input("输入商品名:")
    # 创建驱动器对象           驱动器位置
    driver = webdriver.Firefox(executable_path="F:/火狐/geckodriver")
    login_url = "https://login.taobao.com/member/login.jhtml"
    wait = WebDriverWait(driver, 20) # 显示等待 20秒元素加载

    # 登录
    taobao(user,password)



    # 搜索     driver.page_source 返回网页源码
    source = search(shop)

    # 写入
    tree = etree.HTML(source)
    ret = tree.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div')
    for element in ret:
        price = "￥" + element.xpath('div[2]/div[1]/div[1]/strong/text()')[0]
        name = ",".join([i.strip() for i in element.xpath('div[2]/div[2]/a/text()') if i.strip() != ''])
        sales = " "+element.xpath('div[2]/div[1]/div[2]/text()')[0]
        print(price, name, sales)
        with open(shop+".text","a",encoding="utf8") as f:
            f.write(price+name+sales+"\n")

    # with open("taobao.html","w",encoding="utf8") as f :
    #     for i in driver.page_source:
    #         f.write(i)

    driver.close()