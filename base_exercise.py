#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # 姓名列表
    name_list = ['Tom','Hanmeimei','Kate','Kitty','John']
    # 数字列表
    score_list = [100, 99, 70, 88, 98]
    # 打印列表索引为3的元素
    print(name_list[3], score_list[3])
    # 打印列表倒数第一个的元素
    print(name_list[-1], score_list[-1])
    print("--------------------------------------------")

    # 取出列表中从第一个元素开始到倒数第一个的元素结束的所有元素
    new_name_list = name_list[0:-1]
    # 取出列表中从第一个元素开始到第四个元素结束的所有元素
    new_score_list = score_list[0:4]
    print(new_name_list)
    print(new_score_list)
    print("--------------------------------------------")

    # 如果姓名列表的长度大于3，就打印下面一行字
    if len(name_list) > 3:
        print("The number of elements in name_list is larger than 3")
    else:
        # 否则就打印下面长度不超过3的字符
        print("The number of elements in name_list is not larger than 3")
    print("--------------------------------------------")

    # 分数空字典
    score_dict = {}
    # 对一个姓名列表，既遍历索引又要遍历元素时
    for idx, name in enumerate(name_list):
        #修改
        score_dict[name] = score_list[idx]
    print(score_dict)
    print("--------------------------------------------")

    Kate_score = score_dict['Kate']
    print("Kate_score is", Kate_score)
    print("--------------------------------------------")

    print("The type of name_list is", type(name_list))
    print("The type of combine_dict is", type(score_dict))
    print("--------------------------------------------")

    total_score = 0
    for score in score_list:
        total_score += score
    print("The total score is %d \n" % total_score)

    