def draw_flow_chart(match_by_file, lines, reliance):
    # 确保一一对应的指令位置正确
    reliance[3] = 2     # stage 1
    reliance[5] = 4
    reliance[7] = 6
    reliance[9] = 8
    reliance[11] = 10
    reliance[13] = 12
    reliance[19] = 18
    reliance[21] = 20
    reliance[24] = 23

    reliance[26] = 25
    reliance[28] = 27
    reliance[30] = 29
    reliance[35] = 34
    reliance[38] = 37       # stage 2
    reliance[42] = 41
    reliance[45] = 44
    reliance[48] = 47
    reliance[50] = 49
    reliance[52] = 51
    reliance[54] = 53
    reliance[56] = 55

    reliance[61] = 60       # stage 3
    reliance[68] = 67

    flow_chart_output = open("./result/flow_chart_output.txt", 'w')
    node_output = '    % adding nodes\n'
    frame_output = '    % adding frame\n'
    arrow_output = '    % adding arrows\n'
    lower_appearance_list = []
    lower_start_list = []
    higher_appearance_list = []
    last_count = 60
    total_count = 0
    last_type = {0: 1}
    for stage_iter in range(len(match_by_file)):
        match_by_stage = match_by_file[stage_iter + 1]
        for line_iter in range(len(match_by_stage)):
            total_count += 1
            line_count = match_by_stage[line_iter + 1]
            certain_line = lines[stage_iter + 1][line_iter + 1]
            if '检查单' in certain_line[1]:
                higher_appearance_list.append((certain_line, line_count))
                last_type[total_count] = 1
            elif reliance[total_count] != -1 and last_type[reliance[total_count]] == -1:
                lower_appearance_list[len(lower_appearance_list) - 1].append((certain_line, line_count))
                last_type[total_count] = -1
            elif reliance[total_count] != -1 and last_type[reliance[total_count]] == 1:
                higher_appearance_list.append((certain_line, line_count))
                last_type[total_count] = 1
            else:
                if line_count > 30:
                    higher_appearance_list.append((certain_line, line_count))
                    last_type[total_count] = 1
                else:
                    if last_type[total_count - 1] == 1:
                        lower_appearance = [(certain_line, line_count)]
                        lower_appearance_list.append(lower_appearance)
                        lower_start_list.append(len(higher_appearance_list))
                    else:
                        lower_appearance_list[len(lower_appearance_list) - 1].append((certain_line, line_count))
                    last_type[total_count] = -1

            last_count = line_count

    # 生成 node\arrow 部分
    node_output += '    \\node (start) [startstop] {Start};\n'
    last_node = 'start'
    process_count = 0
    for list_iter in range(len(higher_appearance_list)):
        process_count += 1
        if len(higher_appearance_list[list_iter]) == 2:
            actual_line = higher_appearance_list[list_iter][0][1]
        else:
            actual_line = higher_appearance_list[list_iter][0][1] + '\ 或\ ' + higher_appearance_list[list_iter][0][2]
        node_output += '    \\node (pro{}) [process{}, below of={}] {{{}}};\n'.format(
            process_count, higher_appearance_list[list_iter][0][0], last_node, actual_line.replace('_', '\_') + '：' + str(higher_appearance_list[list_iter][1]) + '次')
        arrow_output += '    \\draw [arrow] ({}) -- (pro{});\n'.format(last_node, process_count)
        last_node = 'pro{}'.format(process_count)
    arrow_output += '    \\draw [arrow] ({}) -- ({});\n'.format(last_node, 'stop')
    arrow_output += '\n'
    node_output += '    \\node (stop) [startstop, below of={}] {{Stop}};\n'.format(last_node)
    node_output += '\n'

    x_shift = []        # (start, end, out)
    for double_list_iter in range(len(lower_appearance_list)):
        lower_appearance = lower_appearance_list[double_list_iter]
        if lower_start_list[double_list_iter] == 0:
            last_node = 'start'
        else:
            last_node = 'pro{}'.format(lower_start_list[double_list_iter])
        left_side = 0
        right_side = 0
        for shift_iter in range(len(x_shift)):
            start = x_shift[shift_iter][0]
            end = x_shift[shift_iter][1]
            out = x_shift[shift_iter][2]
            if end < lower_start_list[double_list_iter] or start > lower_start_list[double_list_iter] + len(lower_appearance):
                continue
            else:
                if out < 0:
                    left_side = min(left_side, out)
                else:
                    right_side = max(right_side, out)
        if abs(left_side) < abs(right_side):
            final_shift = left_side - 1
        elif abs(left_side) > abs(right_side):
            final_shift = right_side + 1
        else:
            if abs(left_side) == 0:
                final_shift = -1
            else:
                final_shift = left_side - 1
        x_shift.append((lower_start_list[double_list_iter], lower_start_list[double_list_iter] + len(lower_appearance), final_shift))
        for list_iter in range(len(lower_appearance)):
            process_count += 1
            if len(lower_appearance[list_iter][0]) == 2:
                actual_line = lower_appearance[list_iter][0][1]
            else:
                actual_line = lower_appearance[list_iter][0][1] + '\ 或\ ' + lower_appearance[list_iter][0][2]
            if list_iter == 0:
                if final_shift < 0:
                    node_output += '    \\node (pro{}) [processOptional{}, left of={}, xshift={}cm] {{{}}};\n'.format(
                        process_count, lower_appearance[list_iter][0][0], last_node, final_shift * 4, actual_line.replace('_', '\_') + '：' + str(lower_appearance[list_iter][1]) + '次')
                else:
                    node_output += '    \\node (pro{}) [processOptional{}, right of={}, xshift={}cm] {{{}}};\n'.format(
                        process_count, lower_appearance[list_iter][0][0], last_node, final_shift * 4, actual_line.replace('_', '\_') + '：' + str(lower_appearance[list_iter][1]) + '次')
                arrow_output += '    \\draw [arrow,dashed] ({}) -- (pro{});\n'.format(last_node, process_count)
            else:
                node_output += '    \\node (pro{}) [processOptional{}, below of={}] {{{}}};\n'.format(
                    process_count, lower_appearance[list_iter][0][0], last_node, actual_line.replace('_', '\_') + '：' + str(lower_appearance[list_iter][1]) + '次')
                arrow_output += '    \\draw [arrow,dashed] ({}) -- (pro{});\n'.format(last_node, process_count)
            last_node = 'pro{}'.format(process_count)
        if lower_start_list[double_list_iter] + 1 > len(higher_appearance_list):
            arrow_output += '    \\draw [arrow,dashed] ({}) -- ({});\n'.format(last_node, 'stop')
        else:
            arrow_output += '    \\draw [arrow,dashed] ({}) -- (pro{});\n'.format(last_node, lower_start_list[double_list_iter] + 1)
        node_output += '\n'
        arrow_output += '\n'

    # 生成 frame 部分

    final_chart_output = node_output + arrow_output
    print(final_chart_output, file=flow_chart_output)


