import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import scipy.stats as stats
import seaborn as sns

plt.style.use('seaborn-darkgrid')
colors = sns.color_palette()


def plot_metric_line(df, metric, ax, color, label):
    '''
    DOCSTRING
    '''
    ax.plot(df.columns, df.loc[metric], color=colors[i], lw=3, label=label)
    

def get_colors(df, location, column):
    df = df.loc[location]
    color_lst = []
    for val in df[column]:
        if val:
            color_lst.append('blue')
        else:
            color_lst.append('red')
    return color_lst


def get_corr_bar(df, location, ax, color_col):
    df = df.loc[location]
    color_lst = get_colors(df, location, color_col)
    colors_dict = {'Not Significant':'red', 'Significant':'blue'}         
    labels = list(colors_dict.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors_dict[label]) for label in labels]
    ax.barh(df['index'], df['Correlation Coefficient'], color=color_lst)
    ax.set_ylabel('Metric', size=20)
    ax.set_xlabel('Correlation Coefficient', size=20)
    ax.legend(handles, labels, fontsize=14)


def get_pvalue_bar(df, ax, y_vals, widths):
    d = {'metrics':y_vals, 'significance ratio':widths}
    df = pd.DataFrame(data=d)
    df = df.sort_values('significance ratio', ascending=True)
    ax.barh(df['metrics'], df['significance ratio'], tick_label=df['metrics'])
    ax.set_title('Rate of Correlation Significance by Metric', size=32)
    ax.set_ylabel('Metric', fontsize=24)
    ax.set_xlabel('Rate at which Correlation is Significant', fontsize=24)


if __name__ == '__main__':
    
    palette = itertools.cycle(colors)
    metrics = ['CO 2nd Max 1-hr', 'SO2 2nd Max 24-hr', 'Ozone 4th Max 8-hr', 'PM2.5 98th Percentile 24-hr',
    'Infant Mortality Rate', 'Asthma Hosp. Rate']
    titles = ['Carbon Monoxide','Sulfur Dioxide','Ozone','Particulate Matter','Infant Mortality',
    'Childhood Asthma Hospitalizations']
    y_labels = ['Concentration, ppm', 'Concentration, ppb', 'Concentration, ppm', 'Concentration, ug/m3',
    'Deaths per 1,000 Births', 'Hosp. per 10,000 Children']
    title = 'New York City Air Pollution and Health Outcomes'
    new_york = pd.read_csv('../data/cleaned/new_york.csv', index_col = 'Unnamed: 0')

    fig, axs = plt.subplots(6, 1, figsize = (12, 16), sharex=True)
    for i, ax in enumerate(axs.flatten()):
        plot_metric_line(new_york, metrics[i], ax, colors[i], titles[i])
        ax.set_ylabel(y_labels[i], size=14)
        ax.legend(loc=1, fontsize=16)
    ax.set_xlabel('Year', size=20)
    fig.suptitle(title, x=.52, y=.99, size=24)
    plt.xticks(rotation=60, fontsize=16)
    fig.tight_layout()
    plt.savefig('../images/nyc_plots_1.png')
    plt.show()


    q1 = pd.read_csv('../data/cleaned/q1.csv', index_col='Unnamed: 0')
    medians = pd.read_csv('../data/cleaned/median.csv', index_col='Unnamed: 0')
    q3 = pd.read_csv('../data/cleaned/q3.csv', index_col='Unnamed: 0')

    dataframes = [q1, medians, q3]

    metrics = ['CO 2nd Max 1-hr', 'SO2 2nd Max 24-hr', 'Ozone 4th Max 8-hr', 'PM2.5 98th Percentile 24-hr',
     'Infant Mortality']
    titles = ['Carbon Monoxide','Sulfur Dioxide','Ozone','Particulate Matter','Infant Mortality',]
    y_labels = ['Concentration, ppm', 'Concentration, ppb', 'Concentration, ppm', 'Concentration, ug/m3',
    'Deaths per 1,000 Births']
    title = 'National Air Pollution and Infant Mortality Interquartile Range'
    medians = pd.read_csv('../data/cleaned/median.csv', index_col='Unnamed: 0')

    fig, axs = plt.subplots(5, 1, figsize=(12,16), sharex=True)
    count = 1
    for df in dataframes:
        for i, ax in enumerate(axs.flatten()):
            if count == 1:
                label=titles[i]
            else:
                label=None
            plot_metric_line(df, metrics[i], ax, color=colors[i], label=label)
        count +=1
    for i, ax in enumerate(axs.flatten()):
        color=colors[i]
        ax.set_ylabel(y_labels[i], size=14)
        ax.legend(loc=1, fontsize=16)
        ax.fill_between(x=dataframes[0].columns, y1=dataframes[0].loc[metrics[i]],
        y2=dataframes[-1].loc[metrics[i]], color=color, alpha=.2)
    ax.set_xlabel('Year', size=20)
    fig.suptitle(title, x=.52, y=.99, size=24)
    plt.xticks(rotation=60, fontsize=16)
    fig.tight_layout()
    plt.savefig('../images/interquartile_1.png')
    plt.show()

    all_cities_corr = pd.read_csv('../data/cleaned/all_cities_correlation_1.csv', index_col='Location')

    # print(all_cities_corr.head())

    fig, ax = plt.subplots(figsize=(12, 8))
    get_corr_bar(all_cities_corr, 'Denver', ax, 'Significant?')
    ax.set_title('Denver Infant Mortality Correlation and Significance', size=32, x=.4)
    ax.set_ylabel('Metric', size=20)
    ax.set_xlabel('Correlation Coefficient', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    fig.tight_layout()
    plt.savefig('../images/denver_corr_sig_1.png')
    plt.show()


    fig, ax = plt.subplots(figsize=(12, 8))
    get_corr_bar(all_cities_corr, 'New York City', ax, 'Significant?')
    ax.set_title('NYC Asthma Correlation and Significance', size=32, x=.4)
    ax.set_ylabel('Metric', size=20)
    ax.set_xlabel('Correlation Coefficient', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    fig.tight_layout()
    plt.savefig('../images/asthma_corr_sig_1.png')
    plt.show()


    fig, ax = plt.subplots(figsize=(12,8))
    y_vals = all_cities_corr['index'].unique()
    widths = []
    for metric in y_vals:
        data = all_cities_corr.loc[all_cities_corr['index']==metric, 'Significant?']
        widths.append(sum(data)/len(data))
    get_pvalue_bar(all_cities_corr, ax, y_vals, widths)
    fig.tight_layout()
    plt.savefig('../images/corr_sig_rates_1.png')
    plt.show()