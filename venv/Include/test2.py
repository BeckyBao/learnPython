#列表 元组 字典 集合
'''
#EMS项目练习

#显示系统欢迎信息
print('-'*20,'欢迎使用员工管理系统','-'*20)

#创建一个列表，用来存储员工的信息
emps = ['美少女\t18\t女\t城堡❤','大怪兽\t100\t男\t山洞']

#创建一个死循环
while True:
    #显示用户选项
    print('请选择要进行的操作：')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出员工')
    user_choose = input('请选择【1-4】：')
    # 打印分割线
    print('-' * 62)
    #根据用户选择进行后续操作
    if user_choose == '1':
        #查询员工
        #打印表头
        print(f'\t序号\t姓名\t年龄\t性别\t住址')
        #创建一个变量，表是员工序号
        n = 1
        #显示员工信息
        for emp in emps :
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_choose == '2':
        #添加员工
        #获取员工的信息，姓名 年龄 性别 住址
        emp_name = input('请输入员工的姓名：')
        emp_age = input('请输入员工的年龄：')
        emp_gender = input('请输入员工的性别：')
        emp_address = input('请输入员工的住址：')

        #创建员工信息
        emp = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        #显示一个提示信息
        print('以下员工将被添加到系统中')
        print('-' * 62)
        print(f'姓名\t年龄\t性别\t住址')
        print(emp)
        print('-' * 62)
        user_confirm = input('是否确认该操作？【y/n】')
        if(user_confirm == 'y' or user_confirm == 'yes'):
            #确认
            emps.append(emp)
            print('添加已成功！')
        else :
            #取消操作
            print('添加已取消！')
            pass
    elif user_choose == '3':
        #删除员工，根据员工序号来删除
        del_num = int(input('请输入要删除的员工序号：'))
        #判断序号是否有效
        if 0<del_num<=len(emps):
            #序号合法，通过序号来获取
            del_i = del_num -1;
            # 显示一个提示信息
            print('以下员工将被删除')
            print('-' * 62)
            print(f'\t序号\t姓名\t年龄\t性别\t住址')
            print(f'\t{del_num}\t{emps[del_i]}')
            print('-' * 62)
            user_confirm2 = input('是否确认该操作？【y/n】')
            if (user_confirm2 == 'y' or user_confirm2 == 'yes'):
                # 确认
                emps.pop(del_i)
                print('已删除成功！')
            else:
                # 取消操作
                print('删除已取消！')
                pass
        pass
    elif user_choose == '4':
        #退出
        input('感谢使用！再见【‘点击回车键退出系统】')
        break
    else :
        print('您的输入有误，请重新选择！')

    # 打印分割线
    print('-' * 62)
    '''
#元祖
my_tuple = 10,20,30,40
a,b,*c = my_tuple
print('a=',a)
print('c=',c)

