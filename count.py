import json
from compare import reset_count_process
from compare import compare_and_count
from compare import init_lines
from compare import output_result
# from compare import lines


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

    for realFileName in wholeRealFileName:

        PMRecordsList = []
        PFRecordsList = []
        PMIDList = []
        PFIDList = []

        realFileCount += 1
        reset_count_process(realFileCount)

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
            # print(splitPMID)

            # start to store compare item
            # compare_and_count(realFileName, splitPMRecords, splitPFRecords, splitPMID, splitPFID)
            PMRecordsList.append(splitPMRecords)
            PFRecordsList.append(splitPFRecords)
            PMIDList.append(splitPMID)
            PFIDList.append(splitPFID)

        # start to compare
        # print(PMIDList)
        compare_and_count(realFileName, sortedSplitNumList, PMRecordsList, PFRecordsList, PMIDList, PFIDList)

    output_result()
