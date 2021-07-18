import json
import os
import csv
import codecs
# from compare import reset_count_process
# from compare import compare_and_count_with_strategy
from compare import init_lines
from compare import non_identity_compare
from compare import match_by_file
# from compare import output_result
# from compare import underline_compare
from compare import lines
from drawFlowChart import draw_flow_chart


def parse_json(jsonpath):
    with open(jsonpath, 'r', encoding='utf8') as file:
        jsonContents = json.load(file)
        splitInf = {}
        for jsonContent in jsonContents:
            recordName = jsonContent['file_upload']
            PMID = []  # 保存PM的ID，如果不在PMID里就是在PFID里
            PFID = []
            PMRecords = {}
            PFRecords = {}
            for inf in jsonContent['annotations'][0]['result']:
                if inf['type'] == 'labels':
                    if inf['value']['labels'][0] == 'PM':
                        PMID.append(inf['id'])
                        PMRecords[inf['id']] = (inf['value']['start'], inf['value']['end'])
                    elif inf['value']['labels'][0] == 'PF':
                        PFID.append(inf['id'])
                        PFRecords[inf['id']] = (inf['value']['start'], inf['value']['end'])
                elif inf['type'] == 'textarea':
                    if inf['id'] in PMRecords:
                        PMRecords[inf['id']] = [PMRecords[inf['id']], inf['value']['text'][0]]
                    elif inf['id'] in PFRecords:
                        PFRecords[inf['id']] = [PFRecords[inf['id']], inf['value']['text'][0]]
            splitInf[recordName] = (PMRecords, PFRecords, PMID, PFID)
            # print(splitInf)
        return splitInf


if __name__ == "__main__":

    '''
        realFileCount:  真正文件个数
    '''
    realFileCount = 0

    wholeSplitInf = {}

    if os.path.exists('./result/cer.txt'):
        os.remove('./result/cer.txt')
    if os.path.exists('./result/match.txt'):
        os.remove('./result/match.txt')
    if os.path.exists('./result/not_match.txt'):
        os.remove('./result/not_match.txt')
    if os.path.exists('./result/statistics.txt'):
        os.remove('./result/statistics.txt')
    if os.path.exists('./result/statistics.csv'):
        os.remove('./result/statistics.csv')
    statistic_table = open('./result/statistics.csv', 'w')

    # print(underline_compare('a_ab', 'a11bb'))

    print('==================================================')
    for num in range(6):
        filename = 'labels/0' + str(num + 1) + '.json'
        print(filename)
        tempSplitInf = parse_json(filename)
        wholeSplitInf.update(tempSplitInf)

    sortedWholeSplitInf = {}
    # sortedWholeSplitInf[record_name][split_number] = (PMRecords, PFRecords, PMID, PFID)

    for originFileName, infItem in wholeSplitInf.items():
        underlineSplit = originFileName.split('_')
        splitNum = eval(underlineSplit[0])
        realFileName = underlineSplit[1][0:-8]
        # print(originFileName)
        # print(splitNum, ' ', realFileName)

        if realFileName in sortedWholeSplitInf.keys():
            sortedWholeSplitInf[realFileName][splitNum] = infItem
        else:
            realFileSplitDict = {splitNum: infItem}
            sortedWholeSplitInf[realFileName] = realFileSplitDict

    # sort the file names
    wholeRealFileName = list(sortedWholeSplitInf.keys())
    wholeRealFileName.sort()

    # print(len(lines))
    init_lines()
    # print(len(lines))
    total_match_count = 0
    total_not_match_count = 0
    total_count = 0

    headers = ['文件名']
    for stage_iter in range(len(lines)):
        line_by_stage = lines[stage_iter + 1]
        for line_iter in range(len(line_by_stage)):
            if len(line_by_stage[line_iter + 1]) == 2:
                headers.append(line_by_stage[line_iter + 1][1])
            else:
                headers.append(line_by_stage[line_iter + 1][1] + ' 或 ' + line_by_stage[line_iter + 1][2])
    # statistic_table.write(codecs.BOM_UTF8)  # 解决乱码问题
    csv_writer = csv.writer(statistic_table, dialect='excel')
    csv_writer.writerow(headers)

    for realFileName in wholeRealFileName:

        PMRecordsList = []
        PFRecordsList = []
        PMIDList = []
        PFIDList = []

        realFileCount += 1
        # reset_count_process(realFileCount)

        realFileSplitDict = sortedWholeSplitInf[realFileName]
        # print(realFileName)
        # sort the split numbers
        sortedSplitNumList = list(realFileSplitDict.keys())
        sortedSplitNumList.sort()
        for splitNum in sortedSplitNumList:
            infItemTuple = sortedWholeSplitInf[realFileName][splitNum]      # get the (PMRecords, PFRecords, PMID, PFID) tuple
            # print(splitNum)
            splitPMRecords = infItemTuple[0]
            splitPFRecords = infItemTuple[1]
            splitPMID = infItemTuple[2]
            splitPFID = infItemTuple[3]
            total_count += len(splitPFID)
            total_count += len(splitPMID)
            # print(splitPMID)

            # start to store compare item
            # compare_and_count(realFileName, splitPMRecords, splitPFRecords, splitPMID, splitPFID)
            PMRecordsList.append(splitPMRecords)
            PFRecordsList.append(splitPFRecords)
            PMIDList.append(splitPMID)
            PFIDList.append(splitPFID)

        # start to compare
        # print(PMIDList)
        # compare_and_count_with_strategy(realFileName, sortedSplitNumList, PMRecordsList, PFRecordsList, PMIDList, PFIDList)
        match_count, not_match_count = non_identity_compare(realFileName, sortedSplitNumList, PMRecordsList, PFRecordsList, PMIDList, PFIDList, csv_writer)
        total_match_count += match_count
        total_not_match_count += not_match_count

    # output_result()
    # print('_aa'.split('_'))
    csv_line = ['total_count']
    statistic_file = open('./result/statistics.txt', 'a')
    print('', file=statistic_file)
    print('total count', file=statistic_file)
    for stage_iter in range(len(match_by_file)):
        match_by_stage = match_by_file[stage_iter + 1]
        for line_iter in range(len(match_by_file[stage_iter + 1])):
            print('stage {} line {} has {} match, expect {}.'.format(stage_iter + 1, line_iter + 1, match_by_stage[line_iter + 1],
                                                                    lines[stage_iter + 1][line_iter + 1]), file=statistic_file)
            csv_line.append(match_by_stage[line_iter + 1])
    csv_writer.writerow(csv_line)
    print('====================   finished, match {}, not match {}   ===================='.format(total_match_count, total_not_match_count))
    draw_flow_chart(match_by_file, lines)
    # print(total_count, ' ', len(wholeRealFileName))
