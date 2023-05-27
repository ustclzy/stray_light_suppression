import numpy as np
import matplotlib.pyplot as plt
import os

from lvm import read_data as lvm_data
from nlj import read_data as nlj_data



def compare_result(a_index,b_index,nlj_result,lvm_result):
    nlj_old = nlj_result[str(a_index)]
    nlj_new = nlj_result[str(b_index)]
    lvm_old = lvm_result[str(a_index)]
    lvm_new = lvm_result[str(b_index)]
    lvm_diff_percent = (lvm_new - lvm_old) / lvm_old * 100
    nlj_diff_percent = (nlj_new - nlj_old) / nlj_old * 100
    print(f"LVM: {lvm_old} -> {lvm_new} ({lvm_diff_percent:.2f}%)")
    print(f"NLJ: {nlj_old} -> {nlj_new} ({nlj_diff_percent:.2f}%)")
    print(f"Energy Loss: {lvm_diff_percent - nlj_diff_percent:.2f}%")
    return lvm_diff_percent,nlj_diff_percent


if __name__ == "__main__":
    nlj = nlj_data(r"C:\Users\duan'we'hua\Desktop\stray_light_suppression\data\0526-nengliangji")
    lvm = lvm_data(r"C:\Users\duan'we'hua\Desktop\stray_light_suppression\data\0526")
    # print(nlj)
    # print(lvm)
    # # 绘制柱状图，x轴为nlj的key，y轴为nlj的value以及lvm的value，nlj和lvm的key相同，颜色不一样，图例显示
    # x = np.array(sorted([int(_data) for _data in nlj.keys()]))
    # nlj_values = [nlj[str(_data)] for _data in x]
    # lvm_values = [lvm[str(_data)] for _data in x]
    # width = 0.35
    # fig, ax = plt.subplots()
    # rects1 = ax.bar(x - width / 2, nlj_values, width, label='nlj')
    # rects2 = ax.bar(x + width / 2, lvm_values, width, label='lvm')
    # ax.set_ylabel('avg')
    # ax.set_title('avg by nlj and lvm')
    
    # # set_xticklabels 1:1,2:2,3:3,4,5,...11
    # xticks = [str(_data) for _data in x]
    # print(xticks)
    # # set xticks
    # ax.set_xticks(x)
    # ax.legend()
    # fig.tight_layout()
    # plt.show()

    compare_result(2,7,nlj,lvm)