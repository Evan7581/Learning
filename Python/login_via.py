# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
i=0

while i<10:
    if i != 6:
        print(i+1)
    i+=1
    
print('done')
'''
import sys

via_name="Evan"
via_password="Happy123"

via_num=3
via_fail_num=0

while via_fail_num < via_num:
    
    user_name=input('请输入用户名：')
    user_password=input('请输入密码：')
    
    if user_name == via_name:
        if user_password == via_password:
            print("用户验证通过")
            break
        else:
            print("密码错误")
            via_fail_num += 1
    else:
        print("用户名错误，请重新输入")
        via_fail_num += 1
        
    if via_fail_num == via_num:
        print("用户验证失败")
        sys.exit(1)
    else:
        continue

print("欢迎使用Python3.7")