# coding=utf-8
'''
Created on 2018年9月4日

@author: baron
'''
import random
from lottery_conf import *

def weighted_random(items):
    """抽奖算法"""
    '''计算概率和'''
    total = sum(w for _, w in items)
    '''生成概率范围内的随机数'''
    n = random.uniform(0, total)
    '''遍历概率空间'''
    for x, w in items:
        '''判断n是否在w区间内'''
        if n < w: 
            break
        '''如果不在，则向后遍历'''
        n = n - w 
    return x 

def try_times_by_high(total_times, ssr_up):
    """连续抽：高级"""
    item_list = []
    for time_no in range(0, total_times):
        '''确定级别'''
        high_prize_probability_up_list = []
        for high_item in high_prize_probability_list:
            item_level = high_item[0]
            item_probability = high_item[1]
            if item_level == 'SSR':
                item_probability = item_probability * ssr_up
            high_prize_probability_up_list.append((item_level, item_probability))
        level = weighted_random(high_prize_probability_up_list)
        '''确定名称'''
        name = weighted_random(high_prize_type_dict[level])
        '''存入数组'''
        item_dict = {}
        item_dict['level'] = level
        item_dict['name'] = name
        item_list.append(item_dict)
    return item_list

def try_times_by_low(total_times):
    """连续抽：低级"""
    item_list = []
    for time_no in range(0, total_times):
        '''确定级别'''
        level = weighted_random(low_prize_probability_list)
        '''确定名称'''
        name = weighted_random(low_prize_type_dict[level])
        '''存入数组'''
        item_dict = {}
        item_dict['level'] = level
        item_dict['name'] = name
        item_list.append(item_dict)
    return item_list

def sum_dict_value(item_dict):
    """统计字典数值"""
    total_size = 0
    for item in item_dict:
        total_size = total_size + item_dict[item]
    return total_size

if __name__ == '__main__':
    test_size = 1000
    