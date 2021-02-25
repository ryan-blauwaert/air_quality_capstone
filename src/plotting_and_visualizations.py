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
        ax.plot(df.columns, df.loc[metrics[i]], color=next(palette), lw=3, label=ax_titles[i])
        ax.legend(loc=1, fontsize=16)
        ax.set_ylabel(y_labels[i], size=14)
    ax.set_xlabel('Year', size=20)
    fig.suptitle(title, x=.52, y=.99, size=24)
    plt.xticks(rotation=60, fontsize=16)
    fig.tight_layout()
    plt.savefig(write_to)
    # plt.show()

def plot_ranges(dfs, metrics, ax_titles, y_labels, title, write_to):
    '''
    DOCSTRING
    '''
    fig, axs = plt.subplots(len(metrics), 1, figsize=(12, 16), sharex=True)
    count = 1
    for df in dfs:
        for i, ax in enumerate(axs.flatten()):
            color = sns.color_palette()[i]
            if count == 1:
                ax.plot(df.columns, df.loc[metrics[i]], color=color, lw=2, label=ax_titles[i])
            else:
                ax.plot(df.columns, df.loc[metrics[i]], color=color, lw=2)
        count += 1           
    for i, ax in enumerate(axs.flatten()):
        color = sns.color_palette()[i]
        ax.set_ylabel(y_labels[i], size=14)
        ax.legend(loc=1, fontsize=16)
        ax.fill_between(x=dfs[0].columns, y1=dfs[0].loc[metrics[i]], y2=dfs[-1].loc[metrics[i]],
        color=color, alpha=.2)
    ax.set_xlabel('Year', size=20)
    fig.suptitle(title, x=.52, y=.99, size=24)
    plt.xticks(rotation=60, fontsize=16)
    fig.tight_layout()
    plt.savefig(write_to)
    # plt.show()


def get_pvalue_bar(df, write_to):
    y_vals = df['index'].unique()
    widths = []
    for metric in y_vals:
        data = df.loc[df['index']==metric, 'Significant?']
        widths.append(sum(data)/len(data))
    d = {'metrics':y_vals, 'significance ratio':widths}
    df = pd.DataFrame(data=d)
    df = df.sort_values('significance ratio', ascending=True)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(df['metrics'], df['significance ratio'], tick_label=df['metrics'])
    ax.set_title('Rate of p-value Significance by Metric', size=32)
    ax.set_ylabel('Metric', fontsize=24)
    ax.set_xlabel('Rate at which p-value is Significant', fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    fig.tight_layout()
    plt.savefig(write_to)
    # plt.show()


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
    # plot_lines(new_york, metrics, titles, y_labels, title, '../images/nyc_plots.png')

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
    
    all_cities_corr = pd.read_csv('../data/cleaned/all_cities_correlation.csv')
    # get_pvalue_bar(all_cities_corr, '../images/corr_sig_rates.png')
    
    denver = pd.read_csv('../data/cleaned/denver.csv', index_col='Unnamed: 0')
    metrics = ['CO 2nd Max 1-hr', 'SO2 2nd Max 24-hr', 'Ozone 4th Max 8-hr', 'PM2.5 98th Percentile 24-hr',
     'Infant Mortality Rate']
    title = 'Denver Air Pollution and Infant Mortality'
    plot_lines(denver, metrics, titles, y_labels, title, '../images/denver.png')