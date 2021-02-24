import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import scipy.stats as stats
import seaborn as sns

plt.style.use('seaborn-darkgrid')
palette = itertools.cycle(sns.color_palette())


def plot_lines(df, metrics, ax_titles, y_labels, title, write_to):
    '''
    DOCSTRING
    '''
    fig, axs = plt.subplots(len(metrics), 1, figsize=(12, 16), sharex=True)
    for i, ax in enumerate(axs.flatten()):
        ax.plot(df.columns, df.loc[metrics[i]], color=next(palette), lw=3)
        ax.set_title(ax_titles[i], size=13)
        ax.set_ylabel(y_labels[i], size=13)
    ax.set_xlabel('Year', size=16)
    fig.suptitle(title, x=.52, y=.99, size=16)
    fig.tight_layout()
    plt.xticks(rotation=30)
    plt.savefig(write_to)

def plot_ranges(dfs, metrics, ax_titles, y_labels, title, write_to):
    '''
    DOCSTRING
    '''
    fig, axs = plt.subplots(len(metrics), 1, figsize=(12, 16), sharex=True)
    # colors = 
    for df in dfs:
        for i, ax in enumerate(axs.flatten()):
            color = sns.color_palette()[i]
            ax.plot(df.columns, df.loc[metrics[i]], color=color, lw=2)
    for i, ax in enumerate(axs.flatten()):
        color = sns.color_palette()[i]
        ax.set_title(ax_titles[i], size=13)
        ax.set_ylabel(y_labels[i], size=13)
        ax.fill_between(x=dfs[0].columns, y1=dfs[0].loc[metrics[i]], y2=dfs[-1].loc[metrics[i]],
        color=color, alpha=.3)
    ax.set_xlabel('Year', size=16)
    fig.suptitle(title, x=.52, y=.99, size=16)
    fig.tight_layout()
    plt.xticks(rotation=30)
    plt.savefig(write_to)


if __name__ == '__main__':
    
    metrics = ['CO 2nd Max 1-hr', 'SO2 2nd Max 24-hr', 'Ozone 4th Max 8-hr', 'PM2.5 98th Percentile 24-hr',
    'Infant Mortality Rate', 'Asthma Hosp. Rate']
    titles = ['Carbon Monoxide','Sulfur Dioxide','Ozone','Particulate Matter','Infant Mortality',
    'Childhood Asthma Hospitalizations']
    y_labels = ['Concentration, ppm', 'Concentration, ppb', 'Concentration, ppm', 'Concentration, ug/m3',
    'Deaths per 1,000 Births', 'Hosp. per 10,000 Children']
    title = 'New York City Air Pollution and Health Outcomes'
    new_york = pd.read_csv('../data/cleaned/new_york.csv', index_col = 'Unnamed: 0')
    # print(new_york)
    plot_lines(new_york, metrics, titles, y_labels, title, '../images/nyc_plots.png')

    metrics = ['CO 2nd Max 1-hr', 'SO2 2nd Max 24-hr', 'Ozone 4th Max 8-hr', 'PM2.5 98th Percentile 24-hr',
     'Infant Mortality']
    titles = ['Carbon Monoxide','Sulfur Dioxide','Ozone','Particulate Matter','Infant Mortality',]
    y_labels = ['Concentration, ppm', 'Concentration, ppb', 'Concentration, ppm', 'Concentration, ug/m3',
    'Deaths per 1,000 Births']
    title = 'National Air Pollution and Infant Mortality Medians'
    medians = pd.read_csv('../data/cleaned/median.csv', index_col='Unnamed: 0')
    # plot_lines(medians, metrics, titles, y_labels, title, '../images/medians_test.png')


    q1 = pd.read_csv('../data/cleaned/q1.csv', index_col='Unnamed: 0')
    q3 = pd.read_csv('../data/cleaned/q3.csv', index_col='Unnamed: 0')

    title = 'National Air Pollution and Infant Mortality Inner Quartile Range'
    # plot_ranges([q1, medians, q3], metrics, titles, y_labels, title, '../images/inner_quartile.png')
    