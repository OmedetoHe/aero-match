def draw_flow_chart(match_by_file, lines):
    flow_chart_output = open("./result/flow_chart_output.txt", 'w')
    node_output = '    % adding nodes\n'
    frame_output = '    % adding frame\n'
    arrow_output = '    % adding arrows\n'
    lower_appearance_list = []
    lower_start_list = []
    higher_appearance_list = []
    last_count = 60
    for stage_iter in range(len(match_by_file)):
        match_by_stage = match_by_file[stage_iter + 1]
        for line_iter in range(len(match_by_stage)):
            line_count = match_by_stage[line_iter + 1]
            certain_line = lines[stage_iter + 1][line_iter + 1]
            if line_count > 30:
                higher_appearance_list.append(certain_line)
            else:
                if last_count > 30:
                    lower_appearance = [certain_line]
                    lower_appearance_list.append(lower_appearance)
                    lower_start_list.append(len(higher_appearance_list))
                else:
                    lower_appearance_list[len(lower_appearance_list) - 1].append(certain_line)

            last_count = line_count

    # 生成 node\arrow 部分
    node_output += '    \\node (start) [startstop] {Start};\n'
    last_node = 'start'
    process_count = 0
    for list_iter in range(len(higher_appearance_list)):
        process_count += 1
        if len(higher_appearance_list[list_iter]) == 2:
            actual_line = higher_appearance_list[list_iter][1]
        else:
            actual_line = higher_appearance_list[list_iter][1] + '\ 或\ ' + higher_appearance_list[list_iter][2]
        node_output += '    \\node (pro{}) [process, below of={}] {{{}}};\n'.format(process_count, last_node, actual_line.replace('_', '\_'))
        arrow_output += '    \\draw [arrow] ({}) -- (pro{});\n'.format(last_node, process_count)
        last_node = 'pro{}'.format(process_count)
    arrow_output += '    \\draw [arrow] ({}) -- ({});\n'.format(last_node, 'stop')
    arrow_output += '\n'
    node_output += '    \\node (stop) [startstop, below of={}] {{Stop}};\n'.format(last_node)
    node_output += '\n'

    x_shift = 1
    last_pos = 0
    last_shift = 1
    for double_list_iter in range(len(lower_appearance_list)):
        whether_left = False
        lower_appearance = lower_appearance_list[double_list_iter]
        if lower_start_list[double_list_iter] == 0:
            last_node = 'start'
        else:
            last_node = 'pro{}'.format(lower_start_list[double_list_iter])
        if last_pos >= lower_start_list[double_list_iter]:
            x_shift = last_shift + 1
            whether_left = True
        else:
            x_shift = 1
            last_shift = 1
        for list_iter in range(len(lower_appearance)):
            process_count += 1
            if len(lower_appearance[list_iter]) == 2:
                actual_line = lower_appearance[list_iter][1]
            else:
                actual_line = lower_appearance[list_iter][1] + '\ 或\ ' + lower_appearance[list_iter][2]
            if list_iter == 0:
                if whether_left:
                    node_output += '    \\node (pro{}) [process, left of={}, xshift={}cm] {{{}}};\n'.format(
                        process_count, last_node, -2.5, actual_line.replace('_', '\_'))
                else:
                    node_output += '    \\node (pro{}) [process, right of={}, xshift={}cm] {{{}}};\n'.format(process_count, last_node, 2.5, actual_line.replace('_', '\_'))
                arrow_output += '    \\draw [arrow] ({}) -- (pro{});\n'.format(last_node, process_count)
            else:
                node_output += '    \\node (pro{}) [process, below of={}] {{{}}};\n'.format(process_count, last_node, actual_line.replace('_', '\_'))
                arrow_output += '    \\draw [arrow] ({}) -- (pro{});\n'.format(last_node, process_count)
            last_node = 'pro{}'.format(process_count)
        if lower_start_list[double_list_iter] + 1 > len(higher_appearance_list):
            arrow_output += '    \\draw [arrow] ({}) -- ({});\n'.format(last_node, 'stop')
        else:
            arrow_output += '    \\draw [arrow] ({}) -- (pro{});\n'.format(last_node, lower_start_list[double_list_iter] + 1)
        last_shift = x_shift
        last_pos = lower_start_list[double_list_iter] + len(lower_appearance) - 1
        node_output += '\n'
        arrow_output += '\n'

    # 生成 frame 部分

    final_chart_output = node_output + arrow_output
    print(final_chart_output, file=flow_chart_output)


