import glob
import os
import random
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.feature
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import matplotlib.colors as colors
import cartopy.feature as cfeature
import seaborn as sns
import pandas as pd
from scipy.stats import norm
from scipy.stats import laplace
import matplotlib as mpl
from scipy import stats
import os
from scipy import optimize
import pymannkendall as mk
from matplotlib.colors import LogNorm
import cartopy.io.shapereader as shpreader
import json
import numpy as np
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

def num_to_color(num):
    if num < -7:
        return (231/255,98/255,84/255)
    elif num < -5:
        return (239/255,138/255,71/255)
    elif num < -3:
        return (247/255,170/255,88/255)
    elif num < -1:
        return (255/255,208/255,111/255)
    elif num < 1:
        return (255/255,230/255,183/255)
    elif num < 3:
        return (170/255,220/255,224/255)
    elif num < 5:
        return (114/255,188/255,213/255)
    elif num < 7:
        return (82/255,143/255,173/255)
    else:
        return (55/255,103/255,149/255)

filepath = r"D:\phd_research\grd\China_p.shp"
shape_feature = shpreader.Reader(filepath)
rainfall = np.loadtxt(r"D:\phd_research\grd\data\trend_p\total_trend.txt")
p = np.loadtxt(r"D:\phd_research\grd\data\trend_p\total_p.txt")
rainfall = rainfall * 1000
print(rainfall.shape)
a = np.loadtxt(r"D:\phd_research\grd\data/region.txt")
clist = []
plist = []

for i in range(1544):
    clist.append(rainfall[int(a[i,-3]),7])
    plist.append(p[int(a[i,-3]),7])

cmin , cmax = np.min(clist) , np.max(clist)

fig = plt.figure(figsize=(15, 7), dpi=400)

ax = plt.axes(projection=ccrs.PlateCarree())

ax.set_extent([72, 136, 17, 55],crs=ccrs.PlateCarree())  ##设置范围与投影方式
# gl = ax.gridlines( draw_labels=True, linewidth=0.1, color='gray', alpha=0.8, linestyle='-')
gl = ax.gridlines(draw_labels=True, linewidth=1, color='black', linestyle='-')
gl.xlabel_style = {'color': 'black', 'weight': 'bold', 'size': 10, 'rotation': 45, 'ha': 'right', 'va': 'top', 'pad': 10}
gl.ylabel_style = {'color': 'black', 'weight': 'bold', 'size': 10, 'rotation': 45, 'ha': 'right', 'va': 'top', 'pad': 10}
gl.xlocator = mticker.FixedLocator([ 75,90, 105, 120, 135])
gl.ylocator = mticker.FixedLocator([20,30, 40,50])
gl.xlabels_bottom = False  # 避免底部标签重叠
gl.xlabels_top = False     # 避免顶部标签重叠
gl.ylabels_left = False    # 避免左侧标签重叠
gl.ylabels_right = False   # 避免右侧标签重叠
gl.xformartter = LONGITUDE_FORMATTER
gl.yformartter = LATITUDE_FORMATTER
gl.xlabel_style = {'family': 'Times New Roman', 'size': 25, 'color': 'black'}
gl.ylabel_style = {'family': 'Times New Roman', 'size': 25, 'color': 'black'}
# ax.add_feature(cfeature.COASTLINE, lw=0.5, edgecolor='k')
gl.xlines = False
gl.ylines = False
# ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.5)
for i in range(len(plist)):
    if plist[i] < 0.1:
        scatter = plt.scatter(a[i, 2], a[i, 1], transform=ccrs.PlateCarree(), s=20, c=num_to_color(clist[i]),
                 marker='o')
    else:
        scatter = plt.scatter(a[i, 2], a[i, 1], transform=ccrs.PlateCarree(), s=20, c="none",
                 marker='o',linewidths=1,edgecolors = num_to_color(clist[i]) )

for shape in shape_feature.geometries():
    ax.add_geometries([shape], ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=2)

ax.set_xticks([ 75,90, 105, 120, 135], crs=ccrs.PlateCarree())
ax.set_yticks([20,30, 40,50], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
ax.tick_params(axis='both', which='major', labelsize=20,length = 10 ,width =2)
for spine in ax.spines.values():
    spine.set_linewidth(2)
plt.show()