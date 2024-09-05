import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from scipy.stats import gaussian_kde
rainfall = np.loadtxt(r"D:\phd_research\grd\data\trend_p\total_trend.txt")
rainfall = rainfall * 10
a = np.loadtxt(r"D:\phd_research\grd\data/region.txt")
fig, axes = plt.subplots(nrows=7, ncols=1, figsize=(9, 50), dpi=400)
num = 7
for ax in axes:
    urbanlist = []
    countrylist = []
    for i in range(1544):
        if rainfall[int(a[i,3]),num] > -999:
            if a[i,-2]>0:
                urbanlist.append(rainfall[int(a[i,3]),num])
            else:
                countrylist.append(rainfall[int(a[i,3]),num])
    num+=1
    density = gaussian_kde(urbanlist)
    x_vals = np.linspace(min(urbanlist), max(urbanlist), 1000)
    density.covariance_factor = lambda : 0.25
    density._compute_covariance()

    density1 = gaussian_kde(countrylist)
    x_vals1 = np.linspace(min(countrylist), max(countrylist), 1000)
    density1.covariance_factor = lambda : 0.25
    density1._compute_covariance()

    total = urbanlist+countrylist
    ax.plot(x_vals, density(x_vals), 'r-', linewidth=2) 
    ax.plot(x_vals1, density1(x_vals1), 'k--', linewidth=1) 
    # plt.xlabel('Trend',fontsize=18)
    # plt.ylabel('Density',fontsize=18)
    value = (max(total) - min(total)) / 2
    ax.set_xlim(-value, value)
    ax.locator_params(axis='x', nbins=6)
    ax.locator_params(axis='y', nbins=6)

    ax.grid(True, linestyle='--')
    ax.axvline(x=0, color='black', linestyle='-', linewidth=2)
    # ax=plt.gca()
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
plt.tight_layout()
plt.show()