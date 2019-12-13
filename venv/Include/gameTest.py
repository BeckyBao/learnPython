#python练习 小游戏《唐僧大战白骨精》
#欢迎信息
print('-'*20,'欢迎光临《唐僧大战白骨精》','-'*20)

#显示身份选择信息
print('请选择你的身份：')
print('\t1.唐僧')
print('\t2.白骨精')

#身份选择
player_choose = input('请选择【1-2】：')

#分割线
print('-'*68)

#根据用户的选择来显示不同的提示信息
if player_choose == '1':
    #选择1
    print('您将以>唐僧<的身份来进行游戏')
elif player_choose == '2':
    # 选择2
    print('您竟然选择了白骨精！太不要脸了，系统将自动为您分配>唐僧<身份')
else :
    print('您的输入不合法，您将以>唐僧<的身份来进行游戏')

#进入游戏

#创建变量，来保存玩家的生命值和攻击力
player_life = 2 #基础生命值
player_attack = 2 #基础攻击力

#创建变量，保存boss的生命值和攻击力
boss_life = 10 #基础生命值
boss_attack = 10 #基础攻击力

#打印分割线
print('-'*68)
#显示玩家信息（生命值、攻击力）
print(f'唐僧，你的生命值是{player_life}，你的攻击力是{player_attack}')

#处理用户选择
while( True ):
    # 打印分割线
    print('-' * 68)
    # 显示游戏选项，游戏开始
    print('请选择你要进行的操作：')
    print('\t1.练级')
    print('\t2.打boss')
    print('\t3.逃跑')
    # 游戏选择
    game_choose = input('请选择【1-3】：')
    if game_choose == '1':
        #增加玩家生命值和攻击力
        player_life += 2
        player_attack += 2
        print(f'恭喜你升级了！你现在的生命值是{player_life}，攻击力是{player_attack}')
    elif game_choose == '2':
        #玩家攻击boss
        #boss反击玩家
        boss_life -= player_attack
        # 打印分割线
        print('-' * 68)
        print('>唐僧<攻击了白骨精')
        #检查boss是否死亡
        if(boss_life <= 0):
            #boss死亡，游戏结束
            print(f'>白骨精<受到了{player_attack}点伤害，┏┛墓┗┓...(((m-__-)m')
            #游戏结束
            print('恭喜闯关成功')
            break
        #boss反击玩家
        player_life -= boss_attack
        print('>白骨精<攻击了唐僧')
        #检查玩家是否死亡
        if player_life <= 0:
            #玩家死亡
            print(f'>唐僧<受到了{boss_attack}点伤害，┏┛墓┗┓...(((m-__-)m')
            # 游戏结束
            print('您已死亡，闯关失败')
            break
    elif game_choose == '3':
        # 游戏结束
        print('你逃跑了，闯关失败')
        break
    else:
        print('你输入有误，请重新输入')


