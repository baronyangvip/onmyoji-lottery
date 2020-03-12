# coding=utf-8
'''
Created on 2018年9月4日

@author: baron
'''
from lottery_utils import *

def run_lottery_by_low(total_num, one_size):
    """抽奖测试"""
    print '='*20
    is_stop = False
    total_size = 0
    name_dict = {}
    while not is_stop:
        item_list = try_times_by_low(one_size)
        total_size = total_size + one_size
        out_line = str(total_size) + '\t' + \
                    str(item_list).decode('string_escape')
        print out_line
        for item in item_list:
            if item['name'].endswith('呱'):
                item['level'] = 'SSN'
            if item['level'] not in name_dict:
                name_dict[item['level']] = {item['name']:1}
            else:
                if item['name'] not in name_dict[item['level']]:
                    name_dict[item['level']][item['name']] = 1
                else:
                    name_dict[item['level']][item['name']] = name_dict[item['level']][item['name']] + 1                
        if total_size >= total_num:
            is_stop = True
    print '-'*20
    for name in name_dict:
        print name + '数量：' + str(sum_dict_value(name_dict[name]))
        sorted_item_list = sorted(name_dict[name].items(), key=lambda d: d[1], reverse=True) 
        print str(sorted_item_list).decode('string_escape') 
    print '='*20
    
if __name__ == '__main__':
    total_num = 100
    one_size = 10
    run_lottery_by_low(total_num, one_size)
    
    