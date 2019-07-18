# coding=utf
"""
author=Hui_T
"""
import json
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

# 连接mongoDB 返回spider库
def Mongo_client(ip, port, username, password):
    db = pymongo.MongoClient(host=ip, port=port, username=username, password=password)
    return db.spider

def my_order():
    my_taobao_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_SiteNavMytaobao > div.site-nav-menu-hd > a')))
    my_taobao_a.click()
    time.sleep(1)
    my_shop_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#bought')))
    my_shop_a.click()
    return driver.page_source

def filter_write_mongodb(tree):
    #  该网页订单
    order_div = tree.xpath('//*[@id="tp-bought-root"]/div')

    # 筛选出 订单 div
    order_div = order_div[3:18]
    # print(order_div)
    if not order_div :
        print("没有订单信息")
    else:
        with open('./data/data.csv','w',encoding='utf8') as f :
            for  ele in order_div:
                try:
                    date = ele.xpath(".//div/table/tbody[1]/tr/td[1]/label/span[2]/text()")[0]
                    order = ele.xpath('.//div/table/tbody[1]/tr/td[1]/span/span[3]/text()')[0]
                    name = ele.xpath('.//div/table/tbody[2]/tr[1]/td[1]/div/div[2]/p[1]/a[1]/span[2]/text()')[0]
                    shop_title = ele.xpath('.// div / table / tbody[1] / tr / td[2] / span / a /text()')
                    shop_title = shop_title[0] if shop_title  else "空"# 特殊处理
                    account = ele.xpath('.// div / table / tbody[2] / tr / td[5] / div / div[1] / p / strong / span[2]/text()')[0]
                    status =  ele.xpath('.// div / table / tbody[2]/ tr / td[6] / div / p / span / text()')[0]
                    info = {"订单号":order,"日期":date,"店铺名称":shop_title,"商品名称":name,"付款金额":account,"订单状态":status}
                    # print(info)
                    f.write(json.dumps(info,ensure_ascii=False))
                    f.write('\n')
                    # 写入spider.myorder 表中
                    spider_db.myorder.insert_one(info)
                except Exception as e :
                    print("写入数据错误",1)

if __name__ == '__main__':
    user = input("输入会员名/微博/手机号:")
    password = input("输入密码:")
    page = int(input("输入订单页数:"))
    # 创建驱动器对象           驱动器位置
    driver = webdriver.Firefox(executable_path="F:/火狐/geckodriver")
    login_url = "https://login.taobao.com/member/login.jhtml"
    wait = WebDriverWait(driver, 300)  # 显示等待 20秒元素加载
    driver.get(login_url)

    #连接MongoDB
    spider_db = Mongo_client(Mongo_ip,Mongo_port,Mongo_user,Mongo_pwd)

    # 登录
    taobao(user,password)
    time.sleep(2)
    # 进入我的订单 返回网页源码
    source = my_order()
    time.sleep(1)
    # 网站源码(第一页)
    tree = etree.HTML(source)

    # 筛选和写入数据
    filter_write_mongodb(tree)
    time.sleep(3)
    for i in range(page-1):
        # driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # time.sleep(0.5)
        page_next = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button.button-mod__button___2HDif:nth-child(2)')))
        page_next.click()
        time.sleep(1)
        tree = etree.HTML(driver.page_source)
        filter_write_mongodb(tree)
        time.sleep(2)
    driver.close()