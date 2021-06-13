print('*'*10,'请输入你的级别','*'*10)
level = int(input())
if level == 1:
    print('免费关卡随便玩。。。')
else:
    print('本关卡需要充值!请输入充值金额：')
    money = int(input())
    if money % 100 == 0 and money > 0:
        print('充值成功，您充值的金额为：',money)
    else:
        print('您充值的金额有误，充值的金额必须时100的倍数!!!')