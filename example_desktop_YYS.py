import time, os

from numpy import true_divide
import auto_player as player

def get_pictures():   
    player.screen_shot()

def auto_play_yuhun(round=50):
    count = 0
    while count < round:       
        ar1 = ['start_yys', 'exp_yys',]
        re = player.find_touch_any(ar1)
        if re == 'start_yys':
            print('开始新一轮...')
            count += 1
            #time.sleep(10)
        elif re == 'exp_yys':
            print('领取奖励...')
        elif re is None:
            ar2 = ['going_yys',]
            re = player.find_touch_any(ar2, False)
            if re == 'goging_yys':
                print('托管中...')
                time.sleep(5)


def auto_play_yuhun1(round=50):
    count = 0
    while count < round:       
        ar1 = ['ht_accept_invite', 'ht_confirm', 'ht_tiaozhan', 'ht_shenli', 'ht_done']
        re = player.find_touch_all(ar1)
        if re == 'ht_tiaozhan':
            count += 1
            print('********* 开始第 %3d 轮 ***' % (count))
            time.sleep(10)
        elif re == 'ht_shenli':
            print('战斗胜利...')
            time.sleep(1)
        elif re == 'ht_done':
            print('领取奖励...')
            time.sleep(1)
        elif re is None:
            ar2 = ['ht_zidong',]
            re = player.find_touch_all(ar2, False)
            if re == 'ht_zidong':
                print('战斗中...')
                time.sleep(5)
        else:
            time.sleep(1)

def auto_play_yuhun2(round=200):
    count = 0
    while count < round:       
        ar1 = ['n_default_invite', 'n_accept_all', 'n_accept_invite', 'n_confirm', 'n_shenli', 'n_done', 'n_tiaozhan']
        re = player.find_touch_all(ar1)
        if re == 'n_tiaozhan':
            count += 1
            print('********* 开始第 %d 轮 共 %d 轮***' % (count, round))
            time.sleep(10)
        elif re == 'n_shenli':
            print('战斗胜利...')
        elif re == 'n_done':
            print('领取奖励...')
        elif re is None:
            ar2 = ['n_zidong',]
            re = player.find_touch_all(ar2, False)
            if re == 'n_zidong':
                print('战斗中...')
                time.sleep(5)

def auto_play_tupo(round=20):
    count = 0
    cl = ['tupo_target', 'tupo_attack']
    while count < round:
        re = player.cascade_find_touch(cl)
        if re == cl:
            count += 1
            print('********* 开始第 %d 轮 ***' % (count))
            time.sleep(2)
        else:
            re = player.find_touch_all(['tupo_reward'])
            if re == 'tupo_reward':
                print('突破奖励...')
                continue

            ar = ['tupo_refresh', 'tupo_confirm']
            re = player.cascade_find_touch(ar)
            if re == ar:
                print('突破完成一页，刷新...')
                continue

        while True:
            ar1 = ['tupo_ready1', 'tupo_ready2', 'tupo_ready3', 'tupo_fail', 'tupo_success']
            re = player.find_touch_all(ar1)
            if re == 'tupo_success':
                print('突破胜利...')
                time.sleep(2)
                break
            elif re == 'tupo_fail':
                print('突破失败...')
                time.sleep(2)
                break
            elif re is None:
                ar2 = ['tupo_auto',]
                re = player.find_touch_all(ar2, False)
                if re == 'tupo_auto':
                    print('战斗中...')
                    time.sleep(3)
    print("Finished %d round" % (count))

def auto_play_tupo1(playernum=1):
    round = playernum * 30
    count = 0
    tp_start = ['tupo_target', 'tupo_attack']
    while count < round:
        fight_status = player.find_touch_all(['tupo_ready1', 'tupo_ready2', 'tupo_ready3',
                                            'tupo_fail', 'tupo_success', 'tupo_reward'],
                                            True, True, True)
        if fight_status == 'tupo_success':
            print('突破胜利...')
        elif fight_status == 'tupo_fail':
            print('突破失败...')
        elif fight_status is None:
            fight_status = player.find_touch_all(['tupo_auto'], False)
            if fight_status == 'tupo_auto':
                print('战斗中...')

        re = player.cascade_find_touch(tp_start)
        if re == tp_start:
            count += 1
            print('********* 开始第 %d 轮，  共 %d 轮***' % (count, round))

        re_list = player.tupo_check_refresh()
        if re_list:
            print("check reresh done: ", re_list)
        # ar = ['tupo_refresh', 'tupo_confirm']
        # re = player.cascade_find_touch(ar)
        # if re == ar:
        #     print('突破完成一页，刷新...')
        #     continue

    print("Finished %d round" % (count))

def one_player_tupo():
    auto_play_tupo1(1)

def two_player_tupo():
    auto_play_tupo1(2)

def three_player_tupo():
    auto_play_tupo1(3)
        
def get_cursor_pos():
    x, y = player.get_mouse_pos()
    print("当前鼠标位置： X %d   Y %d" % (x, y))

def menu(debug=False):

    menu_list = [
    [get_pictures, '获取当前屏幕截图'],
    [get_cursor_pos, '获取当前鼠标位置'],
    [auto_play_yuhun1, '自动御魂_模拟器'],
    [auto_play_yuhun2, '自动御魂_桌面版'],
    [one_player_tupo, '自动突破_单窗口'],
    [two_player_tupo, '自动突破_双窗口'],
    [three_player_tupo, '自动突破_三窗口'],
    ]

    start_time = time.time()
    print('程序启动，当前时间', time.ctime(), '\n')
    while True:
        i = 0
        for func, des in menu_list:
            msg = str(i) + ": " + des + '\n'
            print(msg)
            i += 1
        player.alarm(1)
        raw = input("选择功能模式：") if not debug else 1
        index = int(raw) if raw else 1
        func, des = menu_list[index]
        print('已选择功能： ' + des)
        func()

if __name__ == '__main__':
    menu()
