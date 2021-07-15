current_stage = 1
# current_stage 代表当前到达的阶段，1代表下降，2代表进近，3代表着陆，4代表着陆滑跑
current_line_number = 1
# current_line_number 同理代表当前阶段预期获得的喊话序号
lines = {}
# line 存储全部喊话内容
expect_next_line = ('PF', '下降检查单')
# expect_next_line 预期的下一个喊话

files_short_of = {}
# files_short_of 文件缺少的喊话
lines_statistics = {}
match_by_file = {}

def init_lines():
    print('====================   lines initialization   ====================')

    # stage 1
    stage_lines = {}
    stage_lines[1] = ('PF', '下降检查单')
    stage_lines[2] = ('PF', '增压')
    stage_lines[3] = ('PM', '着陆高度_')
    stage_lines[4] = ('PF', '再现')
    stage_lines[5] = ('PM', '检查')
    stage_lines[6] = ('PF', '自动刹车')
    stage_lines[7] = ('PM', '_')
    stage_lines[8] = ('PF', '着陆数据')
    stage_lines[9] = ('PM', 'VREF_Minimums_')
    stage_lines[10] = ('PF', '进近简令')
    stage_lines[11] = ('PM', '完成')
    stage_lines[12] = ('PF', '最大着陆重量')
    stage_lines[13] = ('PM', '核实')
    stage_lines[14] = ('PM', '下降检查单完成')

    stage_lines[15] = ('PM', '过渡高度层')
    stage_lines[16] = ('PF', '高度表_')        # 高度表拨正值 ？
    stage_lines[17] = ('PF', '进近检查单')
    stage_lines[18] = ('PF', '高度表')
    stage_lines[19] = ('PM', '_')
    stage_lines[20] = ('PF', '航道导航频率调定')
    stage_lines[21] = ('PM', '核实')
    stage_lines[22] = ('PM', '进近检查单完成')

    stage_lines[23] = ('PF', '开灯')
    stage_lines[24] = ('PM', '10000')

    lines[1] = stage_lines

    lines_statistic = {}
    file_short_of = {}
    match_by_stage = {}
    for i in range(24):
        lines_statistic[i + 1] = []
        file_short_of[i + 1] = []
        match_by_stage[i + 1] = 0
    lines_statistics[1] = lines_statistic
    files_short_of[1] = file_short_of
    match_by_file[1] = match_by_stage

    # stage 2
    stage_lines = {}
    stage_lines[1] = ('PF', '襟翼_')
    stage_lines[2] = ('PM', '襟翼_')
    stage_lines[3] = ('PF', '襟翼_速度')
    stage_lines[4] = ('PM', '襟翼_到位')

    stage_lines[5] = ('PF', '自动驾驶_航道_ILS识别码_')
    stage_lines[6] = ('PM', '证实')
    stage_lines[7] = ('PF', 'APP预位', 'VOR/LOC预位')

    stage_lines[8] = ('PM', '航道截获')
    stage_lines[9] = ('PF', '进近航向_APP预位')
    stage_lines[10] = ('PM', '证实')

    stage_lines[11] = ('PM', '下滑道移动')
    stage_lines[12] = ('PF', '放轮襟翼15')
    stage_lines[13] = ('PM', '放轮襟翼15')
    stage_lines[14] = ('PF', '襟翼15速度')

    stage_lines[15] = ('PM', '下滑道截获')
    stage_lines[16] = ('PF', '襟翼30/40')
    stage_lines[17] = ('PM', '襟翼30/40')
    stage_lines[18] = ('PF', '进近速度_')

    stage_lines[19] = ('PF', '复飞高度_')
    stage_lines[20] = ('PM', '证实')
    stage_lines[21] = ('PF', '着陆检查单')
    stage_lines[22] = ('PF', '发动机启动电门')
    stage_lines[23] = ('PM', '连续')
    stage_lines[24] = ('PF', '减速板')
    stage_lines[25] = ('PM', '预位')
    stage_lines[26] = ('PF', '起落架')
    stage_lines[27] = ('PM', '放下')
    stage_lines[28] = ('PF', '襟翼')
    stage_lines[29] = ('PM', '_绿灯')
    stage_lines[30] = ('PF', 'APU引气按需设置')
    stage_lines[31] = ('PM', '核实')
    stage_lines[32] = ('PM', '着陆检查单完成')

    lines[2] = stage_lines

    lines_statistic = {}
    file_short_of = {}
    match_by_stage = {}
    for i in range(32):
        lines_statistic[i + 1] = []
        file_short_of[i + 1] = []
        match_by_stage[i + 1] = 0
    lines_statistics[2] = lines_statistic
    files_short_of[2] = file_short_of
    match_by_file[2] = match_by_stage

    # stage 3
    stage_lines = {}
    stage_lines[1] = ('PM', 'OM/FAP高度_')
    stage_lines[2] = ('PF', '检查')

    stage_lines[3] = ('PM', '1000稳定', '1000不稳定')
    stage_lines[4] = ('PF', '检查开灯', '复飞')

    stage_lines[5] = ('PM', '500稳定', '500不稳定')
    stage_lines[6] = ('PF', '检查')
    stage_lines[7] = ('PM', '拉平预位')     # 双通道 ？

    stage_lines[8] = ('PM', '差100')
    stage_lines[9] = ('PF', '继续')

    stage_lines[10] = ('PM', '300稳定', '300不稳定')
    stage_lines[11] = ('PF', '检查', '复飞')

    stage_lines[12] = ('PM', '频闪灯')

    stage_lines[13] = ('PM', 'MINIMUMS_')       # 能见的目视参考 ？
    stage_lines[14] = ('PF', '继续/落地')

    lines[3] = stage_lines

    lines_statistic = {}
    file_short_of = {}
    match_by_stage = {}
    for i in range(14):
        lines_statistic[i + 1] = []
        file_short_of[i + 1] = []
        match_by_stage[i + 1] = 0
    lines_statistics[3] = lines_statistic
    files_short_of[3] = file_short_of
    match_by_file[3] = match_by_stage

    # stage 4
    stage_lines = {}
    stage_lines[1] = ('PM', '减速板升起', '无减速板')

    stage_lines[2] = ('PM', '自动刹车工作', '自动刹车解除')

    stage_lines[3] = ('PM', '反推正常', '_发无反推/无反推')

    stage_lines[4] = ('PM', '60')

    stage_lines[5] = ('PM', '自动刹车解除')

    lines[4] = stage_lines

    lines_statistic = {}
    file_short_of = {}
    match_by_stage = {}
    for i in range(5):
        lines_statistic[i + 1] = []
        file_short_of[i + 1] = []
        match_by_stage[i + 1] = 0
    lines_statistics[4] = lines_statistic
    files_short_of[4] = file_short_of
    match_by_file[4] = match_by_stage
    files_short_of[-1] = {}
    files_short_of[-1][-1] = []


def reset_count_process(real_file_count):

    global current_stage
    global current_line_number
    global expect_next_line

    print('====================   file {}, start to reset   ===================='.format(real_file_count))
    current_stage = 1
    current_line_number = 1
    expect_next_line = ('PF', '下降检查单')


def compare_and_count(real_file_name, split_num_list, pm_records_list, pf_records_list, pm_id_list, pf_id_list):

    global current_stage
    global current_line_number
    global expect_next_line

    list_num_pm = 0
    list_num_pf = 0
    num_pm = 0
    num_pf = 0

    while current_stage <= 4:
        need_to_choose = -1
        stage_lines = lines[current_stage]
        # print(current_stage, ' ', current_line_number)
        if len(expect_next_line) == 3 \
                and current_line_number + 1 <= len(stage_lines) \
                and len(stage_lines[current_line_number + 1]) == 3:
            need_to_choose = 0
        if need_to_choose == -1:
            if expect_next_line[0] == 'PF':
                if list_num_pf < len(pf_records_list):
                    current_pf_records = pf_records_list[list_num_pf]
                    current_pf_id = pf_id_list[list_num_pf]
                    if num_pf < len(current_pf_records):
                        if '@' not in current_pf_records[current_pf_id[num_pf]][1]:
                            if len(expect_next_line) == 2:
                                compare_result = compare_line(expect_next_line[1], current_pf_records[current_pf_id[num_pf]][1])

                                if compare_result:
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pf, current_pf_id[num_pf], current_pf_records[current_pf_id[num_pf]]))
                                else:
                                    files_short_of[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pf, current_pf_id[num_pf], current_pf_records[current_pf_id[num_pf]]))
                            else:
                                compare_result1 = compare_line(expect_next_line[1], current_pf_records[current_pf_id[num_pf]][1])
                                compare_result2 = compare_line(expect_next_line[2], current_pf_records[current_pf_id[num_pf]][1])

                                if compare_result1 or compare_result2:
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pf, current_pf_id[num_pf],
                                         current_pf_records[current_pf_id[num_pf]]))
                                else:
                                    files_short_of[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pf, current_pf_id[num_pf],
                                         current_pf_records[current_pf_id[num_pf]]))
                        num_pf += 1
                        if num_pf >= len(current_pf_records):
                            list_num_pf += 1
                            num_pf = 0
            else:
                if list_num_pm < len(pm_records_list):
                    current_pm_records = pm_records_list[list_num_pm]
                    current_pm_id = pm_id_list[list_num_pm]
                    if num_pm < len(current_pm_records):
                        if '@' not in current_pm_records[current_pm_id[num_pm]][1]:
                            if len(expect_next_line) == 2:
                                compare_result = compare_line(expect_next_line[1],
                                                                       current_pm_records[current_pm_id[num_pm]][1])

                                if compare_result:
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pm, current_pm_id[num_pm],
                                         current_pm_records[current_pm_id[num_pm]]))
                                else:
                                    files_short_of[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pm, current_pm_id[num_pm],
                                         current_pm_records[current_pm_id[num_pm]]))
                            else:
                                compare_result1 = compare_line(expect_next_line[1],
                                                                        current_pm_records[current_pm_id[num_pm]][1])
                                compare_result2 = compare_line(expect_next_line[2],
                                                                        current_pm_records[current_pm_id[num_pm]][1])

                                if compare_result1 or compare_result2:
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pm, current_pm_id[num_pm],
                                         current_pm_records[current_pm_id[num_pm]]))
                                else:
                                    files_short_of[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pm, current_pm_id[num_pm],
                                         current_pm_records[current_pm_id[num_pm]]))
                        num_pm += 1
                        if num_pm >= len(current_pm_records):
                            list_num_pm += 1
                            num_pm = 0
            current_line_number += 1
            if current_line_number > len(stage_lines):
                current_stage += 1
                current_line_number = 1
            if current_stage <= 4:
                expect_next_line = lines[current_stage][current_line_number]
                # print(type(expect_next_line))
        else:
            # print(type(expect_next_line))
            if expect_next_line[0] == 'PF':
                if list_num_pf < len(pf_records_list):
                    current_pf_records = pf_records_list[list_num_pf]
                    current_pf_id = pf_id_list[list_num_pf]
                    if num_pf < len(current_pf_records):
                        if '@' not in current_pf_records[current_pf_id[num_pf]][1]:
                            compare_result1 = compare_line(expect_next_line[1], current_pf_records[current_pf_id[num_pf]][1])
                            compare_result2 = compare_line(expect_next_line[2], current_pf_records[current_pf_id[num_pf]][1])

                            if compare_result1 or compare_result2:
                                lines_statistics[current_stage][current_line_number].append(
                                    (real_file_name, list_num_pf, current_pf_id[num_pf],
                                     current_pf_records[current_pf_id[num_pf]]))
                            else:
                                files_short_of[current_stage][current_line_number].append(
                                    (real_file_name, list_num_pf, current_pf_id[num_pf],
                                     current_pf_records[current_pf_id[num_pf]]))
                            if compare_result1:
                                need_to_choose = 1
                            if compare_result2:
                                need_to_choose = 2
                        num_pf += 1
                        if num_pf >= len(current_pf_records):
                            list_num_pf += 1
                            num_pf = 0
            else:
                if list_num_pm < len(pm_records_list):
                    current_pm_records = pm_records_list[list_num_pm]
                    current_pm_id = pm_id_list[list_num_pm]
                    if num_pm < len(current_pm_records):
                        if '@' not in current_pm_records[current_pm_id[num_pm]][1]:
                            compare_result1 = compare_line(expect_next_line[1],
                                                                    current_pm_records[current_pm_id[num_pm]][1])
                            compare_result2 = compare_line(expect_next_line[2],
                                                                    current_pm_records[current_pm_id[num_pm]][1])

                            if compare_result1 or compare_result2:
                                lines_statistics[current_stage][current_line_number].append(
                                    (real_file_name, list_num_pm, current_pm_id[num_pm],
                                     current_pm_records[current_pm_id[num_pm]]))
                            else:
                                files_short_of[current_stage][current_line_number].append(
                                    (real_file_name, list_num_pm, current_pm_id[num_pm],
                                     current_pm_records[current_pm_id[num_pm]]))
                            if compare_result1:
                                need_to_choose = 1
                            if compare_result2:
                                need_to_choose = 2
                        num_pm += 1
                        if num_pm >= len(current_pm_records):
                            list_num_pm += 1
                            num_pm = 0
            current_line_number += 1
            if current_line_number > len(stage_lines):
                current_stage += 1
                current_line_number = 1
            if current_stage <= 4:
                if need_to_choose == 2:
                    expect_next_line = (lines[current_stage][current_line_number][0],
                                        lines[current_stage][current_line_number][2])
                else:
                    expect_next_line = (lines[current_stage][current_line_number][0],
                                        lines[current_stage][current_line_number][1])


def compare_and_count_with_strategy(real_file_name, split_num_list, pm_records_list, pf_records_list, pm_id_list, pf_id_list):

    global current_stage
    global current_line_number
    global expect_next_line

    list_num_pm = 0
    list_num_pf = 0
    num_pm = 0
    num_pf = 0

    while current_stage <= 4:
        need_to_choose = -1
        stage_lines = lines[current_stage]
        # print(current_stage, ' ', current_line_number)
        if len(expect_next_line) == 3 \
                and current_line_number + 1 <= len(stage_lines) \
                and len(stage_lines[current_line_number + 1]) == 3:
            need_to_choose = 0
        if need_to_choose == -1:
            if expect_next_line[0] == 'PF':
                if list_num_pf < len(pf_records_list):
                    current_pf_records = pf_records_list[list_num_pf]
                    current_pf_id = pf_id_list[list_num_pf]
                    if num_pf < len(current_pf_records):
                        if '@' not in current_pf_records[current_pf_id[num_pf]][1]:
                            if len(expect_next_line) == 2:
                                compare_result = compare_line(expect_next_line[1], current_pf_records[current_pf_id[num_pf]][1])

                                if compare_result:
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF', current_pf_records[current_pf_id[num_pf]]))
                                else:
                                    ahead_match_result, ahead_stage, ahead_line_number, ahead_need_to_choose = \
                                        ahead_match(current_stage, current_line_number + 1, 'PF', current_pf_records[current_pf_id[num_pf]][1])
                                    if ahead_match_result:
                                        current_stage = ahead_stage
                                        current_line_number = ahead_line_number
                                        need_to_choose = ahead_need_to_choose
                                        lines_statistics[current_stage][current_line_number].append(
                                            (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF',
                                             current_pf_records[current_pf_id[num_pf]]))
                                    else:
                                        files_short_of[current_stage][current_line_number].append(
                                            (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF', current_pf_records[current_pf_id[num_pf]]))
                            else:
                                compare_result1 = compare_line(expect_next_line[1], current_pf_records[current_pf_id[num_pf]][1])
                                compare_result2 = compare_line(expect_next_line[2], current_pf_records[current_pf_id[num_pf]][1])

                                if compare_result1 or compare_result2:
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF',
                                         current_pf_records[current_pf_id[num_pf]]))
                                else:
                                    ahead_match_result, ahead_stage, ahead_line_number, ahead_need_to_choose = \
                                        ahead_match(current_stage, current_line_number + 1, 'PF',
                                                    current_pf_records[current_pf_id[num_pf]][1])
                                    if ahead_match_result:
                                        current_stage = ahead_stage
                                        current_line_number = ahead_line_number
                                        need_to_choose = ahead_need_to_choose
                                        lines_statistics[current_stage][current_line_number].append(
                                            (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF',
                                             current_pf_records[current_pf_id[num_pf]]))
                                    else:
                                        files_short_of[current_stage][current_line_number].append(
                                            (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF',
                                             current_pf_records[current_pf_id[num_pf]]))
                        num_pf += 1
                        if num_pf >= len(current_pf_records):
                            list_num_pf += 1
                            num_pf = 0
            else:
                if list_num_pm < len(pm_records_list):
                    current_pm_records = pm_records_list[list_num_pm]
                    current_pm_id = pm_id_list[list_num_pm]
                    if num_pm < len(current_pm_records):
                        if '@' not in current_pm_records[current_pm_id[num_pm]][1]:
                            if len(expect_next_line) == 2:
                                compare_result = compare_line(expect_next_line[1],
                                                                       current_pm_records[current_pm_id[num_pm]][1])

                                if compare_result:
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                         current_pm_records[current_pm_id[num_pm]]))
                                else:
                                    ahead_match_result, ahead_stage, ahead_line_number, ahead_need_to_choose = \
                                        ahead_match(current_stage, current_line_number + 1, 'PM',
                                                    current_pm_records[current_pm_id[num_pm]][1])
                                    if ahead_match_result:
                                        current_stage = ahead_stage
                                        current_line_number = ahead_line_number
                                        need_to_choose = ahead_need_to_choose
                                        lines_statistics[current_stage][current_line_number].append(
                                            (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                             current_pm_records[current_pm_id[num_pm]]))
                                    else:
                                        files_short_of[current_stage][current_line_number].append(
                                            (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                             current_pm_records[current_pm_id[num_pm]]))
                            else:
                                compare_result1 = compare_line(expect_next_line[1],
                                                                        current_pm_records[current_pm_id[num_pm]][1])
                                compare_result2 = compare_line(expect_next_line[2],
                                                                        current_pm_records[current_pm_id[num_pm]][1])

                                if compare_result1 or compare_result2:
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                         current_pm_records[current_pm_id[num_pm]]))
                                else:
                                    ahead_match_result, ahead_stage, ahead_line_number, ahead_need_to_choose = \
                                        ahead_match(current_stage, current_line_number + 1, 'PM',
                                                    current_pm_records[current_pm_id[num_pm]][1])
                                    if ahead_match_result:
                                        current_stage = ahead_stage
                                        current_line_number = ahead_line_number
                                        need_to_choose = ahead_need_to_choose
                                        lines_statistics[current_stage][current_line_number].append(
                                            (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                             current_pm_records[current_pm_id[num_pm]]))
                                    else:
                                        files_short_of[current_stage][current_line_number].append(
                                            (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                             current_pm_records[current_pm_id[num_pm]]))
                        num_pm += 1
                        if num_pm >= len(current_pm_records):
                            list_num_pm += 1
                            num_pm = 0
            current_line_number += 1
            if current_line_number > len(lines[current_stage]):
                current_stage += 1
                current_line_number = 1
            '''
            if current_stage <= 4:
                expect_next_line = lines[current_stage][current_line_number]
            '''
        else:
            # print(type(expect_next_line))
            if expect_next_line[0] == 'PF':
                if list_num_pf < len(pf_records_list):
                    current_pf_records = pf_records_list[list_num_pf]
                    current_pf_id = pf_id_list[list_num_pf]
                    if num_pf < len(current_pf_records):
                        if '@' not in current_pf_records[current_pf_id[num_pf]][1]:
                            compare_result1 = compare_line(expect_next_line[1], current_pf_records[current_pf_id[num_pf]][1])
                            compare_result2 = compare_line(expect_next_line[2], current_pf_records[current_pf_id[num_pf]][1])

                            if compare_result1 or compare_result2:
                                lines_statistics[current_stage][current_line_number].append(
                                    (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF',
                                     current_pf_records[current_pf_id[num_pf]]))
                            else:
                                ahead_match_result, ahead_stage, ahead_line_number, ahead_need_to_choose = \
                                    ahead_match(current_stage, current_line_number + 1, 'PF',
                                                current_pf_records[current_pf_id[num_pf]][1])
                                if ahead_match_result:
                                    current_stage = ahead_stage
                                    current_line_number = ahead_line_number
                                    need_to_choose = ahead_need_to_choose
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF',
                                         current_pf_records[current_pf_id[num_pf]]))
                                else:
                                    files_short_of[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF',
                                         current_pf_records[current_pf_id[num_pf]]))
                            if compare_result1:
                                need_to_choose = 1
                            if compare_result2:
                                need_to_choose = 2
                        num_pf += 1
                        if num_pf >= len(current_pf_records):
                            list_num_pf += 1
                            num_pf = 0
            else:
                if list_num_pm < len(pm_records_list):
                    current_pm_records = pm_records_list[list_num_pm]
                    current_pm_id = pm_id_list[list_num_pm]
                    if num_pm < len(current_pm_records):
                        if '@' not in current_pm_records[current_pm_id[num_pm]][1]:
                            compare_result1 = compare_line(expect_next_line[1],
                                                                    current_pm_records[current_pm_id[num_pm]][1])
                            compare_result2 = compare_line(expect_next_line[2],
                                                                    current_pm_records[current_pm_id[num_pm]][1])

                            if compare_result1 or compare_result2:
                                lines_statistics[current_stage][current_line_number].append(
                                    (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                     current_pm_records[current_pm_id[num_pm]]))
                            else:
                                ahead_match_result, ahead_stage, ahead_line_number, ahead_need_to_choose = \
                                    ahead_match(current_stage, current_line_number + 1, 'PM',
                                                current_pm_records[current_pm_id[num_pm]][1])
                                if ahead_match_result:
                                    current_stage = ahead_stage
                                    current_line_number = ahead_line_number
                                    need_to_choose = ahead_need_to_choose
                                    lines_statistics[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                         current_pm_records[current_pm_id[num_pm]]))
                                else:
                                    files_short_of[current_stage][current_line_number].append(
                                        (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                                         current_pm_records[current_pm_id[num_pm]]))
                            if compare_result1:
                                need_to_choose = 1
                            if compare_result2:
                                need_to_choose = 2
                        num_pm += 1
                        if num_pm >= len(current_pm_records):
                            list_num_pm += 1
                            num_pm = 0
            current_line_number += 1
            if current_line_number > len(lines[current_stage]):
                current_stage += 1
                current_line_number = 1
            '''
            if current_stage <= 4:
                if need_to_choose == 2:
                    expect_next_line = (lines[current_stage][current_line_number][0],
                                        lines[current_stage][current_line_number][2])
                else:
                    expect_next_line = (lines[current_stage][current_line_number][0],
                                        lines[current_stage][current_line_number][1])
            '''
        if current_stage <= 4:
            if need_to_choose == 1:
                expect_next_line = (lines[current_stage][current_line_number][0],
                                    lines[current_stage][current_line_number][1])
            elif need_to_choose == 2:
                expect_next_line = (lines[current_stage][current_line_number][0],
                                    lines[current_stage][current_line_number][2])
            else:
                # print(current_line_number, ' ', len(lines[current_stage]), ' ', current_stage)
                expect_next_line = lines[current_stage][current_line_number]
    while list_num_pf < len(pf_records_list):
        current_pf_records = pf_records_list[list_num_pf]
        current_pf_id = pf_id_list[list_num_pf]
        # print(num_pf, ' ', len(current_pf_records), ' ', list_num_pf, ' ', len(pf_records_list))
        if num_pf < len(current_pf_records):
            files_short_of[-1][-1].append(
                (real_file_name, list_num_pf, current_pf_id[num_pf], 'PF',
                 current_pf_records[current_pf_id[num_pf]]))
        num_pf += 1
        if num_pf >= len(current_pf_records):
            list_num_pf += 1
            num_pf = 0
    while list_num_pm < len(pm_records_list):
        current_pm_records = pm_records_list[list_num_pm]
        current_pm_id = pm_id_list[list_num_pm]
        if num_pm < len(current_pm_records):
            files_short_of[-1][-1].append(
                (real_file_name, list_num_pm, current_pm_id[num_pm], 'PM',
                 current_pm_records[current_pm_id[num_pm]]))
        num_pm += 1
        if num_pm >= len(current_pm_records):
            list_num_pm += 1
            num_pm = 0


def ahead_match(start_stage, start_line_number, identity, actual_string):

    ahead_stage = start_stage
    ahead_line_number = start_line_number

    if ahead_line_number > len(lines[ahead_stage]):
        ahead_stage += 1
        ahead_line_number = 1

    while ahead_stage <= 4:
        ahead_stage_lines = lines[ahead_stage]
        ahead_expect_line = ahead_stage_lines[ahead_line_number]
        ahead_need_to_choose = -1
        if len(ahead_expect_line) == 3 \
                and ahead_line_number + 1 <= len(ahead_stage_lines) \
                and len(ahead_stage_lines[ahead_line_number + 1]) == 3:
            ahead_need_to_choose = 0
        if ahead_expect_line[0] == identity:
            if len(ahead_expect_line) == 2:
                compare_result = compare_line(ahead_expect_line[1], actual_string)
                if compare_result:
                    return True, ahead_stage, ahead_line_number, ahead_need_to_choose
                else:
                    ahead_line_number += 1
            else:
                compare_result1 = compare_line(ahead_expect_line[1], actual_string)
                compare_result2 = compare_line(ahead_expect_line[2], actual_string)

                if ahead_need_to_choose == 0:
                    if compare_result1:
                        ahead_need_to_choose = 1
                    if compare_result2:
                        ahead_need_to_choose = 2

                if compare_result1 or compare_result2:
                    return True, ahead_stage, ahead_line_number, ahead_need_to_choose
                else:
                    ahead_line_number += 1
        else:
            ahead_line_number += 1

        if ahead_line_number > len(ahead_stage_lines):
            ahead_stage += 1
            ahead_line_number = 1
    return False, -1, -1, -1


def non_identity_compare(real_file_name, split_num_list, pm_records_list, pf_records_list, pm_id_list, pf_id_list, csv_writer):

    print('====================   file {} comparison start   ===================='.format(real_file_name))
    # 初始化统计列表
    flag_by_file = {}
    for stage_iter in range(len(lines)):
        flag_by_stage = {}
        for line_iter in range(len(lines[stage_iter + 1])):
            flag_by_stage[line_iter + 1] = 0
        flag_by_file[stage_iter + 1] = flag_by_stage
    match_list = []
    not_match_list = []

    # 开始循环比较
    for split_iter in range(len(split_num_list)):
        print('====================   split {} comparison start   ===================='.format(split_num_list[split_iter]))
        pm_records = pm_records_list[split_iter]
        pf_records = pf_records_list[split_iter]
        pm_id = pm_id_list[split_iter]
        pf_id = pf_id_list[split_iter]

        # pf 部分的比较
        for pf_iter in range(len(pf_id)):
            certain_record = pf_records[pf_id[pf_iter]]

            #注意去除@
            if '@' in certain_record[1]:
                continue

            match_stage, match_line = match_by_process(certain_record[1].replace('，', '/').replace(',', '/'), flag_by_file)
            if match_stage == -1:
                not_match_list.append((split_num_list[split_iter], pf_id[pf_iter], 'PF', certain_record))
            else:
                match_list.append((split_num_list[split_iter], pf_id[pf_iter], 'PF', certain_record))
                flag_by_file[match_stage][match_line] += 1
                match_by_file[match_stage][match_line] += 1

        # pm 部分的比较
        for pm_iter in range(len(pm_id)):
            certain_record = pm_records[pm_id[pm_iter]]

            #注意去除@
            if '@' in certain_record[1]:
                continue

            match_stage, match_line = match_by_process(certain_record[1].replace('，', '/').replace(',', '/'), flag_by_file)
            if match_stage == -1:
                not_match_list.append((split_num_list[split_iter], pm_id[pm_iter], 'PM', certain_record))
            else:
                match_list.append((split_num_list[split_iter], pm_id[pm_iter], 'PM', certain_record))
                flag_by_file[match_stage][match_line] += 1
                match_by_file[match_stage][match_line] += 1

    # 输出结果
    match_file = open('./result/match.txt', 'a')
    print('file {} has {} match.'.format(real_file_name, len(match_list)), file=match_file)
    for match_iter in range(len(match_list)):
        output_tuple = match_list[match_iter]
        print('split {} id {} label {} text {}'.format(output_tuple[0], output_tuple[1], output_tuple[2], output_tuple[3][1]), file=match_file)

    not_match_file = open('./result/not_match.txt', 'a')
    print('file {} has {} not match.'.format(real_file_name, len(not_match_list)), file=not_match_file)
    for not_match_iter in range(len(not_match_list)):
        output_tuple = not_match_list[not_match_iter]
        print('split {} id {} label {} text {}'.format(output_tuple[0], output_tuple[1], output_tuple[2], output_tuple[3][1]), file=not_match_file)

    csv_line = [real_file_name]
    statistic_file = open('./result/statistics.txt', 'a')
    print('file {}'.format(real_file_name), file=statistic_file)
    for stage_iter in range(len(lines)):
        flag_by_stage = flag_by_file[stage_iter + 1]
        for line_iter in range(len(lines[stage_iter + 1])):
            print('stage {} line {} has {} match, expect {}.'.format(stage_iter + 1, line_iter + 1, flag_by_stage[line_iter + 1],
                                                                    lines[stage_iter + 1][line_iter + 1]), file=statistic_file)
            csv_line.append(flag_by_stage[line_iter + 1])
    csv_writer.writerow(csv_line)
    return len(match_list), len(not_match_list)


def match_by_process(actual_string, flag):

    for stage_iter in range(len(lines)):
        stage_line = lines[stage_iter + 1]
        for line_iter in range(len(stage_line)):
            if flag[stage_iter + 1][line_iter + 1] == 1:
                continue
            expect_line = stage_line[line_iter + 1]
            if len(expect_line) == 2:
                compare_result = compare_line(expect_line[1], actual_string)
                if compare_result:
                    return stage_iter + 1, line_iter + 1
            else:
                compare_result1 = compare_line(expect_line[1], actual_string)
                compare_result2 = compare_line(expect_line[2], actual_string)
                if compare_result1 or compare_result2:
                    return stage_iter + 1, line_iter + 1
    return -1, -1


def compare_line(expect_string, actual_string):
    cer_file = open('./result/cer.txt', 'a')
    if '_' in expect_string:
        return underline_compare(expect_string, actual_string)
    elif '#' in actual_string:
        translations = actual_string.split('#')
        calculate_cer = cer([x for x in expect_string], [x for x in translations[1]])
        print('{} {} have cer {}'.format(expect_string, translations[1], calculate_cer), file=cer_file)
        # return expect_string == translations[1]
        if calculate_cer <= 0.75:
            return True
        else:
            return False
    else:
        calculate_cer = cer([x for x in expect_string], [x for x in actual_string])
        print('{} {} have cer {}'.format(expect_string, actual_string, calculate_cer), file=cer_file)
        # return expect_string == actual_string
        if calculate_cer <= 0.75:
            return True
        else:
            return False


def underline_compare(expect_string, actual_string):
    """
    expect_length = len(expect_string)
    actual_length = len(actual_string)
    i = 0
    j = 0
    while i < expect_length and j < actual_length:
        if expect_string[i] != '_':
            if expect_string[i] == actual_string[j]:
                i += 1
                j += 1
            else:
                return False
        else:
            i += 1
            while '0' <= actual_string[j] <= '9':
                j += 1
                if j >= actual_length:
                    break
    if i == expect_length and j == actual_length:
        return True
    else:
        return False
    """
    current_expect_pos = 0
    current_actual_pos = 0
    # cer_total = 0
    # cer_count = 0
    while current_expect_pos < len(expect_string):
        if expect_string[current_expect_pos] == '_':
            if current_actual_pos >= len(actual_string) or actual_string[current_actual_pos] < '0' or actual_string[current_actual_pos] > '9':
                return False
            else:
                while current_actual_pos < len(actual_string) \
                        and ('0' <= actual_string[current_actual_pos] <= '9'
                             or actual_string[current_actual_pos] == '.'
                             or actual_string[current_actual_pos] == '/'):
                    current_actual_pos += 1
                current_expect_pos += 1
        else:
            start_expect_pos = current_expect_pos
            end_expect_pos = current_expect_pos
            while end_expect_pos < len(expect_string) and expect_string[end_expect_pos] != '_':
                end_expect_pos += 1

            start_pos = current_actual_pos
            end_pos = current_actual_pos
            while end_pos < len(actual_string) \
                    and (actual_string[end_pos] < '0' or actual_string[end_pos] > '9'):
                end_pos += 1
            cer_temp = cer([x for x in expect_string[start_expect_pos:end_expect_pos]], [x for x in actual_string[start_pos:end_pos]])
            # print('split cer == {}'.format(cer_temp))
            if cer_temp > 0.75:
                return False
            current_expect_pos = end_expect_pos
            current_actual_pos = end_pos
    # print('cer == total {} count {}'.format(cer_total, cer_count))
    return True


def cer(r: list, h: list):
    """
    Calculation of CER with Levenshtein distance.
    """
    # initialisation
    import numpy
    d = numpy.zeros((len(r) + 1) * (len(h) + 1), dtype=numpy.uint16)
    d = d.reshape((len(r) + 1, len(h) + 1))
    for i in range(len(r) + 1):
        for j in range(len(h) + 1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i
    # computation
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                substitution = d[i - 1][j - 1] + 1
                insertion = d[i][j - 1] + 1
                deletion = d[i - 1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)
    return d[len(r)][len(h)] / float(len(r))


def output_result():

    total_match = 0
    match_file = open('./result/match.txt', 'w')
    for loop_stage in range(len(lines_statistics)):
        stage_lines = lines_statistics[loop_stage + 1]
        for loop_line in range(len(stage_lines)):
            match_line = stage_lines[loop_line + 1]
            match_count = len(match_line)
            total_match += match_count
            print('stage {} line {} has {} matches.'.format((loop_stage + 1), (loop_line + 1), match_count), file=match_file)
            for output_line in range(match_count):
                output_tuple = match_line[output_line]
                print('file {} split {} id {} label {} text {}'.format(output_tuple[0], output_tuple[1], output_tuple[2], output_tuple[3], output_tuple[4][1]), file=match_file)

    total_not_match = 0
    not_match_file = open('./result/not_match.txt', 'w')
    for loop_stage in range(4):
        stage_lines = files_short_of[loop_stage + 1]
        for loop_line in range(len(stage_lines)):
            match_line = stage_lines[loop_line + 1]
            match_count = len(match_line)
            total_not_match += match_count
            print('stage {} line {} has {} not match.'.format((loop_stage + 1), (loop_line + 1), match_count), file=not_match_file)
            for output_line in range(match_count):
                output_tuple = match_line[output_line]
                print('file {} split {} id {} label {} text {}'.format(output_tuple[0], output_tuple[1], output_tuple[2], output_tuple[3], output_tuple[4][1]), file=not_match_file)

    left_lines = files_short_of[-1][-1]
    match_count = len(left_lines)
    total_not_match += match_count
    print('stage {} line {} has {} not match.'.format(-1, -1, match_count), file=not_match_file)
    for output_line in range(match_count):
        output_tuple = left_lines[output_line]
        print('file {} split {} id {} label {} text {}'.format(output_tuple[0], output_tuple[1], output_tuple[2], output_tuple[3], output_tuple[4][1]), file=not_match_file)

    print('====================   finished, match {}, not match {}   ===================='.format(total_match, total_not_match))
