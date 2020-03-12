#coding=utf-8

'''
Created on 2018年7月16日

@author: yangbl
'''

from common_conf import *

"""工作路径"""
KB_PATH = LOCAL_PATH + '/kb'

"""概率配置"""
high_prize_probability_list = []
for line in open(KB_PATH + '/' + 'high_level_dict.txt'):
    line = line.strip()
    line_array = line.split('\t')
    if len(line_array) == 2:
        line_type = line_array[0]
        line_percent = line_array[1]
        high_prize_probability_list.append((line_type, float(line_percent)))

low_prize_probability_list = []
for line in open(KB_PATH + '/' + 'low_level_dict.txt'):
    line = line.strip()
    line_array = line.split('\t')
    if len(line_array) == 2:
        line_type = line_array[0]
        line_percent = line_array[1]
        low_prize_probability_list.append((line_type, float(line_percent)))

"""副本SR"""
low_SR_list = [
                '日和坊',
                '鬼使黑',
                '骨女',
                '海坊主',
                '小松丸',
                '二口女',
                '跳跳哥哥',
                '桃花妖',
                '镰鼬'
    ]

low_R_list = [
                '椒图',
                '饿鬼',
                '铁鼠'
    ]

"""奖品配置"""
high_prize_type_dict = {}
low_prize_type_dict = {}
for line in open(KB_PATH + '/' + 'name_dict.txt'):
    line = line.strip()
    line_array = line.split('\t')
    if len(line_array) == 3:
        name = line_array[0]
        level = line_array[1]
        status = line_array[2]
        '''高级'''
        if level in ['R', 'SR', 'SSR'] and status == 'y':
            if level not in high_prize_type_dict:
                if name in low_SR_list:
                    high_prize_type_dict[level] = [(name,2)]
                elif name in low_R_list:
                    high_prize_type_dict[level] = [(name,2)]
                else:
                    high_prize_type_dict[level] = [(name,10)]
            else:
                if name in low_SR_list:
                    high_prize_type_dict[level].append((name,2))
                elif name in low_R_list:
                    high_prize_type_dict[level].append((name,2))
                else:
                    high_prize_type_dict[level].append((name,10))
        '''低级'''
        if level in ['N', 'R'] and status == 'y':
            if level not in low_prize_type_dict:
                if name.endswith('呱'):
                    low_prize_type_dict[level] = [(name,6)]
                elif name in low_R_list:
                    low_prize_type_dict[level] = [(name,200)]
                else:
                    low_prize_type_dict[level] = [(name,1000)]
            else:
                if name.endswith('呱'):
                    low_prize_type_dict[level].append((name,6))
                elif name in low_R_list:
                    low_prize_type_dict[level].append((name,200))
                else:
                    low_prize_type_dict[level].append((name,1000))
