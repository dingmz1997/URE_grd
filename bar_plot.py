import matplotlib.pyplot as plt
import numpy as np
from scipy import stats




# 绘制柱状图
fig, axes = plt.subplots(nrows=7, ncols=1, figsize=(9, 50), dpi=400)
num = 0
for ax in axes:
    value = num
    num+=1
    trend = np.loadtxt(r"D:\phd_research\grd\data\trend_p\total_trend.txt")
    trend = trend * 1000
    urbanlist = []
    countrylist = []
    a = np.loadtxt(r"D:\phd_research\grd\data/region.txt")
    for i in range(1544):
        if trend[int(a[i,3]),value] > -999:
                if a[i,-2]>0:
                    urbanlist.append(trend[int(a[i,3]),value])
                else:
                    countrylist.append(trend[int(a[i,3]),value])
    # 两个示例列表
    list1 = urbanlist
    list2 = countrylist
    mean_list1 = np.mean(list1)
    std_list1 = stats.sem(list1)
    conf_int1 = stats.t.interval(0.9, len(list1) - 1, loc=mean_list1, scale=std_list1)  # 90% 置信区间 
    mean_list2 = np.mean(list2)
    std_list2 = stats.sem(list1)
    conf_int2 = stats.t.interval(0.9, len(list2) - 1, loc=mean_list2, scale=std_list2)  # 90% 置信区间 
    diff_means = mean_list1 - mean_list2
    error_bar_list1 = (conf_int1[1] - conf_int1[0]) / 2
    error_bar_list2 = (conf_int2[1] - conf_int2[0]) / 2
    bar_data = [mean_list1, mean_list2, diff_means,0]
    error_bars = [error_bar_list1, error_bar_list2, 0,0]  # 差值无误差
    labels = ['Urban', 'Rural', 'Difference',""]
    colorlist = ["grey","lightgrey","red","black"]
    total_bar = []
    total_err = []
    total_lab = []
    total_col = []
    total_bar += bar_data
    total_err += error_bars
    total_lab += labels
    total_col += colorlist
    urbanlist = []
    countrylist = []
    for i in range(1544):
        if trend[int(a[i,3]),value] > -999:
            if  a[i,1] < 42 and a[i,1] >36 and a[i,2] < 119 and a[i,2] >111:
                if a[i,-2]>0:
                    urbanlist.append(trend[int(a[i,3]),value])
                else:
                    countrylist.append(trend[int(a[i,3]),value])
    list1 = urbanlist
    list2 = countrylist
    mean_list1 = np.mean(list1)
    std_list1 = stats.sem(list1)
    conf_int1 = stats.t.interval(0.9, len(list1) - 1, loc=mean_list1, scale=std_list1)  
    mean_list2 = np.mean(list2)
    std_list2 = stats.sem(list1)
    conf_int2 = stats.t.interval(0.9, len(list2) - 1, loc=mean_list2, scale=std_list2) 
    diff_means = mean_list1 - mean_list2
    error_bar_list1 = (conf_int1[1] - conf_int1[0]) / 2
    error_bar_list2 = (conf_int2[1] - conf_int2[0]) / 2
    bar_data = [mean_list1, mean_list2, diff_means,0]
    error_bars = [error_bar_list1, error_bar_list2, 0,0]  # 差值无误差
    labels = ['Urban', 'Rural', 'Difference',""]
    colorlist = ["grey","lightgrey","red","black"]
    total_bar += bar_data
    total_err += error_bars
    total_lab += labels
    total_col += colorlist

    urbanlist = []
    countrylist = []
    for i in range(1544):
        if trend[int(a[i,3]),value] > -999:
            if a[i,2] < 123 and a[i,2] >115.5 and a[i,1] < 33.5 and a[i,1] >27:
                if a[i,-2]>0:
                    urbanlist.append(trend[int(a[i,3]),value])
                else:
                    countrylist.append(trend[int(a[i,3]),value])
    list1 = urbanlist
    list2 = countrylist
    mean_list1 = np.mean(list1)
    std_list1 = stats.sem(list1)
    conf_int1 = stats.t.interval(0.9, len(list1) - 1, loc=mean_list1, scale=std_list1)  
    mean_list2 = np.mean(list2)
    std_list2 = stats.sem(list1)
    conf_int2 = stats.t.interval(0.9, len(list2) - 1, loc=mean_list2, scale=std_list2) 
    diff_means = mean_list1 - mean_list2
    error_bar_list1 = (conf_int1[1] - conf_int1[0]) / 2
    error_bar_list2 = (conf_int2[1] - conf_int2[0]) / 2
    bar_data = [mean_list1, mean_list2, diff_means,0]
    error_bars = [error_bar_list1, error_bar_list2, 0,0]  # 差值无误差
    labels = ['Urban', 'Rural', 'Difference',""]
    colorlist = ["grey","lightgrey","red","black"]
    total_bar += bar_data
    total_err += error_bars
    total_lab += labels
    total_col += colorlist

    urbanlist = []
    countrylist = []
    for i in range(1544):
        if trend[int(a[i,3]),value] > -999:
            if a[i,1] < 26 and a[i,1] >20.5 and a[i,2] < 118 and a[i,2] >110:
                if a[i,-2]>0:
                    urbanlist.append(trend[int(a[i,3]),value])
                else:
                    countrylist.append(trend[int(a[i,3]),value])
    list1 = urbanlist
    list2 = countrylist
    mean_list1 = np.mean(list1)
    std_list1 = stats.sem(list1)
    conf_int1 = stats.t.interval(0.9, len(list1) - 1, loc=mean_list1, scale=std_list1)  
    mean_list2 = np.mean(list2)
    std_list2 = stats.sem(list1)
    conf_int2 = stats.t.interval(0.9, len(list2) - 1, loc=mean_list2, scale=std_list2) 
    diff_means = mean_list1 - mean_list2
    error_bar_list1 = (conf_int1[1] - conf_int1[0]) / 2
    error_bar_list2 = (conf_int2[1] - conf_int2[0]) / 2
    bar_data = [mean_list1, mean_list2, diff_means,0]
    error_bars = [error_bar_list1, error_bar_list2, 0,0]  # 差值无误差
    labels = ['Urban', 'Rural', 'Difference',""]
    colorlist = ["grey","lightgrey","red","black"]
    total_bar += bar_data
    total_err += error_bars
    total_lab += labels
    total_col += colorlist
    x_pos = np.arange(len(total_bar))
    
    ax.bar(x_pos, total_bar,1, yerr=total_err, align='center', alpha=0.7, edgecolor='black', color=total_col)
    ax.set_xticks(x_pos)
    
    ax.set_ylabel('Slope (%/10y)', fontsize=20)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=2)
    ax.axvline(x=3, color='black', linestyle='--', linewidth=0.5)
    ax.axvline(x=7, color='black', linestyle='--', linewidth=0.5)
    ax.axvline(x=11, color='black', linestyle='--', linewidth=0.5)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['right'].set_color('black')
    ax.xaxis.set_tick_params(labelsize=24)
    ax.yaxis.set_tick_params(labelsize=24)
    for label in ax.get_yticklabels():
        label.set_fontname('Times New Roman')
    for label in ax.get_xticklabels():
        label.set_fontname('Times New Roman')
    ax.set_xlim([-1,len(x_pos)-1])
    plt.tight_layout()
plt.show()