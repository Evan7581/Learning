##########################################################################
# -*- coding: utf-8 -*-
#
# for Python3 str learning practice
# 1. 开发敏感词过滤器，如果包含已知过滤词，则替换为“*****”，如“苍老师”“东京热”
# 2. 制作表格
#   - 循环提示用户输入用户名、密码、邮箱
#   - 要求用户输入长度不超过20个字符，如果超过，只有前20个字符有效
#   - 输入q或者Q时退出
#   - 最终以表格形式输出
# 3. 制作加法计算器
# 4. 制作随机验证码，不区分大小写
#   - 如果用户输入不对，再次生成验证码等待用户输入
#
##########################################################################
import sys
import random


def run_func(choose):
    if choose == 0:
        shield()
    elif choose == 1:
        info_register()
    elif choose == 2:
        calculator()
    elif choose == 3:
        verification_code()
    else:
        return 2


def calculator():
    print('I\m calculator')


def info_register():
    print('I\'m info_register')
    table_str = 'Name\tPassword\tE-mail\n'
    while True:
        user_name = input('请输入用户名：')
        if user_name == 'q' or user_name == 'Q':
            register_info_print(table_str)
            break
        user_pwd = input('请输入密码：')
        if user_pwd == 'q' or user_pwd == 'Q':
            register_info_print(table_str)
            break
        user_mail = input('请输入邮箱地址：')
        if user_mail == 'q' or user_mail == 'Q':
            register_info_print(table_str)
            break

        # user info need judge weather input is space and weather include '\t'
        if user_name and user_name.isprintable() is True:
            tmp_info = user_name.strip()[0:20] + '\t'
        else:
            print('用户名输入错误，退出输入!')
            register_info_print(table_str)
            break

        if user_pwd and user_pwd.isprintable() is True:
            tmp_info = tmp_info + user_pwd.strip()[0:20] + '\t'
        else:
            print('用户密码输入错误，退出输入!')
            register_info_print(table_str)
            break

        if user_mail and user_mail.isprintable() is True:
            table_str = table_str + tmp_info + user_mail.strip()[0:20] + '\n'
        else:
            print('用户邮箱输入错误，退出输入!')
            register_info_print(table_str)
            break

    print('用户信息录入完成')


def register_info_print(untreated_info):
    # untreated_info should come from function info_register()
    print('start expandtabs')
    if untreated_info:
        print(untreated_info.expandtabs(22))
    else:
        print('table info is empty!')

    return


def shield():
    print('I\'m shield')
    shield_word = ['苍老师', '东京热']
    user_input = input('please input what you want to say:')
    for index in range(0, len(shield_word)):
        user_input = user_input.replace(shield_word[index], '***')
    print(user_input)


# produce random code
# random code for 4 chars cover figure and capital
def check_code():
    checkcode = ''
    for i in range(4):
        current = random.randrange(0, 4)
        if current != i:
            temp = chr(random.randint(65, 90))
        else:
            temp = random.randint(0, 9)
        checkcode += str(temp)
    return checkcode


def verification_code():
    code = check_code()
    print('Welcome to Earth, please enter verification code ', code)
    enter_code = input('please feed in:')
    verify_times = 1
    while verify_times < 3:
        if enter_code.strip().upper() == code:
            print("Verify Pass! Welcome!")
            break
        else:
            code = check_code()
            verify_times += 1
            print('Verify Fail, please re-feed-in verification code', code)
            enter_code = input('please feed in:')
    else:
        print('Verify Fail, YOU NOT ALLOWED ENTER TO EARTH!!!')


if __name__ == '__main__':
    print(sys.argv[1])
    func_list = ['shield', 'info_register', 'calculator', 'verification_code']
    print('you can run below function:')
    for index in range(0, len(func_list)):
        print(index+1, ': ', func_list[index])
    func_choose = input('Please choose which function you want to run:')
    if func_choose.isdecimal():
        func_choose = int(func_choose) - 1
    else:
        print('input error, please input correct serial number')
        exit()
    if func_choose < len(func_list):
        print('run ', func_list[func_choose])
        run_func(func_choose)
    else:
        print('input error, please input correct serial number')
        exit()
    print('RUNNING DONE!')
