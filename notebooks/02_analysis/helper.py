import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

from time import time
from copy import deepcopy
from collections import OrderedDict


def bar_plot(stats:dict, w:int=20, h:int=7, r:int=300, d:float=0.3, count:bool=True, title:str='', min_cnt=100, file_name:str=''):
    """
    Plots a barplot.

    Input:
    w:int = width
    h:int = height
    r:int = degrees of rotation for xticks
    d:float = delta position for the xlabel
    count:bool = whether or not to include the count of each occurence
    title:str = the title
    min_cnt:int = the minimum count for the feature to be included
    file_name:str = path to save the plot
    """
    stats_avg, stats_cnt = dict(), dict()
    for i in stats:
        if stats[i].count() > min_cnt:
            stats_avg[i] = stats[i].mean()
            stats_cnt[i] = stats[i].count()
    _, ax = plt.subplots(figsize=(w,h))
    plt.bar(range(len(stats_avg)), list(stats_avg.values()), align='center')
    plt.xticks(range(len(stats_avg)), list(stats_avg.keys()), rotation=r)
    if count:
        for i, (j, v) in enumerate(stats_cnt.items()):
            if np.isfinite(stats_avg[j]): ax.text(i - d, stats_avg[j] + 0.003, str(v), color='blue', fontweight='bold')
    if len(title) > 0:
        plt.title(title)
    if len(file_name) > 0:
        plt.savefig('plots/'+file_name+'.png', transparent=True, bbox_inches='tight')
    plt.show()


def two_bar_plot(stats_1:dict, stats_2:dict, w:int=20, h:int=7, r:int=0, title:str='', legend:str='', count:bool=False, min_cnt:int=100, file_name:str=''):
    """
    Plots a barplot for two inputs.

    Input:
    w:int = width
    h:int = height
    r:int = degrees of rotation for xticks
    d:float = delta position for the xlabel
    count:bool = whether or not to include the count of each occurence
    title:str = the title
    min_cnt:int = the minimum count for the feature to be included
    file_name:str = path to save the plot
    """
    stats_1_avg, stats_2_avg = dict(), dict()
    stats_1_cnt, stats_2_cnt = dict(), dict()
    for i in stats_1:
        stats_1_avg[i] = stats_1[i].mean()
        stats_2_avg[i] = stats_2[i].mean()
        if i in stats_1: stats_1_cnt[i] = stats_1[i].count()
        if i in stats_2: stats_2_cnt[i] = stats_2[i].count()
    _, ax = plt.subplots(figsize=(w,h))
    plt.bar(np.arange(len(stats_1_avg))-.2, list(stats_1_avg.values()), width=.4, align='center')
    plt.bar(np.arange(len(stats_1_avg))+.2, list(stats_2_avg.values()), width=.4, align='center')
    plt.xticks(range(len(stats_1_avg)), list(stats_1_avg.keys()), rotation=r)
    if count:
        for j, (k, v) in enumerate(stats_1_cnt.items()):
            if np.isfinite(stats_1_avg[k]): ax.text(j-.4, stats_1_avg[k]+0.003, str(v), color='blue',   fontweight='bold')
        for j, (k, v) in enumerate(stats_2_cnt.items()):
            if np.isfinite(stats_2_avg[k]): ax.text(j-.2, stats_2_avg[k]+0.003, str(v), color='orange', fontweight='bold')
    if len(title) > 0:
        plt.title(title)
    if len(legend) > 0:
        plt.legend(legend)
    if len(file_name) > 0:
        plt.savefig('plots/'+file_name+'.png', transparent=True, bbox_inches='tight')
    plt.show()


def three_bar_plot(stats_1:dict, stats_2:dict, stats_3:dict, w:int=20, h:int=7, r:int=0, title:str='', legend:str='', count=False, min_cnt:int=100, file_name:str=''):
    """
    Plots a barplot for three inputs.

    Input:
    w:int = width
    h:int = height
    r:int = degrees of rotation for xticks
    d:float = delta position for the xlabel
    count:bool = whether or not to include the count of each occurence
    title:str = the title
    min_cnt:int = the minimum count for the feature to be included
    file_name:str = path to save the plot
    """
    stats_1_avg, stats_2_avg, stats_3_avg = dict(), dict(), dict()
    stats_1_cnt, stats_2_cnt, stats_3_cnt = dict(), dict(), dict()
    for i in stats_1:
        #if stats_1[i].count() > min_cnt and stats_2[i].count() > min_cnt and stats_3[i].count() > min_cnt:
        stats_1_avg[i] = stats_1[i].mean()
        stats_2_avg[i] = stats_2[i].mean()
        stats_3_avg[i] = stats_3[i].mean()
        if i in stats_1: stats_1_cnt[i] = stats_1[i].count()
        if i in stats_2: stats_2_cnt[i] = stats_2[i].count()
        if i in stats_3: stats_3_cnt[i] = stats_3[i].count()
    _, ax = plt.subplots(figsize=(w,h))
    plt.bar(np.arange(len(stats_1_avg))-.2, list(stats_1_avg.values()), width=.2, align='center')
    plt.bar(np.arange(len(stats_1_avg)),    list(stats_2_avg.values()), width=.2, align='center')
    plt.bar(np.arange(len(stats_1_avg))+.2, list(stats_3_avg.values()), width=.2, align='center')
    plt.xticks(range(len(stats_1_avg)), list(stats_1_avg.keys()), rotation=r)
    if count:
        for j, (k, v) in enumerate(stats_1_cnt.items()):
            if np.isfinite(stats_1_avg[k]): ax.text(j-.4, stats_1_avg[k]+0.003, str(v), color='blue',   fontweight='bold')
        for j, (k, v) in enumerate(stats_2_cnt.items()):
            if np.isfinite(stats_2_avg[k]): ax.text(j-.2, stats_2_avg[k]+0.003, str(v), color='orange', fontweight='bold')
        for j, (k, v) in enumerate(stats_3_cnt.items()):
            if np.isfinite(stats_3_avg[k]): ax.text(j,    stats_3_avg[k]+0.003, str(v), color='green',  fontweight='bold')
    if len(title) > 0:
        plt.title(title)
    if len(legend) > 0:
        plt.legend(legend)
    if len(file_name) > 0:
        plt.savefig('plots/'+file_name+'.png', transparent=True, bbox_inches='tight')
    plt.show()


def five_bar_plot(stats_1:dict, stats_2:dict, stats_3:dict, stats_4:dict, stats_5:dict, w:int=30, h:int=7, r:int=0, title:str='', legend:str='', count=False):
    """
    Plots a barplot for five inputs.

    Input:
    w:int = width
    h:int = height
    r:int = degrees of rotation for xticks
    d:float = delta position for the xlabel
    count:bool = whether or not to include the count of each occurence
    title:str = the title
    min_cnt:int = the minimum count for the feature to be included
    file_name:str = path to save the plot
    """
    stats_1_avg, stats_2_avg, stats_3_avg, stats_4_avg, stats_5_avg = dict(), dict(), dict(), dict(), dict()
    stats_1_cnt, stats_2_cnt, stats_3_cnt, stats_4_cnt, stats_5_cnt = dict(), dict(), dict(), dict(), dict()
    for i in stats_1:
        stats_1_avg[i] = stats_1[i].mean()
        stats_2_avg[i] = stats_2[i].mean()
        stats_3_avg[i] = stats_3[i].mean()
        stats_4_avg[i] = stats_4[i].mean()
        stats_5_avg[i] = stats_5[i].mean()
        if i in stats_1: stats_1_cnt[i] = stats_1[i].count()
        if i in stats_2: stats_2_cnt[i] = stats_2[i].count()
        if i in stats_3: stats_3_cnt[i] = stats_3[i].count()
        if i in stats_4: stats_4_cnt[i] = stats_4[i].count()
        if i in stats_5: stats_5_cnt[i] = stats_5[i].count()
    _, ax = plt.subplots(figsize=(w,h))
    plt.bar(np.arange(len(stats_1_avg))-.2, list(stats_1_avg.values()), width=.1, align='center')
    plt.bar(np.arange(len(stats_1_avg))-.1, list(stats_2_avg.values()), width=.1, align='center')
    plt.bar(np.arange(len(stats_1_avg)),    list(stats_3_avg.values()), width=.1, align='center')
    plt.bar(np.arange(len(stats_1_avg))+.1, list(stats_4_avg.values()), width=.1, align='center')
    plt.bar(np.arange(len(stats_1_avg))+.2, list(stats_5_avg.values()), width=.1, align='center')
    plt.xticks(range(len(stats_1_avg)), list(stats_1_avg.keys()), rotation=r)
    if count:
        for j, (k, v) in enumerate(stats_1_cnt.items()):
            if np.isfinite(stats_1_avg[k]): ax.text(j-.3, stats_1_avg[k]+0.003, str(v), color='blue',   fontweight='bold')
        for j, (k, v) in enumerate(stats_2_cnt.items()):
            if np.isfinite(stats_2_avg[k]): ax.text(j-.2, stats_2_avg[k]+0.003, str(v), color='orange', fontweight='bold')
        for j, (k, v) in enumerate(stats_3_cnt.items()):
            if np.isfinite(stats_3_avg[k]): ax.text(j-.1, stats_3_avg[k]+0.003, str(v), color='green',  fontweight='bold')
        for j, (k, v) in enumerate(stats_4_cnt.items()):
            if np.isfinite(stats_4_avg[k]): ax.text(j,    stats_4_avg[k]+0.003, str(v), color='red',    fontweight='bold')
        for j, (k, v) in enumerate(stats_5_cnt.items()):
            if np.isfinite(stats_5_avg[k]): ax.text(j+.1, stats_5_avg[k]+0.003, str(v), color='purple', fontweight='bold')
    if len(title) > 0:
        plt.title(title)
    if len(legend) > 0:
        plt.legend(legend)
    plt.show()


def custom_round(x, base=5):
    return int(base * round(float(x)/base))