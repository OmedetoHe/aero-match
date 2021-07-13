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
    for i in range(24):
        lines_statistic[i + 1] = []
        file_short_of[i + 1] = []
    lines_statistics[1] = lines_statistic
    files_short_of[1] = file_short_of

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
    for i in range(32):
        lines_statistic[i + 1] = []
        file_short_of[i + 1] = []
    lines_statistics[2] = lines_statistic
    files_short_of[2] = file_short_of

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
    for i in range(14):
        lines_statistic[i + 1] = []
        file_short_of[i + 1] = []
    lines_statistics[3] = lines_statistic
    files_short_of[3] = file_short_of

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
    for i in range(5):
        lines_statistic[i + 1] = []
        file_short_of[i + 1] = []
    lines_statistics[4] = lines_statistic
    files_short_of[4] = file_short_of


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

def compare_line(expect_string, actual_string):
    if '_' in expect_string:
        return underline_compare(expect_string, actual_string)
    else:
        return expect_string == actual_string

def underline_compare(expect_string, actual_string):
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
                print('file {} split {} id {} text {}'.format(output_tuple[0], output_tuple[1], output_tuple[2], output_tuple[3][1]), file=match_file)

    total_not_match = 0
    not_match_file = open('./result/not_match.txt', 'w')
    for loop_stage in range(len(files_short_of)):
        stage_lines = files_short_of[loop_stage + 1]
        for loop_line in range(len(stage_lines)):
            match_line = stage_lines[loop_line + 1]
            match_count = len(match_line)
            total_not_match += match_count
            print('stage {} line {} has {} not match.'.format((loop_stage + 1), (loop_line + 1), match_count), file=not_match_file)
            for output_line in range(match_count):
                output_tuple = match_line[output_line]
                print('file {} split {} id {} text {}'.format(output_tuple[0], output_tuple[1], output_tuple[2], output_tuple[3][1]), file=not_match_file)

    print('====================   finished, match {}, not match {}   ===================='.format(total_match, total_not_match))