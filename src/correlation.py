import pandas as pd
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from air_quality_cleaning_and_aggregation import append_dataframes
plt.style.use('seaborn-darkgrid')


def get_pvalue_from_corr(r, n):
    """Calculates a p-value using a two tailed t-test with 
    n-2 degrees of freedom

    Args:
        r (float): Pearson correlation coefficient
        n (int): number of samples used to calculate r

    Returns:
        [float]: p-value
    """
    t_stat = (r*(np.sqrt(n-2)))/(np.sqrt(1-r**2))
    return t.sf(abs(t_stat), df=n-2)


def correlation_by_city(df1, df2, location, n, alpha):
    """Combines data from two pandas DataFrames to provide 
    correlation coefficients, p-values, and significance
    for air quality metrics and health outcomes

    Args:
        df1 (pandas DataFrame): DataFrame containing air quality 
            data
        df2 (pandas DataFrame): DataFrame containing health outcome 
            data
        location (str): the name of the city for which correlation, 
            etc. is to be calculated
        n (int): number of samples being used to calculate correlation
            coefficient
        alpha (float): significance level against which p-value is to 
            be compared

    Returns:
        [type]: [description]
    """
    df = df1.loc[location]
    df.set_index('Year', drop=True, inplace=True)
    df = df.transpose()
    df = df.append(df2.loc[location])
    df = df.rename(index={location:'Infant Mortality'})
    df.drop(index='Lead Max 3-Mo Avg', inplace=True)
    corr = df.corrwith(df.loc['Infant Mortality'], axis=1)
    corr = pd.DataFrame(data=corr, columns=['Correlation Coefficient'])
    corr.drop(index='Infant Mortality', inplace=True)
    corr.reset_index(inplace=True)
    corr.insert(0, 'Location', location)
    corr['p-value'] = get_pvalue_from_corr(corr['Correlation Coefficient'], n)
    corr['Significant?'] = corr['p-value'] <= alpha/2
    return corr


if __name__ == '__main__':

    np.seterr(divide='ignore')

    all_air = pd.read_csv('../data/cleaned/air_all_years.csv', index_col='Location')
    inf_mor = pd.read_csv('../data/cleaned/infant_mortality_plus_stats.csv', index_col='Location')

    inf_mor.columns = [int(col) for col in inf_mor.columns]
    ignore = ['National Means', 'National First Quartile', 'National Median',
    'National Third Quartile']

    corr_df_lst = []

    for location in all_air.index.unique():
        if location not in ignore:
            df = correlation_by_city(all_air, inf_mor, location, 20, .05)
            corr_df_lst.append(df)

    # print(corr_df_lst[0])

    append_dataframes(corr_df_lst, '../data/cleaned/all_cities_correlation_1.csv')
    