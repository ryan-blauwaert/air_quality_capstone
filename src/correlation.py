import pandas as pd
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from air_quality_cleaning_and_aggregation import append_dataframes
plt.style.use('seaborn-darkgrid')


def get_pvalue_from_corr(r, n):
    t_stat = (r*(np.sqrt(n-2)))/(np.sqrt(1-r**2))
    return t.sf(abs(t_stat), df=n-2)


def correlation_by_city(air_df, inf_mor_df, n):
    inf_mor.columns = inf_mor.columns.astype(int)
    city_dfs = []
    for city in air_df.index.unique():
        if city not in ['National Means', 'National First Quartile', 'National Median', 'National Third Quartile']:
            df = air_df.loc[city]
            df.set_index('Year', drop=True, inplace=True)
            df = df.transpose()
            df = df.append(inf_mor_df.loc[city])
            df = df.rename(index={city:'Infant Mortality'})
            df.drop(index='Lead Max 3-Mo Avg', inplace=True)
            corr = df.corrwith(df.loc['Infant Mortality'], axis=1)
            corr = pd.DataFrame(data=corr, columns=['Correlation Coefficient'])
            corr.drop(index='Infant Mortality', inplace=True)
            corr.reset_index(inplace=True)
            corr.insert(0, 'Location', city)
            corr['p-value'] = get_pvalue_from_corr(corr['Correlation Coefficient'], n)
            corr['Significant?'] = corr['p-value'] <= .025
            city_dfs.append(corr)
    return city_dfs


if __name__ == '__main__':

    np.seterr(divide='ignore')

    all_air = pd.read_csv('../data/cleaned/air_all_years.csv', index_col='Location')
    inf_mor = pd.read_csv('../data/cleaned/infant_mortality_plus_stats.csv', index_col='Location')


    city_df_lists = correlation_by_city(all_air, inf_mor)
    # print(city_df_lists[5])

    # append_dataframes(city_df_lists, '../data/cleaned/all_cities_correlation.csv')

    all_cities_corr = pd.read_csv('../data/cleaned/all_cities_correlation.csv')
    