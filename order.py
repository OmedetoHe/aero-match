import json


def hasnum(text):
    num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    for word in num:
        if word in text:
            return 1
    return 0


class Text2order:
    def __init__(self, json_path):
        with open(json_path, 'r', encoding='utf-8')as fp:
            self.order_dict = json.load(fp)
            for key in self.order_dict:
                order_dict = self.order_dict[key]
                for k in order_dict:
                    order_dict[k] = 0
        self.order_dict = self.order_dict
        self.last_stage = 0

    def text2order(self, text):
        """

        APU引气按需设置?
        :param text:
        :return: order
        """
        order_dict = self.order_dict['近进阶段']
        land_unique_order = ["连续", "证实", "航道截获", "下滑道移动"]  # 可以唯一确定的指令
        match_list = []
        if "起落架" in text:
            order_dict['起落架'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '起落架'))
            # return True, '近进阶段', '起落架'
        if "放轮" in text:
            order_dict['放轮襟翼15'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '放轮襟翼15'))
            # return True, '近进阶段', '放轮襟翼15'
        if "自动驾驶" in text:
            order_dict['自动驾驶_航道_ILS识别码_'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '自动驾驶_航道_ILS识别码_'))
            # return True, '近进阶段', '自动驾驶_航道_ILS识别码_'
        if "放下" in text and "起落架" not in text:
            order_dict['放下'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '放下'))
            # return True, '近进阶段', '放下'
        if "襟翼" in text and "速度" in text and "15" not in text and "十五" not in text:
            order_dict['襟翼_速度'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '襟翼_速度'))
            # return True, '近进阶段', '襟翼_速度'
        if "襟翼" in text and "速度" in text and ("15" in text or "十五" in text):
            order_dict['襟翼15速度'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '襟翼15速度'))
            # return True, '近进阶段', '襟翼15速度'
        if "到位" in text:
            order_dict['襟翼_到位'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '襟翼_到位'))
            # return True, '近进阶段', '襟翼_到位'
        if "襟翼" in text and "速度" not in text and "到位" not in text and "绿灯" not in text and "30" not in text and "40" not in text and "三十" not in text and "四十" not in text:
            order_dict['襟翼_'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '襟翼_'))
            # return True, '近进阶段', '襟翼_'
        if "襟翼" in text and ("30" in text or "40" in text or "三十" in text or "四十" in text):
            order_dict['襟翼30/40'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '襟翼30/40'))
            # return True, '近进阶段', '襟翼30/40'
        if "下滑道截获" in text:
            order_dict['下滑道截获'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '下滑道截获'))
            # return True, '近进阶段', '下滑道截获'
        if "襟翼" in text and "速度" not in text and "到位" not in text and "绿灯" not in text and "0" not in text and "十" not in text:
            order_dict['襟翼'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '襟翼'))
            # return True, '近进阶段', '襟翼'
        if "预位" in text and "拉平" not in text and "APP" not in text and "LOC" not in text:
            order_dict['预位'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '预位'))
            # return True, '近进阶段', '预位'
        if "着陆检查单完成" in text:
            order_dict['着陆检查单完成'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '着陆检查单完成'))
            # return True, '近进阶段', '着陆检查单完成'
        elif "着陆检查单" in text:
            order_dict['着陆检查单'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '着陆检查单'))
            # return True, '近进阶段', '着陆检查单'
        if ("发动机" in text) and "电门" in text:
            order_dict['发动机启动电门'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '发动机启动电门'))
            # return True, '近进阶段', '发动机启动电门'
        if "复飞高度" in text:
            order_dict['复飞高度_'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '复飞高度_'))
            # return True, '近进阶段', '复飞高度_'
        if "绿灯" in text:
            order_dict['_绿灯'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '_绿灯'))
            # return True, '近进阶段', '_绿灯'
        if "减速板" in text and "无" not in text and "升起" not in text:
            order_dict['减速板'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '减速板'))
            # return True, '近进阶段', '减速板'
        if ("APP" in text or "LOC" in text or "VOR" in text) and "进近" not in text:
            order_dict['APP预位/VOR/LOC预位'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', 'APP预位/VOR/LOC预位'))
            # return True, '近进阶段', 'APP预位/VOR/LOC预位'
        if "预位" in text and "进近" in text and "APP" in text:
            order_dict['进近航向_APP预位'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '进近航向_APP预位'))
            # return True, '近进阶段', '进近航向_APP预位'
        if "进近速度" in text:
            order_dict['进近速度_'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', '进近速度_'))
            # return True, '近进阶段', '进近速度_'
        if "APU" in text:
            order_dict['APU引气按需设置'] += 1
            self.last_stage = 2
            match_list.append(('近进阶段', 'APU引气按需设置'))
            # return True, '近进阶段', 'APU引气按需设置'
        for item in land_unique_order:
            if item in text:
                order_dict[item] += 1
                self.last_stage = 2
                match_list.append(('近进阶段', item))
                # return True, '近进阶段', item

        # 下降阶段
        order_dict = self.order_dict['下降阶段']
        land_unique_order = ["增压", "最大着陆重量"]  # 可以唯一确定的指令
        if "下降检查单完成" in text:
            order_dict['下降检查单完成'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '下降检查单完成'))
            # return True, '下降阶段', '下降检查单完成'
        elif "下降检查单" in text:
            order_dict['下降检查单'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '下降检查单'))
            # return True, '下降阶段', '下降检查单'
        if "进近检查单完成" in text:
            order_dict['进近检查单完成'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '进近检查单完成'))
            # return True, '下降阶段', '进近检查单完成'
        elif "进近检查单" in text:
            order_dict['进近检查单'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '进近检查单'))
            # return True, '下降阶段', '进近检查单'
        if "着陆高度" in text:
            order_dict['着陆高度_'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '着陆高度_'))
            # return True, '下降阶段', '着陆高度_'
        if "再现" in text:
            order_dict['再现'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '再现'))
            # return True, '下降阶段', '再现'
        # _ 无法判断
        if "自动刹车" in text and "工作" not in text and "解除" not in text:
            order_dict['自动刹车'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '自动刹车'))
            # return True, '下降阶段', '自动刹车'
        if "着陆数据" in text:
            order_dict['着陆数据'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '着陆数据'))
            # return True, '下降阶段', '着陆数据'
        if ("minimums" in text or "MINIMUMS" in text) and "VREF" in text:  # 特殊情况 没有 VREF
            order_dict['VREF_Minimums_'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', 'VREF_Minimums_'))
            # return True, '下降阶段', 'VREF_Minimums_'
        if "进近简令" in text:
            order_dict['进近简令'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '进近简令'))
            # return True, '下降阶段', '进近简令'
        if "完成" in text and "检查单" not in text:
            order_dict['完成'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '完成'))
            # return True, '下降阶段', '完成'
        if "过渡高度层" in text or "过度高度层" in text:
            order_dict['过渡高度层'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '过渡高度层'))
            # return True, '下降阶段', '过渡高度层'
        if text == "高度表":  # 特殊情况 高度表_ 与 高度表、_
            order_dict['高度表'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '高度表'))
            # return True, '下降阶段', '高度表'
        elif text.startswith("高度表"):
            order_dict['高度表_'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '高度表_'))
            # return True, '下降阶段', '高度表_'
        if "航道" in text and "导航频率" in text:
            order_dict['航道导航频率调定'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '航道导航频率调定'))
            # return True, '下降阶段', '航道导航频率调定'
        if ("10000" in text and "开灯" in text) or ("一万" in text and "开灯" in text):  # 特殊情况 10000开灯
            order_dict['10000'] += 1
            order_dict['开灯'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '10000'))
            # return True, '下降阶段', '10000'
        elif "开灯" in text and "检查" not in text:
            order_dict['开灯'] += 1
            self.last_stage = 1
            match_list.append(('下降阶段', '开灯'))
            # return True, '下降阶段', '开灯'
        for item in land_unique_order:
            if item in text:
                order_dict[item] += 1
                self.last_stage = 1
                match_list.append(('下降阶段', item))
                # return True, '下降阶段', item

        # 着陆阶段
        order_dict = self.order_dict['着陆阶段']
        land_unique_order = ["拉平预位", "频闪灯"]  # 可以唯一确定的指令
        if "继续" in text or "落地" in text:
            order_dict['继续/落地'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '继续/落地'))
            # return True, '着陆阶段', '继续/落地'
        if "继续" in text:
            order_dict['继续'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '继续'))
            # return True, '着陆阶段', '继续'
        if "FAF" in text:  # 特殊情况 FAF高度_
            order_dict['OM/FAP高度_'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', 'OM/FAP高度_'))
            # return True, '着陆阶段', 'OM/FAP高度_'
        if ("稳定" in text and "1000" in text) or ("稳定" in text and "一千" in text):
            order_dict['1000稳定'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '1000稳定'))
            # return True, '着陆阶段', '1000稳定'
        elif ("不稳定" in text and "1000" in text) or ("不稳定" in text and "一千" in text):
            order_dict['1000不稳定'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '1000不稳定'))
            # return True, '着陆阶段', '1000不稳定'
        if ("检查" in text and "开灯" in text) or ("复飞" in text and "高度" not in text):
            order_dict['检查开灯/复飞'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '检查开灯/复飞'))
            # return True, '着陆阶段', '检查开灯/复飞'
        if ("检查" in text and "开灯" not in text and "单" not in text) or ("复飞" in text and "高度" not in text):
            order_dict['检查/复飞'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '检查/复飞'))
            # return True, '着陆阶段', '检查/复飞'
        if ("稳定" in text and "500" in text) or ("稳定" in text and "五百" in text):
            order_dict['500稳定'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '500稳定'))
            # return True, '着陆阶段', '500稳定'
        elif ("不稳定" in text and "500" in text) or ("不稳定" in text and "五百" in text):
            order_dict['500不稳定'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '500不稳定'))
            # return True, '着陆阶段', '500不稳定'
        if ("差100" in text) or ("差一百" in text):
            order_dict['差100'] += 1  # 特殊情况 差1000
            self.last_stage = 3
            match_list.append(('着陆阶段', '差100'))
            # return True, '着陆阶段', '差100'
        if ("稳定" in text and "300" in text) or ("稳定" in text and "三百" in text):
            order_dict['300稳定'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '300稳定'))
            # return True, '着陆阶段', '300稳定'
        elif ("不稳定" in text and "300" in text) or ("不稳定" in text and "三百" in text):
            order_dict['300不稳定'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', '300不稳定'))
            # return True, '着陆阶段', '300不稳定'
        if "minimum" in text or "MINIMUM" in text:  # 特殊情况 MINIMUM1880
            order_dict['MINIMUMS_'] += 1
            self.last_stage = 3
            match_list.append(('着陆阶段', 'MINIMUMS_'))
            # return True, '着陆阶段', 'MINIMUMS_'
        for item in land_unique_order:
            if item in text:
                order_dict[item] += 1
                self.last_stage = 3
                match_list.append(('着陆阶段', item))
                # return True, '着陆阶段', item

        # 着陆滑跑阶段
        order_dict = self.order_dict['着陆滑跑阶段']
        land_unique_order = ["自动刹车工作"]  # 可以唯一确定的指令
        if "减速板升起" in text:
            order_dict['减速板升起/无减速板'] += 1  # 特殊情况 接地，减速板升起
            self.last_stage = 4
            match_list.append(('着陆滑跑阶段', '减速板升起/无减速板'))
            # return True, '着陆滑跑阶段', '减速板升起/无减速板'
        if "无减速板" in text:
            order_dict['减速板升起/无减速板'] += 1  # 特殊情况 接地，减速板升起
            self.last_stage = 4
            match_list.append(('着陆滑跑阶段', '减速板升起/无减速板'))
            # return True, '着陆滑跑阶段', '减速板升起/无减速板'
        if "自动刹车解除" in text:
            order_dict['自动刹车解除'] += 1  # 特殊情况 自动刹车解除，使用人工刹车
            self.last_stage = 4
            match_list.append(('着陆滑跑阶段', '自动刹车解除'))
            # return True, '着陆滑跑阶段', '自动刹车解除'
        if "无反推" in text or "反推正常" in text:
            order_dict['反推正常/_发无反推/无反推'] += 1
            self.last_stage = 4
            match_list.append(('着陆滑跑阶段', '反推正常/_发无反推/无反推'))
            # return True, '着陆滑跑阶段', '反推正常/_发无反推/无反推'
        if text == "60" or ("60" in text and "节" in text) or text == "六十":  # 特殊情况 60节
            order_dict['60'] += 1
            self.last_stage = 4
            match_list.append(('着陆滑跑阶段', '60'))
            # return True, '着陆滑跑阶段', '60'
        for item in land_unique_order:
            if item in text:
                order_dict[item] += 1
                self.last_stage = 4
                match_list.append(('着陆滑跑阶段', item))
                # return True, '着陆滑跑阶段', item

        # 多阶段重复特判
        if "核实" in text:
            if self.last_stage <= 1:
                self.order_dict['下降阶段']['核实'] += 1
                self.last_stage = 1
                match_list.append(('下降阶段', '核实'))
                # return True, '下降阶段', '核实'
            else:
                self.order_dict['近进阶段']['核实'] += 1
                self.last_stage = 2
                match_list.append(('近进阶段', '核实'))
                # return True, '近进阶段', '核实'
        if "检查" == text:
            if self.last_stage <= 1:
                self.order_dict['下降阶段']['检查'] += 1
                self.last_stage = 1
                match_list.append(('下降阶段', '检查'))
                # return True, '下降阶段', '检查'
            else:
                self.order_dict['着陆阶段']['检查'] += 1
                self.last_stage = 3
                match_list.append(('着陆阶段', '检查'))
                # return True, '着陆阶段', '检查'
        if len(match_list) == 0:
            return False, match_list
        else:
            return True, match_list

    def clear(self):
        for key in self.order_dict:
            order_dict = self.order_dict[key]
            for k in order_dict:
                order_dict[k] = 0
        self.last_stage = 0


    def get_dicts(self):
        return self.order_dict

'''
reco = Text2order('./order(1)(1).json')
reco.text2order('下降检查单')
print(reco.get_dicts())
reco.clear()
print(reco.get_dicts())
'''