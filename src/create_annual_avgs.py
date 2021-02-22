import pandas as pd
import numpy as np



def create_grouped_dataframe(df_list, index_array, location_to_gather, write_to_location):
    df = pd.DataFrame(data=[], columns=df_list[0].columns)
    df = df.append([_.loc[_['Location'] == location_to_gather] for _ in df_list], 
    ignore_index=True)
    df.set_index(index_array, inplace=True)
    df.to_csv(write_to_location)


def transpose_df(df, write_to_location):
    df = df.transpose()
    cols =  np.arange(1999, 2019)
    df.columns = cols
    df.drop(index=['Unnamed: 0', 'Location'], inplace=True)
    df.to_csv(write_to_location)



if __name__ == '__main__':

    air_1999 = pd.read_csv('../data/cleaned/air_1999.csv')
    air_2000 = pd.read_csv('../data/cleaned/air_2000.csv')
    air_2001 = pd.read_csv('../data/cleaned/air_2001.csv')
    air_2002 = pd.read_csv('../data/cleaned/air_2002.csv')
    air_2003 = pd.read_csv('../data/cleaned/air_2003.csv')
    air_2004 = pd.read_csv('../data/cleaned/air_2004.csv')
    air_2005 = pd.read_csv('../data/cleaned/air_2005.csv')
    air_2006 = pd.read_csv('../data/cleaned/air_2006.csv')
    air_2007 = pd.read_csv('../data/cleaned/air_2007.csv')
    air_2008 = pd.read_csv('../data/cleaned/air_2008.csv')
    air_2009 = pd.read_csv('../data/cleaned/air_2009.csv')
    air_2010 = pd.read_csv('../data/cleaned/air_2010.csv')
    air_2011 = pd.read_csv('../data/cleaned/air_2011.csv')
    air_2012 = pd.read_csv('../data/cleaned/air_2012.csv')
    air_2013 = pd.read_csv('../data/cleaned/air_2013.csv')
    air_2014 = pd.read_csv('../data/cleaned/air_2014.csv')
    air_2015 = pd.read_csv('../data/cleaned/air_2015.csv')
    air_2016 = pd.read_csv('../data/cleaned/air_2016.csv')
    air_2017 = pd.read_csv('../data/cleaned/air_2017.csv')
    air_2018 = pd.read_csv('../data/cleaned/air_2018.csv')

    df_array = [air_1999, air_2000, air_2001, air_2002, air_2003, air_2004,
    air_2005, air_2006, air_2007, air_2008, air_2009, air_2010, air_2011,
    air_2012, air_2013, air_2014, air_2015, air_2016, air_2017, air_2018]

    index_array = pd.Series(range(1999, 2019))

    # create_averages_dataframe(df_array, index_array, 'National Means', 
    # '../data/cleaned/annual_air_data_means.csv')

    annual_means = pd.read_csv('../data/cleaned/annual_air_data_means.csv')
    # print(annual_means)
    # transpose_df(annual_means, '../data/cleaned/transposed_national_air_data.csv')

    transposed_national_air = pd.read_csv('../data/cleaned/transposed_national_air_data.csv', index_col='Unnamed: 0')
    print(transposed_national_air)
    inf_mor = pd.read_csv('../data/cleaned/infant_mortality_with_mean.csv', index_col='Location')
    print(inf_mor)
    transposed_national_air = transposed_national_air.append(inf_mor.loc['Infant Mortality Mean'])
    transposed_national_air.to_csv('../data/cleaned/transposed_national_air_data.csv')