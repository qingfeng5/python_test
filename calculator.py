#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import需要的模块
from sys import version_info
#判断当前运行的python版本，如果是python2，则IS_PYTHON_2为True，否则为False
IS_PYTHON_2 = version_info.major == 2

#如果是偶数，则计算 2+4+...+n 的值
def function_even(n): 
    #最终输出的总和，先赋值为0
    sum = 0
    #从2开始，直到n，每隔2个循环一次，i取值依次为2,4,6,...,n
    for i in range(2, n + 1, 2):
        #累加计算总和
        sum += i
    #返回结果   
    return sum
 
#如果是奇数，则计算 1+3+...+n 的值
def function_odd(n):
    #最终输出的总和，先赋值为0
    sum = 0
    #从1开始，直到n，每隔2个循环一次，i取值依次为1,3,5,...,n
    for i in range(1, n + 1, 2):
        #累加计算总和
        sum += i
    #返回结果    
    return sum

def main(n):
    #判断是否数字，否则输出错误信息，并返回
    if not n.isdigit():
        print("Error! It is not a number.")
        return
    #类型转换，把str转为int
    n = int(n)
    #通过if判断是奇数还是偶数
    if n % 2 == 0:
        #如果是偶数，则传参调用函数function_even
        sum = function_even(n)
    else:
        #如果是奇数，则传参调用函数function_odd
        sum = function_odd(n)
    #打印结果
    print("The result is ", sum)

#代码运行入口
if __name__ == '__main__':
    #判断python版本，如果是python2
    if IS_PYTHON_2:
        #获取输入
        n = raw_input("Please input a number:\n")
    #判断python版本，如果不是python2
    else:
        #获取输入
        n = input("Please input a number:\n")
    #调用main函数
    main(n)
