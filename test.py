# coding=utf
"""
author=Hui_T
"""
from lxml import etree


# print("123人付款".split("人")[0]) # 123
# l = [<Element div at 0x1fccd2b4308>, <Element div at 0x1fccd2b49c8>, <Element div at 0x1fccd2b4348>, <Element div at 0x1fccd2b4708>, <Element div at 0x1fccd2b4788>, <Element div at 0x1fccd2b4848>, <Element div at 0x1fccd2b4408>, <Element div at 0x1fccd2b46c8>, <Element div at 0x1fccd2b4b08>, <Element div at 0x1fccd2b4888>, <Element div at 0x1fccd2b4b48>, <Element div at 0x1fccd2b4b88>, <Element div at 0x1fccd2b4bc8>, <Element div at 0x1fccd2b4c08>, <Element div at 0x1fccd2b4c48>, <Element div at 0x1fccd2b4c88>, <Element div at 0x1fccd2b4cc8>, <Element div at 0x1fccd2b4d08>, <Element div at 0x1fccd2b4d48>, <Element div at 0x1fccd2b4d88>]
# l = [1, 2, 3,4, 5, 6, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

doc='''
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>测试bs4</title>
</head>
<body>
    <div>
        <p>百里守约</p>
    </div>
    <div class="song">
        <p>李清照</p>
        <p>王安石</p>
        <p>苏轼</p>
        <p>柳宗元</p>
        <a href="http://www.song.com/" title="赵匡胤" target="_self">
            <span>this is span</span>
        宋朝是最强大的王朝，不是军队的强大，而是经济很强大，国民都很有钱</a>
        <a href="" class="du">总为浮云能蔽日,长安不见使人愁</a>
        <img src="http://www.baidu.com/meinv.jpg" alt="" />
    </div>
    <div class="tang">
        <ul>
            <li><a href="http://www.baidu.com" title="qing">清明时节雨纷纷,路上行人欲断魂,借问酒家何处有,牧童遥指杏花村</a></li>
            <li><a href="http://www.163.com" title="qin">秦时明月汉时关,万里长征人未还,但使龙城飞将在,不教胡马度阴山</a></li>
            <li><a href="http://www.126.com" alt="qi">岐王宅里寻常见,崔九堂前几度闻,正是江南好风景,落花时节又逢君</a></li>
            <li><a href="http://www.sina.com" class="du">杜甫</a></li>
            <li><a href="http://www.dudu.com" class="du">杜牧</a></li>
            <li><b>杜小月</b></li>
            <li><i>度蜜月</i></li>
            <li><a href="http://www.haha.com" id="feng">凤凰台上凤凰游,凤去台空江自流,吴宫花草埋幽径,晋代衣冠成古丘</a></li>
        </ul>
    </div>
</body>
</html>
'''
# tree = etree.HTML(doc)
# s = tree.xpath("//div[@class='tang']/ul/li/a/text()")
# l = []
# print(l[0] or "空")
# ----
# l = []
# dic = {"1":l if l else "ko"}
# print(dic['1'])
# ----