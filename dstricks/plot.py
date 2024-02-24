import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
    
def cat_plot(data: pd.DataFrame, target: str, cat_cols: list, figsize: tuple=(8, 4), stacked: bool=True, show_legend: bool=True):
    """
    data: dataframe
    target: target column on y axis
    cat_cols: all your categorical columns
    figsize: the figure size (l x w)
    stacked: bar charts stack 
    """
    for i in cat_cols:
        if i!=target:
            plot_data = (pd.crosstab(data[i],data[target],normalize='index')*100)
            plot_data.plot(kind='bar',figsize=figsize, stacked=stacked, legend=show_legend)
            plt.ylabel(target)
            plt.show()

def dist_box_plot(data: pd.DataFrame, num_cols: list, figsize: tuple=(12, 3)):
    for i in num_cols:
        fig, ax = plt.subplots(1, 2, figsize=(12, 3))
        sns.histplot(data, x=i, kde=True, ax=ax[0], palette='winter')
        sns.boxplot(data, x=i, ax=ax[1], showmeans=True)
        plt.show()
