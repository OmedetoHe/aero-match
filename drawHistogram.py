# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
plt.rcParams['font.sans-serif'] = ['SimHei', 'KaiTi', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 6  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
plt.rcParams['figure.figsize'] = (9.0, 6.0) # 设置figure_size尺寸

def draw_histogram(match_by_file):
    order_list = []
    frequency_list = []

    for stage_iter in match_by_file.keys():
        match_by_stage = match_by_file[stage_iter]
        for line_iter in match_by_stage.keys():
            order_list.append(line_iter)
            frequency_list.append(match_by_stage[line_iter])
            # print(match_by_stage[line_iter], ' ', line_iter)

    order_number_list = range(len(order_list))
    # print(len(order_list))
    # print(len(order_number_list))
    # for i in order_number_list:
    #     print(i)
    plt.bar(order_number_list, frequency_list, color="#FF0000")
    # plt.hist(frequency_list, order_number_list, histtype='bar', density=0.2)
    plt.xticks(order_number_list, order_list, rotation=90)  ## 可以设置坐标字

    # plt.legend()

    plt.xlabel('指令内容')
    plt.ylabel('标记频次')

    plt.title(u'标记统计直方图')
    plt.savefig("cm.png", dpi=600)
    # plt.show()
