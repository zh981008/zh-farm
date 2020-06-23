import uiautomator2 as u2
import time
from utils import *
from cv import *
from Automator import *
import matplotlib.pylab as plt


# plt.ion()
# fig, ax = plt.subplots(1)
# plt.show()

a = Automator()
a.start()

def login_auth(ac,pwd):
    need_auth = a.login(ac=ac,pwd=pwd)
    if need_auth:
        auth_name,auth_id = random_name(), CreatIDnum()
        a.auth(auth_name =auth_name ,auth_id = auth_id)

def init_acc():#原作者的初始号初始化函数，不适用于农场号
    while True:

        screen_shot = a.d.screenshot(format="opencv")
        state_flag = a.get_screen_state(screen_shot)

        if state_flag=='dark':
            print('画面变暗,尝试进入引导模式点击')
            screen_shot = a.d.screenshot(format="opencv")
            a.jiaoxue(screen_shot)

        elif state_flag=='zhandou':
            print('侦测到加速按钮, 进入战斗模式')
            a.zhandou()
        elif state_flag=='shouye':
            print('恭喜完成所有教学内容, 跳出循环')
            a.d.click(1, 1)
            time.sleep(1)            
            break
        else:
            template_paths = ['img/tiaoguo.jpg', 'img/ok.jpg','img/xiayibu.jpg', 'img/caidan.jpg', 'img/caidan_yuan.jpg',
                                      'img/caidan_tiaoguo.jpg', 'img/dengji.jpg','img/tongyi.jpg','img/niudan_jiasu.jpg']
            a.guochang(screen_shot,template_paths)


def init_home():
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(1,1)
        time.sleep(0.5)#保证回到首页    
    time.sleep(0.5)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(1,1)
        time.sleep(0.2)#保证回到首页
        a.d.click(100,505)



def shouqu():#收取全部礼物

    while True:#锁定回到首页
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(100,505)
        time.sleep(0.3)
        a.d.click(1,1)
    a.guochang(screen_shot_, ['img/liwu.jpg'],suiji=0)
    while True:#锁定收取履历（礼品盒）
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/shouqulvli.jpg'):
            a.guochang(screen_shot_, ['img/quanbushouqu.jpg'],suiji=0)
            time.sleep(1)
            a.d.click(589,472)#2020-5-29 19:41 bug fixed            
            break
    while True:#锁定回到首页
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(1,1)#礼品盒有特殊性，不能点（100,505），会被挡住
        time.sleep(0.3)


def shouqurenwu():#收取任务报酬

    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/renwu.jpg'):
            a.guochang(screen_shot_, ['img/renwu.jpg'],suiji=0)
            break
        a.d.click(1,1)
        time.sleep(1)
    while True:#锁定全部收取
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/quanbushouqu.jpg'):
            a.guochang(screen_shot_, ['img/quanbushouqu.jpg'],suiji=0)
            time.sleep(1)
            break
    while True:#锁定ok
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/guanbi.jpg'):
            a.guochang(screen_shot_, ['img/guanbi.jpg'],suiji=0)
            time.sleep(1)
            break
    while True:#锁定回到首页
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(100,505)
        time.sleep(0.5)


def niudan():#扭蛋函数
    a.d.click(751,505)
    time.sleep(1)
    while True:
        time.sleep(1)
        active_list = ['img/sheding.jpg','img/ok.jpg','img/niudan_jiasu.jpg','img/zaicichouqu.jpg','img/shilian.jpg']
        screen_shot = a.d.screenshot(format="opencv")
        a.guochang(screen_shot,active_list, suiji=1)
        screen_shot_ = a.d.screenshot(format="opencv")
        state_flag = a.get_screen_state(screen_shot_)
        if state_flag == 'baoshigoumai':
            print('没钱了, 关闭')
            a.d.click(373, 370)
            break

def goumaimana():
    a.d.click(189,62)
    while True:#锁定取消2
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/quxiao2.jpg'):
            break
        a.d.click(189,62)
        time.sleep(0.5)
    a.d.click(596,471)#第一次购买的位置
    while True:#锁定ok
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/ok.jpg'):
            a.guochang(screen_shot_, ['img/ok.jpg'],suiji=0)
            break
    for i in range(7):#购买剩下的7次
        while True:#锁定取消2
            screen_shot_ = a.d.screenshot(format="opencv")
            if a.is_there_img(screen_shot_,'img/quxiao2.jpg'):
                break
        a.d.click(816,478)#购买10次
        while True:#锁定ok
            screen_shot_ = a.d.screenshot(format="opencv")
            if a.is_there_img(screen_shot_,'img/ok.jpg'):
                a.guochang(screen_shot_, ['img/ok.jpg'],suiji=0)
                break
    while True:#锁定首页
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(1,1)
        time.sleep(0.5)#保证回到首页



def write_log(account, pwd):#识别box函数
    time.sleep(1)
    a.d.click(209, 519)
    time.sleep(1)
    a.d.click(659, 30)
    time.sleep(1)
    a.d.click(728, 142)
    time.sleep(1)
    a.d.click(588, 481)
    time.sleep(1)

    base_path = 'img/touxiang/'
    touxiang_path_list = []
    for touxiang_path in os.listdir(base_path):
        touxiang_path_list.append(base_path+touxiang_path)
    screen_shot = a.d.screenshot(format="opencv")
    exist_list = a.get_butt_stat(screen_shot, touxiang_path_list)
    print(exist_list)
    st = ''
    for i in exist_list:
        st = st + str(os.path.basename(i).split('.')[0]) + ','
    with open('jieguo.txt', 'a') as f:
        f.write(account+'\t'+ pwd+'\t'+st+'\n')

def change_acc():#切换账号
    time.sleep(1)
    a.d.click(871, 513)
    a.d.click(871, 513)
    a.d.click(871, 513)
    time.sleep(1)
    find_click('main_page/go_back_title.png')
    time.sleep(1)
    find_click('img/ok.jpg')
    time.sleep(1)

def goumaitili():#购买体力，注意此函数参数默认在首页执行，其他地方执行要调整参数
    for i in range(3):
        while True:
            screen_shot_ = a.d.screenshot(format="opencv")
            if a.is_there_img(screen_shot_,'img/liwu.jpg'):
                break
            a.d.click(100,505)
            time.sleep(1)#首页锁定，保证回到首页
        a.d.click(320,31)
        time.sleep(1)
        screen_shot = a.d.screenshot(format="opencv")
        a.guochang(screen_shot,['img/ok.jpg'], suiji=0)
        time.sleep(1)
        screen_shot = a.d.screenshot(format="opencv")
        a.guochang(screen_shot,['img/zhandou_ok.jpg'], suiji=1)
        a.d.click(100,505)#点击一下首页比较保险

def find_click(name):
    for i in range(10):
        screen_shot_ = a.d.screenshot(format="opencv")
        flag = a.is_there_img(screen_shot_, name)
        if flag:
            x,y = flag
            a.d.click(x, y)
            time.sleep(0.5)
            return
    print("not found"+name)



def hanghui():#自动行会捐赠
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(100,505)
        time.sleep(1)#首页锁定，保证回到首页
    time.sleep(1)
    a.d.click(693, 436)
    time.sleep(1)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        state_flag = a.get_screen_state(screen_shot_)
        if state_flag == 'hanghui':
            find_click('img/juanzeng.jpg')
            time.sleep(1)
            find_click('img/max.jpg')
            time.sleep(1)
            find_click('img/hanghui_ok.jpg')
            time.sleep(1)
            break
    a.d.click(100, 505)
    time.sleep(1)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(100,505)
        a.d.click(1,1)
        time.sleep(1)#首页锁定，保证回到首页


def shuatuzuobiao(x, y, times=1):#刷图函数，xy为该图的坐标，times为刷图次数
    a.d.click(x,y)
    time.sleep(0.5)
    while True:#锁定加号
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/jiahao.jpg'):
            break
        a.d.click(x,y)
        time.sleep(0.5)
    screen_shot = a.d.screenshot(format="opencv")
    for i in range(times-1):#基础1次
        a.guochang(screen_shot,['img/jiahao.jpg'])
        time.sleep(0.2)
    time.sleep(0.3)
    a.d.click(758,330)#使用扫荡券的位置 也可以用OpenCV但是效率不够而且不能自由设定次数
    time.sleep(0.3)
    # screen_shot = a.d.screenshot(format="opencv")
    # a.guochang(screen_shot,['img/shiyongsanzhang.jpg'])
    screen_shot = a.d.screenshot(format="opencv") 
    a.guochang(screen_shot,['img/ok.jpg'])
    while True:
        a.d.click(1,1)
        time.sleep(0.3)
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/normal.jpg'):
            break
def shuatutiaozhan(x,y,direction = True,times=1):
    if direction:
        a.d.drag(600, 270, 200, 270, 0.1)  # 最右
    else:
        a.d.drag(200, 270, 600, 270, 0.1)  # 拖拽到最左

    time.sleep(5)
    a.d.click(x, y)
    print("click"+str(x)+","+str(y))
    time.sleep(0.5)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_, 'img/tiaozhan.jpg'):
            a.d.click(842, 464)
            break
        time.sleep(0.5)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_, 'img/zhandoukaishi.png'):
            a.d.click(829, 449)
            break
        time.sleep(0.5)
    time.sleep(30)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        a.d.click(476, 372) # 升级
        time.sleep(0.5)
        a.d.click(378, 378)  # 限时商店
        if a.is_there_img(screen_shot_, 'img/xiayibu.jpg'):
            a.d.click(839, 497)
            break
        time.sleep(0.5)
    time.sleep(1)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_, 'img/xiayibu.jpg'):
            a.d.click(839, 497)
            break
        if a.is_there_img(screen_shot_, 'img/expedition/return_expedition.png'):
            a.d.click(825, 491)
            break
        time.sleep(0.5)

    for i in range(3):
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_, 'img/guanbi.jpg'):
            a.d.click(839, 497)
            break
        time.sleep(0.5)

def shuatufaster(flag = 1):
    #进入冒险
    a.d.click(480, 505)
    time.sleep(0.5)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        #print(screen_shot_)
        print("find zhuxian")
        a.d.click(480, 505)
        if a.is_there_img(screen_shot_,'img/zhuxianguangka.png'):
            break
    a.d.click(562, 253)
    time.sleep(1)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        print("find normal")
        if a.is_there_img(screen_shot_,'img/normal.jpg'):
            break

    if flag == 1:
        a.d.drag(200, 270, 600, 270, 0.1)  # 拖拽到最左
        time.sleep(2)
        shuatuzuobiao(518,332,4)#10-5
        shuatuzuobiao(603,238,4)#10-4
        shuatuzuobiao(430,239,4)#10-3
        shuatuzuobiao(287,206,4)#10-2
        shuatuzuobiao(146,197,4)#10-1
        shuatuzuobiao(594,429,10)#10-7
        shuatuzuobiao(411,408,10)#10-6
        shuatuzuobiao(690,362,30)#10-8
    else:
        a.d.drag(600, 270, 200, 270, 0.1)  # 最右
        time.sleep(2)
        shuatuzuobiao(583, 259,30)

    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(100,505)
        time.sleep(1)#保证回到首页

def shuatu():#刷图函数 注意此函数要在首页运行
    #进入冒险
    # a.d.click(480, 505)
    # time.sleep(0.5)
    # while True:
    #     screen_shot_ = a.d.screenshot(format="opencv")
    #     #print(screen_shot_)
    #     print("find zhuxian")
    #     if a.is_there_img(screen_shot_,'img/zhuxianguangka.png'):
    #         break
    # a.d.click(562, 253)
    # time.sleep(1)
    # while True:
    #     screen_shot_ = a.d.screenshot(format="opencv")
    #     print("find normal")
    #     if a.is_there_img(screen_shot_,'img/normal.jpg'):
    #         break
    # shuatutiaozhan(374, 234,1) #1-4
    # shuatutiaozhan(481, 284,1) #1-5
    # shuatutiaozhan(547, 374)#1-6
    # shuatutiaozhan(606, 305)#1-7
    # shuatutiaozhan(641, 217)#1-8
    # shuatutiaozhan(735, 232)#1-9
    # shuatutiaozhan(842, 324)#1-10
    # shuatutiaozhan(842, 324)

    # shuatutiaozhan(132, 414,False)  # 2-1
    # shuatutiaozhan(249, 414,False)  # 2-2
    # shuatutiaozhan(387, 378,False)  # 2-3
    # shuatutiaozhan(322, 266,False)  # 2-4
    # shuatutiaozhan(228, 214,False)  # 2-5
    # shuatutiaozhan(341, 170,False)  # 2-6
    # shuatutiaozhan(443, 234,False)  # 2-7
    # shuatutiaozhan(506, 320,False)  # 2-8
    # shuatutiaozhan(606, 368,False)  # 2-9
    # shuatutiaozhan(731, 372,False) # 2-10
    # shuatutiaozhan(835, 345,False) # 2-11
    # shuatutiaozhan(823, 241,False) # 2-12

    # shuatutiaozhan(128, 184) #3-1
    # shuatutiaozhan(195, 314) #3-2
    # shuatutiaozhan(293, 218) #3-3
    # shuatutiaozhan(420, 239)  # 3-4
    # shuatutiaozhan(395, 334)  # 3-5
    # shuatutiaozhan(478, 424)  # 3-6
    # shuatutiaozhan(522, 299)  # 3-7
    # shuatutiaozhan(635, 191)  # 3-8
    # shuatutiaozhan(698, 262)  # 3-9
    # shuatutiaozhan(685, 395)  # 3-10
    # shuatutiaozhan(821, 353) # 3-11
    # shuatutiaozhan(821, 214) # 3-12
    #
    # for i in range(3):
    #     screen_shot_ = a.d.screenshot(format="opencv")
    #     flag = a.is_there_img(screen_shot_, 'img/tiaozhan.jpg')
    #     if flag:
    #         x,y = flag
    #         a.d.click(x, y)
    #         time.sleep(0.5)
    #         break
    # shuatutiaozhan(199, 243,False)  # 4-1
    # shuatutiaozhan(295, 314,False)  # 4-2
    # shuatutiaozhan(401, 262,False)  # 4-3
    # shuatutiaozhan(510, 249,False)  # 4-4
    # shuatutiaozhan(503, 370,False)  # 4-5
    # shuatutiaozhan(631, 351,False)  # 4-6
    # shuatutiaozhan(257, 224)  # 4-7
    # shuatutiaozhan(360, 280)  # 4-8
    # shuatutiaozhan(480, 228)  # 4-9
    # shuatutiaozhan(608, 255)  # 4-10
    # shuatutiaozhan(746, 249)  # 4-11
    # shuatutiaozhan(773, 326)  # 4-12
    # shuatutiaozhan(645, 418)  # 4-13
    # # #
    # #
    # for i in range(5):
    #     screen_shot_ = a.d.screenshot(format="opencv")
    #     flag = a.is_there_img(screen_shot_, 'img/guanbi.jpg')
    #     if flag:
    #         x,y = flag
    #         a.d.click(x, y)
    #         time.sleep(0.5)
    #         break
    # shuatutiaozhan(134, 187,False)  # 5-1
    # shuatutiaozhan(259, 182,False)  # 5-2
    # shuatutiaozhan(357, 230,False)  # 5-3P
    # shuatutiaozhan(501, 234,False)  # 5-4
    # shuatutiaozhan(443, 320,False)  # 5-5
    # shuatutiaozhan(353, 407,False)  # 5-6
    # shuatutiaozhan(547, 422,False)  # 5-7

    # shuatutiaozhan(197, 382)  # 5-8
    # shuatutiaozhan(297, 305)  # 5-9
    # shuatutiaozhan(426, 372)  # 5-10
    shuatutiaozhan(489, 272)  # 5-11
    shuatutiaozhan(600, 243)  # 5-12
    shuatutiaozhan(737, 245)  # 5-13

    for i in range(5):
        screen_shot_ = a.d.screenshot(format="opencv")
        flag = a.is_there_img(screen_shot_, 'img/guanbi.jpg')
        if flag:
            x,y = flag
            a.d.click(x, y)
            time.sleep(0.5)
            break
    #
    shuatutiaozhan(203, 376, False)  # 6-1
    shuatutiaozhan(301, 291, False)  # 6-2
    shuatutiaozhan(401, 272, False)  # 6-3
    shuatutiaozhan(389, 393, False)  # 6-4
    shuatutiaozhan(522, 349, False)  # 6-5
    shuatutiaozhan(637, 397, False)  # 6-6
    shuatutiaozhan(645, 255, False)  # 6-7
    shuatutiaozhan(771, 228, False)  # 6-8

    shuatutiaozhan (247, 339)  # h1-1
    shuatutiaozhan 	(462, 255)  # h1-2
    shuatutiaozhan 	(700, 311)  # h1-3
    shuatutiaozhan(293, 255)  # h2-1
    shuatutiaozhan(464, 347)  # h2-1
    shuatutiaozhan(718, 335)  # h2-1

    shuatutiaozhan(255, 259)  # h3-1
    shuatutiaozhan(480, 328)  # h3-1
    shuatutiaozhan(733, 278)  # h3-1
    shuatutiaozhan(257, 276)  # h4-1
    shuatutiaozhan(497, 226)  # h4-1
    shuatutiaozhan(785, 245)  # h4-1

    # shuatuzuobiao(821,299,3)#10-17
    # shuatuzuobiao(703,328,3)#10-16
    # shuatuzuobiao(608,391,3)#10-15
    # shuatuzuobiao(485,373,3)#10-14
    # shuatuzuobiao(372,281,3)#10-13
    # shuatuzuobiao(320,421,3)#10-12
    # shuatuzuobiao(172,378,3)#10-11
    # shuatuzuobiao(251,235,3)#10-10
    # shuatuzuobiao(111,274,3)#10-9
    #
    # a.d.drag(200,270,600,270,0.1)#拖拽到最左
    # time.sleep(2)
    #
    # shuatuzuobiao(690,362,3)#10-8
    # shuatuzuobiao(594,429,3)#10-7
    # shuatuzuobiao(411,408,3)#10-6
    # shuatuzuobiao(518,332,3)#10-5
    # shuatuzuobiao(603,238,3)#10-4
    # shuatuzuobiao(430,239,3)#10-3
    # shuatuzuobiao(287,206,3)#10-2
    # shuatuzuobiao(146,197,3)#10-1

    # while True:
    #     screen_shot_ = a.d.screenshot(format="opencv")
    #     if a.is_there_img(screen_shot_,'img/liwu.jpg'):
    #         break
    #     a.d.click(100,505)
    #     time.sleep(1)#保证回到首页

def expedition():
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        flag = a.is_there_img(screen_shot_, 'img/expedition/experience.png')
        if flag:
            x,y = flag
            a.d.click(x, y)
            time.sleep(0.5)
            break
    shuatutiaozhan(658, 149)
    shuatutiaozhan(658, 149)
    time.sleep(0.5)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        flag = a.is_there_img(screen_shot_, 'img/expedition/mana.png')
        if flag:
            x, y = flag
            a.d.click(x, y)
            time.sleep(0.5)
            break
    shuatutiaozhan(658, 149)
    shuatutiaozhan(658, 149)
    a.d.click(38, 34)
    time.sleep(0.5)

def join_farm():
    a.d.click(96, 507)
    time.sleep(1)
    find_click('img/hanghui.png')
    time.sleep(1)
    # find_click('img/hanghuisheding.png')
    # time.sleep(5)
    # while True:
    #     a.d.click(855.0, 80.0)
    #     time.sleep(1)
    #     screen_shot_ = a.d.screenshot(format="opencv")
    #     flag = a.is_there_img(screen_shot_, 'img/guild/guild_serch.png')
    #     if flag:
    #         time.sleep(1)
    #         break
    # time.sleep(1)
    # a.d.click(493, 180)
    # time.sleep(2)
    # a.d(text="请输入行会名").send_keys("zhfarm")
    # time.sleep(2)
    # a.d.click(493, 180)
    # a.d.click(562, 430)
    # find_click('img/zhfarm.png')
    # time.sleep(5)
    # a.d.click(835, 447)
    # time.sleep(1)
    # a.d.click(591, 376)
    # time.sleep(1)
    a.d.click(113, 499)
    time.sleep(1)
    return
def flatter():
    a.d.click(96, 507)
    time.sleep(1)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_, 'img/hanghui.png'):
            a.d.click(687, 430)
            break
        time.sleep(0.5)
    time.sleep(1)

    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_, 'img/guild/member_info.png'):
            a.d.click(247, 355)
            break
        time.sleep(0.5)
    time.sleep(1)

    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_, 'img/guild/guild_zhfarm.png'):
            a.d.click(641, 91)
            break
        time.sleep(0.5)
    time.sleep(1)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_, 'img/ok.jpg'):
            a.d.click(510, 232)
            a.d.click(583, 368)
            break
        time.sleep(0.5)
    time.sleep(1)
    a.d.click(823, 197)
    time.sleep(1)
    for i in range(3):
        a.d.click(92, 495)

# def write_log():
#     time.sleep(1)



def dixiacheng():#地下城
    a.d.click(480, 505)
    time.sleep(1) 
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        state_flag = a.get_screen_state(screen_shot_)
        if state_flag == 'maoxian':
            break
        a.d.click(480, 505)
        time.sleep(1)
    a.d.click(900, 138)
    time.sleep(1)

    #下面这段因为调试而注释了，实际使用时要加上
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        state_flag = a.get_screen_state(screen_shot_)
        if state_flag == 'yunhai':
            a.d.click(233, 311)
            time.sleep(1)
            while True:
                screen_shot_ = a.d.screenshot(format="opencv")
                if a.is_there_img(screen_shot_,'img/ok.jpg'):
                    break
                else:
                    a.d.click(233, 311)
                    time.sleep(1)
            a.guochang(screen_shot_, ['img/ok.jpg'],suiji=0)
            time.sleep(1) 
            break


    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/chetui.jpg'):
            break
        else:
            a.d.click(470, 434)
            time.sleep(1)
    time.sleep(1)
    a.d.click(667, 360)#1层
    time.sleep(1)
    a.d.click(833, 456)#挑战
    time.sleep(1)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/zhiyuan.jpg'):
            break
    a.d.click(100, 173)#第一个人
    time.sleep(1)
    screen_shot = a.d.screenshot(format="opencv")
    a.guochang(screen_shot, ['img/zhiyuan.jpg'],suiji=0)
    
    if a.is_there_img(screen_shot_,'img/dengjixianzhi.jpg'):
        a.d.click(213, 208)#如果等级不足，就支援的第二个人
        time.sleep(1)    
    else:
        a.d.click(100, 173)#支援的第一个人
        time.sleep(1)
    
    a.d.click(833, 470)#战斗开始
    time.sleep(1)
    while True:
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/ok.jpg'):
            a.guochang(screen_shot_, ['img/ok.jpg'],suiji=0)
            break


    while True:#战斗中快进
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/caidan.jpg'):
            a.guochang(screen_shot_, ['img/kuaijin.jpg'],suiji=0)
            a.guochang(screen_shot_, ['img/kuaijin_1.jpg'],suiji=0)
            break
    while True:#结束战斗返回
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/shanghaibaogao.jpg'):
            a.guochang(screen_shot_,['img/xiayibu.jpg','img/qianwangdixiacheng.jpg'], suiji=0)
            break
    a.d.click(1, 1)#取消显示结算动画
    time.sleep(1)
    find_click('img/white_ok.png')
    time.sleep(1)
    find_click('img/chetui.jpg')
    time.sleep(1)
    find_click('img/ok.jpg')
    time.sleep(1)
    while True:#首页锁定
        screen_shot_ = a.d.screenshot(format="opencv")
        if a.is_there_img(screen_shot_,'img/liwu.jpg'):
            break
        a.d.click(100,505)
        time.sleep(1)#保证回到首页
#%%
#==============================================================================
#主程序
#join_farm()
account_dic = {}
#expedition()
#join_farm()
# dixiacheng()
# change_acc()
#dixiacheng()
#dixiacheng()  # 地下城
# flatter()
# goumaitili()  # 购买3次体力
# shuatufaster()  # 刷全部10图3次
# hanghui()#行会捐赠
#dixiacheng()
# change_acc()
# goumaitili()  # 购买3次体力
# shuatufaster()  # 刷全部10图3次
#shuatu()

#hanghui()
# hanghui()  # 行会捐赠
# shuatufaster()
#change_acc()
# goumaitili()  # 购买3次体力
# shuatufaster()  # 刷全部10图3次
with open('zhanghao.txt','r') as f:
    for i,line in enumerate(f):
        #print(line)
        account,password = line.split(',')[0:2]
        account_dic[account]=password.strip()


# dixiacheng()  # 地下城
# # goumaitili()#购买3次体力
# shuatufaster()  # 刷全部10图3次
#change_acc()
for account in account_dic:
    print(account, account_dic[account])
    login_auth(account, account_dic[account])

    #init_acc()#账号初始化

    init_home()#初始化，确保进入首页
    shouqurenwu()#收取任务

    # shuatu()
    shouqu()#收取所有礼物
    flatter()
    #expedition()
    #init_home()
    hanghui()#行会捐赠
    #dixiacheng()#地下城
    #goumaitili()#购买3次体力
    #shuatufaster()#刷全部10图3次
    #join_farm()



    #box管理功能，未启用
    # niudan()#扭蛋扭光钻石
    # write_log(account, account_dic[account])#列出box内容在jieguo.txt

    change_acc()#退出当前账号，切换下一个
    time.sleep(3)#确保切换账号稳定性