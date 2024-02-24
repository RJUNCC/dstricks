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

def labeled_barplot(data, feature, perc=False, n=None):
    """
    Barplot with percentage at the top

    data: dataframe
    feature: dataframe column
    perc: whether to display percentages instead of count (default is False)
    n: displays the top n category levels (default is None, i.e., display all levels)
    """

    total = len(data[feature])  # length of the column
    count = data[feature].nunique()
    # if n is None:
    #     plt.figure(figsize=(count + 1, 5))
    # else:
    #     plt.figure(figsize=(n + 1, 5))

    plt.xticks(rotation=90, fontsize=15)
    ax = sns.countplot(
        data=data,
        x=feature,
        palette="Paired",
        order=data[feature].value_counts().index[:n].sort_values(),
    )

    for p in ax.patches:
        if perc == True:
            label = "{:.1f}%".format(
                100 * p.get_height() / total
            )  # percentage of each class of the category
        else:
            label = p.get_height()  # count of each level of the category

        x = p.get_x() + p.get_width() / 2  # width of the plot
        y = p.get_height()  # height of the plot

        ax.annotate(
            label,
            (x, y),
            ha="center",
            va="center",
            size=12,
            xytext=(0, 5),
            textcoords="offset points",
        )  # annotate the percentage

    plt.show()

def biBox(data, y, num_cols = x=None):
    temp1 = 0
    temp2 = 0
    fig, ax = plt.subplots(2, 4, figsize=(17, 10))
    for col in num_cols:
        if col != y:
            sns.boxplot(data=data, x=col, y=y, ax=ax[temp2, temp1])
            sns.histplot(data=data, x=col, ax=ax[temp2+1, temp1])
            temp1 = temp1 + 1
        else:
            continue
    plt.show()